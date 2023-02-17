# Copyright 2019 The dm_control Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""A task consisting of finding goals/targets in a random maze."""

import collections
import itertools

from dm_control import composer
from dm_control import mjcf
from dm_control.composer.observation import observable as observable_lib
from dm_control.locomotion.props import target_sphere
from dm_control.mujoco.wrapper import mjbindings
import numpy as np
import functools
from dm_control.utils import rewards


_NUM_RAYS = 10

# Aliveness in [-1., 0.].
DEFAULT_ALIVE_THRESHOLD = -0.5
# DEFAULT_ALIVE_THRESHOLD = -1.1


DEFAULT_PHYSICS_TIMESTEP = 0.001
DEFAULT_CONTROL_TIMESTEP = 0.025

def round(l, n=3):
    return list(np.around(np.array(l), n))

class NullGoalMaze(composer.Task):
  """A base task for maze with goals."""

  def __init__(self,
               walkers,
               maze_arena,
               primary_agent,
               randomize_spawn_position=True,
               randomize_spawn_rotation=True,
               spawn_rotation_radians=None,
               rotation_bias_factor=0,
               aliveness_reward=0.0,
               aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
               contact_termination=True,
               enable_global_task_observables=False,
               physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
               control_timestep=DEFAULT_CONTROL_TIMESTEP,
               nconmax=100,
               njmax=100,
               z_spawn=0.5,
               random_seed=None):
    """Initializes goal-directed maze task.

    Args:
      walkers: The body to navigate the maze.
      maze_arena: The physical maze arena object.
      primary_agent: key into walkers dict for the primary agent.
                     If None, then no primary agent will be designated.
      randomize_spawn_position: Flag to randomize position of spawning.
      randomize_spawn_rotation: Flag to randomize orientation of spawning.
      rotation_bias_factor: A non-negative number that concentrates initial
        orientation away from walls. When set to zero, the initial orientation
        is uniformly random. The larger the value of this number, the more
        likely it is that the initial orientation would face the direction that
        is farthest away from a wall.
      aliveness_reward: Reward for being alive.
      aliveness_thresh: Threshold if should terminate based on walker
        aliveness feature.
      contact_termination: whether to terminate if a non-foot geom touches the
        ground.
      enable_global_task_observables: Flag to provide task observables that
        contain global information, including map layout.
      physics_timestep: timestep of simulation.
      control_timestep: timestep at which agent changes action.
    """
    self._walkers = walkers
    self._primary_agent = primary_agent
    self._nw = len(walkers)
    self._z_spawn = z_spawn
    self._maze_arena = maze_arena
    for wk in self._walkers.keys():
        self._walkers[wk].create_root_joints(self._maze_arena.attach(self._walkers[wk]))

    self._randomize_spawn_position = randomize_spawn_position
    self._randomize_spawn_rotation = randomize_spawn_rotation
    self._spawn_rotation_radians = spawn_rotation_radians
    self._rotation_bias_factor = rotation_bias_factor

    self._aliveness_reward = aliveness_reward
    self._aliveness_thresh = aliveness_thresh
    self._contact_termination = contact_termination
    self._discount = 1.0
    self._random_seed=random_seed

    self.set_timesteps(
        physics_timestep=physics_timestep, control_timestep=control_timestep)

    only_enable_primary_agent_observables = True
    if only_enable_primary_agent_observables:
        keys = [self._primary_agent]
    else:
        keys = self._walkers.keys()
    for wk in keys:
        self._walkers[wk].observables.egocentric_camera.height = 64
        self._walkers[wk].observables.egocentric_camera.width = 64
        for observable in (self._walkers[wk].observables.proprioception +
                           self._walkers[wk].observables.kinematic_sensors +
                           self._walkers[wk].observables.dynamic_sensors):
          observable.enabled = True
        self._walkers[wk].observables.egocentric_camera.enabled = False  # Setting True leads to large replay buffer filesizes.


    if enable_global_task_observables:
      # Reveal maze text map as observable.
      maze_obs = observable_lib.Generic(
          lambda _: self._maze_arena.maze.entity_layer)
      maze_obs.enabled = True

      absolute_position = {}
      absolute_orientation = {}
      absolute_quaternion = {}
      absolute_position_discrete = {}
      # for ww in range(self._nw):
      for wk in self._walkers.keys():
          # absolute walker position
          def get_walker_pos(physics, k):
            walker_pos = physics.bind(self._walkers[k].root_body).xpos
            return walker_pos
          absolute_position[wk] = observable_lib.Generic(functools.partial(get_walker_pos, k=wk))
          absolute_position[wk].enabled = True

          # absolute walker orientation
          def get_walker_ori(physics, k):
            walker_ori = np.reshape(
                physics.bind(self._walkers[k].root_body).xmat, (3, 3))
            return walker_ori
          absolute_orientation[wk] = observable_lib.Generic(functools.partial(get_walker_ori, k=wk))
          absolute_orientation[wk].enabled = True

          # absolute walker orientation
          def get_walker_quat(physics, k):
              walker_ori = physics.bind(self._walkers[k].root_body).xquat
              return walker_ori

          absolute_quaternion[wk] = observable_lib.Generic(functools.partial(get_walker_quat, k=wk))
          absolute_quaternion[wk].enabled = True

          # grid element of player in maze cell: i,j cell in maze layout
          def get_walker_ij(physics, k):
            walker_xypos = physics.bind(self._walkers[k].root_body).xpos[:-1]
            walker_rel_origin = (
                (walker_xypos +
                 np.sign(walker_xypos) * self._maze_arena.xy_scale / 2) /
                (self._maze_arena.xy_scale)).astype(int)
            x_offset = (self._maze_arena.maze.width - 1) / 2
            y_offset = (self._maze_arena.maze.height - 1) / 2
            walker_ij = walker_rel_origin + np.array([x_offset, y_offset])
            return walker_ij
          absolute_position_discrete[wk] = observable_lib.Generic(functools.partial(get_walker_ij, k=wk))
          absolute_position_discrete[wk].enabled = True

      self._task_observables = collections.OrderedDict({
          'maze_layout': maze_obs,
      })
      self._task_observables[f'maze_size'] =  observable_lib.Generic(lambda _: self._maze_arena.maze_size)
      self._task_observables[f'maze_size'].enabled = True
      for wk in self._walkers.keys():
          name = self._walkers[wk]._mjcf_root.model
          self._task_observables[f'location_in_maze_{name}'] = absolute_position_discrete[wk]
          self._task_observables[f'absolute_position_{name}'] = absolute_position[wk]
          self._task_observables[f'absolute_orientation_{name}'] = absolute_orientation[wk]
          self._task_observables[f'absolute_quaternion_{name}'] = absolute_quaternion[wk]
    else:
      self._task_observables = collections.OrderedDict({})

    self.root_entity.mjcf_model.size.nconmax = nconmax * self._nw
    self.root_entity.mjcf_model.size.njmax = njmax * self._nw
    self.init_rotations = {}
  @property
  def task_observables(self):
    return self._task_observables

  @property
  def name(self):
    return 'goal_maze'

  @property
  def root_entity(self):
    return self._maze_arena

  def initialize_episode_mjcf(self, unused_random_state):
    # self._maze_arena.regenerate(random_seed=1)
    self._maze_arena.regenerate(random_seed=self._random_seed)
    # self._maze_arena.regenerate()


  def _respawn(self, physics, random_state):
    for wk in self._walkers.keys():
        self._walkers[wk].reinitialize_pose(physics, random_state)
        name = self._walkers[wk]._mjcf_root.model
        if self._randomize_spawn_position and wk == self._primary_agent:
          self._spawn_position = self._maze_arena.spawn_positions[wk][
              random_state.randint(0, len(self._maze_arena.spawn_positions[wk]))]
        else:
          self._spawn_position = self._maze_arena.spawn_positions[wk][0] # Just use the first position

        if self._randomize_spawn_rotation or (self._spawn_rotation_radians is not None and not wk in self._spawn_rotation_radians):
          do_bias_away_from_wall = False
          if do_bias_away_from_wall:
            # Move walker up out of the way before raycasting.
            self._walkers[wk].shift_pose(physics, [0.0, 0.0, 100.0])

            distances = []
            geomid_out = np.array([-1], dtype=np.intc)
            for i in range(_NUM_RAYS):
              theta = 2 * np.pi * i / _NUM_RAYS
              pos = np.array([self._spawn_position[0], self._spawn_position[1], 0.1],
                             dtype=np.float64)
              vec = np.array([np.cos(theta), np.sin(theta), 0], dtype=np.float64)
              dist = mjbindings.mjlib.mj_ray(
                  physics.model.ptr, physics.data.ptr, pos, vec,
                  None, 1, -1, geomid_out)
              distances.append(dist)

            def remap_with_bias(x):
              """Remaps values [-1, 1] -> [-1, 1] with bias."""
              return np.tanh((1 + self._rotation_bias_factor) * np.arctanh(x))

            max_theta = 2 * np.pi * np.argmax(distances) / _NUM_RAYS
            rotation = max_theta + np.pi * (
                1 + remap_with_bias(random_state.uniform(-1, 1)))

            print(rotation)
            quat = [np.cos(rotation / 2), 0, 0, np.sin(rotation / 2)]
            print(quat)
            # Move walker back down.
            self._walkers[wk].shift_pose(physics, [0.0, 0.0, -100.0])
          else:
            rotation = 2*np.pi*random_state.uniform(0, 1)
            # print(f'Rotation: {rotation}')
            quat = [np.cos(rotation / 2), 0, 0, np.sin(rotation / 2)]
        else:
          if self._spawn_rotation_radians is None:
            quat = None
          else:
              assert isinstance(self._spawn_rotation_radians, dict)
              if wk in self._spawn_rotation_radians:
                # rotation=3*np.pi/2 #np.pi/4
                quat = [np.cos(self._spawn_rotation_radians[wk] / 2), 0, 0,
                        np.sin(self._spawn_rotation_radians[wk] / 2)]
              else:
                quat = None

        physics.bind(self._walkers[wk]._mjcf_root.find_all('joint')).qpos = 0.
        self._walkers[wk].shift_pose(
            physics, [self._spawn_position[0], self._spawn_position[1], self._z_spawn],
            quat,
            rotate_velocity=True)

  def initialize_episode(self, physics, random_state):
    super().initialize_episode(physics, random_state)
    self._respawn(physics, random_state)
    self._discount = 1.0

    self._walker_nonfoot_geomids = {}
    for wk in self._walkers.keys():
        walker_foot_geoms = set(self._walkers[wk].ground_contact_geoms)
        walker_nonfoot_geoms = [
            geom for geom in self._walkers[wk].mjcf_model.find_all('geom')
            if geom not in walker_foot_geoms]
        self._walker_nonfoot_geomids[wk] = set(
            physics.bind(walker_nonfoot_geoms).element_id)
    self._ground_geomids = set(
        physics.bind(self._maze_arena.ground_geoms).element_id)

  def _is_disallowed_contact(self, contact, walker_id=0):
    set1, set2 = self._walker_nonfoot_geomids[walker_id], self._ground_geomids
    return ((contact.geom1 in set1 and contact.geom2 in set2) or
            (contact.geom1 in set2 and contact.geom2 in set1))

  def after_step(self, physics, random_state):
    self._failure_termination = False
    if self._contact_termination:
      for c in physics.data.contact:
        if self._is_disallowed_contact(c):
          self._failure_termination = True
          break

  def should_terminate_episode(self, physics):
    for wk in self._walkers.keys():
        if self._walkers[wk].aliveness(physics) < self._aliveness_thresh:
          self._failure_termination = True
    if self._failure_termination:
      self._discount = 0.0
      return True
    else:
      return False

  def get_reward(self, physics):
    del physics
    return self._aliveness_reward

  def get_discount(self, physics):
    del physics
    return self._discount


class VelocityMaze(NullGoalMaze):
    """Requires an agent to move at a target velocity."""

    def __init__(self,
                 walkers,
                 maze_arena,
                 primary_agent,
                 target=None,
                 target_reward_scale=1.0,
                 randomize_spawn_position=True,
                 randomize_spawn_rotation=True,
                 rotation_bias_factor=0,
                 aliveness_reward=0.0,
                 aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
                 contact_termination=True,
                 max_repeats=0,
                 enable_global_task_observables=False,
                 physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
                 control_timestep=DEFAULT_CONTROL_TIMESTEP,
                 regenerate_maze_on_repeat=False,
                 nconmax=100,
                 njmax=100,
                 z_spawn=0.5,
                 target_velocity=3.0,
                 ):
        super().__init__(
            walkers=walkers,
            maze_arena=maze_arena,
            primary_agent=primary_agent,
            randomize_spawn_position=randomize_spawn_position,
            randomize_spawn_rotation=randomize_spawn_rotation,
            rotation_bias_factor=rotation_bias_factor,
            aliveness_reward=aliveness_reward,
            aliveness_thresh=aliveness_thresh,
            contact_termination=contact_termination,
            enable_global_task_observables=enable_global_task_observables,
            physics_timestep=physics_timestep,
            control_timestep=control_timestep,
            nconmax=nconmax,
            njmax=njmax,
            z_spawn=z_spawn,
        )
        self._walkers = walkers
        self._primary_agent = primary_agent
        self._primary_agent_name = walkers[self._primary_agent]._mjcf_root.model
        self._vel = target_velocity
        self._aliveness_reward = aliveness_reward

    def get_reward(self, physics):
        walker = self._walkers[self._primary_agent]
        walker_xvel = physics.bind(walker.root_body).subtree_linvel[0]
        xvel_term = rewards.tolerance(
            walker_xvel, (self._vel, self._vel),
            margin=self._vel,
            sigmoid='linear',
            value_at_margin=0.0)
        return xvel_term + self._aliveness_reward

    def should_terminate_episode(self, physics):
        if super().should_terminate_episode(physics):
            return True

    def get_discount(self, physics):
        if self._failure_termination:
            return 0.
        else:
            return 1.

class LocationMaze(NullGoalMaze):
    """Requires an agent to move at a target velocity."""

    def __init__(self,
                 walkers,
                 maze_arena,
                 primary_agent,
                 target=None,
                 target_reward_scale=1.0,
                 randomize_spawn_position=True,
                 randomize_spawn_rotation=True,
                 rotation_bias_factor=0,
                 aliveness_reward=0.0,
                 aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
                 contact_termination=True,
                 max_repeats=0,
                 enable_global_task_observables=False,
                 physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
                 control_timestep=DEFAULT_CONTROL_TIMESTEP,
                 regenerate_maze_on_repeat=False,
                 nconmax=100,
                 njmax=100,
                 z_spawn=0.5,
                 target_xloc=9.0, # midway between the spheres
                 target_yloc=0.0,
                 ):
        super().__init__(
            walkers=walkers,
            maze_arena=maze_arena,
            primary_agent=primary_agent,
            randomize_spawn_position=randomize_spawn_position,
            randomize_spawn_rotation=randomize_spawn_rotation,
            rotation_bias_factor=rotation_bias_factor,
            aliveness_reward=aliveness_reward,
            aliveness_thresh=aliveness_thresh,
            contact_termination=contact_termination,
            enable_global_task_observables=enable_global_task_observables,
            physics_timestep=physics_timestep,
            control_timestep=control_timestep,
            nconmax=nconmax,
            njmax=njmax,
            z_spawn=z_spawn,
        )
        self._walkers = walkers
        self._primary_agent = primary_agent
        self._primary_agent_name = walkers[self._primary_agent]._mjcf_root.model
        self._xloc = target_xloc
        self._yloc = target_yloc
        self._aliveness_reward = aliveness_reward

    def get_reward(self, physics):
        walker = self._walkers[self._primary_agent]
        walker_xloc = physics.bind(walker.root_body).xpos[0]
        walker_yloc = physics.bind(walker.root_body).xpos[1]
        xloc_term = rewards.tolerance(
            walker_xloc, (self._xloc, self._xloc),
            margin=self._maze_arena.maze.width*self._maze_arena.xy_scale,
            sigmoid='hyperbolic',
            value_at_margin=0.01)
        yloc_term = rewards.tolerance(
            walker_yloc, (self._yloc, self._yloc),
            margin=self._maze_arena.maze.height*self._maze_arena.xy_scale,
            sigmoid='hyperbolic',
            value_at_margin=0.01)
        return 0.5*(xloc_term + yloc_term) + self._aliveness_reward

    def should_terminate_episode(self, physics):
        if super().should_terminate_episode(physics):
            return True

    def get_discount(self, physics):
        if self._failure_termination:
            return 0.
        else:
            return 1.


class RepeatSingleGoalMaze(NullGoalMaze):
  """Requires an agent to repeatedly find the same goal in a maze."""
  def __init__(self,
               walkers,
               maze_arena,
               primary_agent,
               target=None,
               target_reward_scale=1.0,
               randomize_spawn_position=True,
               randomize_spawn_rotation=True,
               spawn_rotation_radians=None,
               rotation_bias_factor=0,
               aliveness_reward=0.0,
               aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
               contact_termination=True,
               max_repeats=0,
               enable_global_task_observables=False,
               physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
               control_timestep=DEFAULT_CONTROL_TIMESTEP,
               regenerate_maze_on_repeat=False,
               nconmax=100,
               njmax=100,
               z_spawn=0.5,
               dense_reward_scaling=0,
               reward_args=None,
               continuous_aliveness=False, # Specific aliveness value, as opposed binary alive/dead
               accel_cost_scale=0.0,
               vel_cost_scale=0.0,
               random_seed=None,
               ):
    super().__init__(
        walkers=walkers,
        maze_arena=maze_arena,
        primary_agent=primary_agent,
        randomize_spawn_position=randomize_spawn_position,
        randomize_spawn_rotation=randomize_spawn_rotation,
        spawn_rotation_radians=spawn_rotation_radians,
        rotation_bias_factor=rotation_bias_factor,
        aliveness_reward=aliveness_reward,
        aliveness_thresh=aliveness_thresh,
        contact_termination=contact_termination,
        enable_global_task_observables=enable_global_task_observables,
        physics_timestep=physics_timestep,
        control_timestep=control_timestep,
        nconmax=nconmax,
        njmax=njmax,
        z_spawn=z_spawn,
        random_seed=random_seed)
    if target is None:
      target = target_sphere.TargetSphere(
            radius=0.5,
            height_above_ground=2.0)
    self._target = target
    self._rewarded_this_step = False
    self._maze_arena.attach(target)
    self._target_reward_scale = target_reward_scale
    self._max_repeats = max_repeats
    self._targets_obtained = 0
    self._regenerate_maze_on_repeat = regenerate_maze_on_repeat
    self._dense_reward_scaling = dense_reward_scaling
    self._reward_args = reward_args
    self._continuous_aliveness = continuous_aliveness
    self._accel_cost_scale = accel_cost_scale
    self._vel_cost_scale = vel_cost_scale

    self._primary_agent = primary_agent
    self._primary_agent_name = walkers[self._primary_agent]._mjcf_root.model

    self._stepnum = 0

    if enable_global_task_observables:
        # xpos = dict()
        # for wk in self._walkers.keys():
        #     xpos[wk] = lambda phys, k: phys.bind(self._walkers[k].root_body).xpos

        xpos = lambda phys, k: phys.bind(self._walkers[k].root_body).xpos

        def _target_pos(physics, target=target):
            return physics.bind(target.geom).xpos

        world_frame_observable = observable_lib.Generic(_target_pos)
        for wk in self._walkers.keys():
            self._walkers[wk].observables.add_egocentric_vector(
                f'target_0',
                world_frame_observable,
                origin_callable=functools.partial(xpos, k=wk))

        for wk in self._walkers.keys():
            def _allocentric(physics, wk, origin_callable, world_frame_observable):
                vec = world_frame_observable.observation_callable(physics)()
                origin_callable = functools.partial(origin_callable, k=wk) or (lambda physics: np.zeros(vec.size))
                delta = vec - origin_callable(physics)
                # print(wk, vec, '\t', round(origin_callable(physics)), '\t', round(delta))
                return delta

            allo = observable_lib.Generic(functools.partial(_allocentric, wk=wk, origin_callable=xpos,
                                                            world_frame_observable=world_frame_observable))
            self._walkers[wk].observables._observables['target_allo_0'] = allo
            self._walkers[wk].observables._observables['target_allo_0'].enabled = True

  def initialize_episode_mjcf(self, random_state):
    super().initialize_episode_mjcf(random_state)
    self._target_position = self._maze_arena.target_positions[
        random_state.randint(0, len(self._maze_arena.target_positions))]
    mjcf.get_attachment_frame(
        self._target.mjcf_model).pos = self._target_position

  def initialize_episode(self, physics, random_state):
    super().initialize_episode(physics, random_state)
    self._rewarded_this_step = False
    self._targets_obtained = 0

  def after_step(self, physics, random_state):
    super().after_step(physics, random_state)
    # pn = self._primary_agent_name
    # print(physics.bind(self._target.geom).xpos, '\t', round(physics.bind(self._walkers['0'].root_body).xpos), '\t', round(self.observables['agent0/target_allo_0'](physics)), '\t', round(self.observables['agent0/target_0'](physics)), '\t', round(self.observables['ball2/target_allo_0'](physics)), '\t', round(self.observables['ball2/target_0'](physics)))
    # print(np.linalg.norm(np.array(self.observables['agent0/target_allo_0'](physics))), '\t', np.linalg.norm(np.array(self.observables['agent0/target_0'](physics))))

    ### TRYING TO CHANGE TEXTURE ON STEP
    # self._maze_arena.regenerate()
    # self._respawn(physics, random_state)
    # self._target.reset(physics)
    """
    self._stepnum += 1
    ma = self._maze_arena
    wb = ma._mjcf_root.worldbody

    for geom_name in ma._texturing_geom_names:
      del ma._mjcf_root.worldbody.geom[geom_name]
    ma._texturing_geom_names = []

    ma._maze_body.geom.clear()

    xyaxes = {
        'x': {-1: [0, -1, 0, 0, 0, 1], 1: [0, 1, 0, 0, 0, 1]},
        'y': {-1: [1, 0, 0, 0, 0, 1], 1: [-1, 0, 0, 0, 0, 1]},
        'z': {-1: [-1, 0, 0, 0, 1, 0], 1: [1, 0, 0, 0, 1, 0]}
    }
    # wall_pos = np.array([(1 - ma._x_offset) * ma._xy_scale,
    #                      -(2 - ma._y_offset) * ma._xy_scale,
    #                      ma._z_height / 2])
    wall_pos = np.array([-14.7,  -0.7,   4.2])
    wall_size = np.array([0.7, 14., 20])
    print(len(wb.geom))
    # wall_size = np.array([16, 16, 16])
    for direction_index, direction in enumerate(('x', 'y', 'z')):
      index = list(i for i in range(3) if i != direction_index)
      delta_vector = np.array([int(i == direction_index) for i in range(3)])
      # material_name = 'wall{}_{}_{}'.format(wall_char, wall_id, direction)
      material_name = f'test_wall_ikfr_material_{self._stepnum}_{direction}'
      ma._texturing_material_names.append(material_name)
      mat = ma._mjcf_root.asset.add(
        'material', name=material_name,
        # texture=ma._current_wall_texture[wall_char],
        texture=np.random.choice(list(ma._current_wall_texture.values())),
        texrepeat=(2 * wall_size[index] / ma._xy_scale))

      for sign, sign_name in zip((-1, 1), ('neg', 'pos')):
        if direction == 'z' and sign == -1:
          continue
        geom_name = (f'test_wall_ikfr_{self._stepnum}_{sign_name}_{sign}_{direction}')
        ma._texturing_geom_names.append(geom_name)
        ma._mjcf_root.worldbody.add(
          'geom', type='plane', name=geom_name,
          # pos=(wall_pos + sign * delta_vector * wall_size),
          pos=(wall_pos + sign * delta_vector * wall_size),
          size=np.concatenate([wall_size[index], [ma._xy_scale]]),
          xyaxes=xyaxes[direction][sign], material=mat,
          contype=0, conaffinity=0)

    """
    #### END CHANGE TEXTURE
    if self._target.activated:
      self._rewarded_this_step = True
      self._targets_obtained += 1
      if self._targets_obtained <= self._max_repeats:
        if self._regenerate_maze_on_repeat:
          self.initialize_episode_mjcf(random_state)
          self._target.set_pose(physics, self._target_position)
        self._respawn(physics, random_state)
        self._target.reset(physics)
    else:
      self._rewarded_this_step = False

  def should_terminate_episode(self, physics):
    if super().should_terminate_episode(physics):
      return True
    if self._targets_obtained > self._max_repeats:
      return True

  def get_reward(self, physics):
    # del physics

    # Get reward for colliding with target.
    if self._rewarded_this_step:
      target_reward = self._target_reward_scale
    else:
      target_reward = 0.0

    if not self._dense_reward_scaling == 0:
        # target_reward += -self._dense_reward_scaling *np.linalg.norm(np.array(self.observables['agent1/target_0'](physics)))
        # target_reward += -self._dense_reward_scaling * np.linalg.norm(
        #     np.array(self.observables[self._primary_agent_name+'/target_0'](physics)))
        # print(physics.bind(self._target.geom).xpos)
        # print(physics.bind(self._walkers[self._primary_agent].root_body).xpos)

        if self._reward_args is None or self._reward_args['goal'] == 'position':
            ## Should you make this a squared distance?
            walker = self._walkers[self._primary_agent]
            walker_xloc = physics.bind(walker.root_body).xpos[0]
            walker_yloc = physics.bind(walker.root_body).xpos[1]
            target_xloc = physics.bind(self._target.geom).xpos[0]
            target_yloc = physics.bind(self._target.geom).xpos[1]
            # xloc_term = rewards.tolerance(
            #     walker_xloc, (target_xloc, target_xloc),
            #     margin=self._maze_arena.maze.width*self._maze_arena.xy_scale,
            #     sigmoid='hyperbolic',
            #     value_at_margin=0.01)
            # yloc_term = rewards.tolerance(
            #     walker_yloc, (target_yloc, target_yloc),
            #     margin=self._maze_arena.maze.height*self._maze_arena.xy_scale,
            #     sigmoid='hyperbolic',
            #     value_at_margin=0.01)
            # target_reward += self._dense_reward_scaling*0.5*(xloc_term + yloc_term)

            walker_dist = np.sqrt((walker_xloc-target_xloc)**2 + (walker_yloc-target_yloc)**2 + 0.01)
            maze_diag = np.sqrt(self._maze_arena.maze.width**2 + self._maze_arena.maze.height**2 + 0.01)
            dist_term = rewards.tolerance(
                walker_dist, (0, 0),
                margin=maze_diag*self._maze_arena.xy_scale,
                # sigmoid='hyperbolic',
              sigmoid='linear',
              value_at_margin=0.01)
            target_reward += self._dense_reward_scaling*dist_term

            # Add reward for being very close to target.
            xy_scale =self._maze_arena.xy_scale
            goal_term = rewards.tolerance(
                # walker_dist, (-xy_scale/2, xy_scale/2),
              walker_dist, (-xy_scale, xy_scale), # Enlarging the size of the target to make things a little easier.
              margin=0,
                # sigmoid='hyperbolic',
              sigmoid='linear',
              value_at_margin=0.00)
            target_reward += self._target_reward_scale*goal_term


        elif self._reward_args['goal'] == 'velocity':
            walker = self._walkers[self._primary_agent]
            walker_xvel = physics.bind(walker.root_body).subtree_linvel[0]
            walker_yvel = physics.bind(walker.root_body).subtree_linvel[1]
            if 'xvel' in self._reward_args.keys():
                xvel = self._reward_args['xvel']
                xvel_term = rewards.tolerance(
                    walker_xvel, (xvel, xvel),
                    margin=np.abs(xvel),
                    sigmoid='linear',
                    value_at_margin=0.0)
                target_reward += xvel_term
            if 'yvel' in self._reward_args.keys():
                yvel = self._reward_args['yvel']
                yvel_term = rewards.tolerance(
                    walker_yvel, (yvel, yvel),
                    margin=np.abs(yvel),
                    sigmoid='linear',
                    value_at_margin=0.0)
                target_reward += yvel_term
    reward = target_reward

    if self._continuous_aliveness:
      walker = self._walkers[self._primary_agent]
      aliveness = (walker.aliveness(physics)+1)   # Make it a positive number
      aliveness *= self._aliveness_reward
    else:
      aliveness = self._aliveness_reward
    reward += aliveness

    # Add in max accel loss function, with a big negative reward approaching accel=1e3, try to keep it below 1e2
    do_max_accel = self._accel_cost_scale > 0
    if do_max_accel:
      max_accel = 5.5e2
      margin = 5e2
      walker = self._walkers[self._primary_agent]
      accel = (walker.accel(physics))
      a = np.max(np.abs(accel))
      cost = rewards.tolerance(a, (0, max_accel-margin), margin=margin, sigmoid='gaussian')
      cost = self._accel_cost_scale*(cost-1)
      reward += cost

    do_max_vel = self._vel_cost_scale > 0
    if do_max_vel:
      max_vel = 150
      margin = 50
      walker = self._walkers[self._primary_agent]
      vel = (walker.ang_vel(physics))
      v = np.max(np.abs(vel))
      cost = rewards.tolerance(v, (0, max_vel - margin), margin=margin, sigmoid='gaussian')
      cost = self._vel_cost_scale * (cost - 1)
      reward += cost
      raise('Max vel not yet implemented.')


    return reward


class ManyHeterogeneousGoalsMaze(NullGoalMaze):
  """Requires an agent to find multiple goals with different rewards."""

  def __init__(self,
               walkers,
               maze_arena,
               primary_agent,
               target_builders,
               target_type_rewards,
               target_type_proportions,
               shuffle_target_builders=False,
               randomize_spawn_position=True,
               randomize_spawn_rotation=True,
               rotation_bias_factor=0,
               aliveness_reward=0.0,
               aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
               contact_termination=True,
               physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
               control_timestep=DEFAULT_CONTROL_TIMESTEP,
               nconmax=100,
               njmax=100,
               z_spawn=0.5,
               enable_global_task_observables=False,
               ):
    super().__init__(
        walkers=walkers,
        maze_arena=maze_arena,
        primary_agent=primary_agent,
        randomize_spawn_position=randomize_spawn_position,
        randomize_spawn_rotation=randomize_spawn_rotation,
        rotation_bias_factor=rotation_bias_factor,
        aliveness_reward=aliveness_reward,
        aliveness_thresh=aliveness_thresh,
        contact_termination=contact_termination,
        physics_timestep=physics_timestep,
        control_timestep=control_timestep,
        nconmax=nconmax,
        njmax=njmax,
        z_spawn=z_spawn,
        enable_global_task_observables=enable_global_task_observables)
    self._active_targets = []
    self._target_builders = target_builders
    self._target_type_rewards = tuple(target_type_rewards)
    self._target_type_fractions = (
        np.array(target_type_proportions, dtype=float) /
        np.sum(target_type_proportions))
    self._shuffle_target_builders = shuffle_target_builders

  def _get_targets(self, total_target_count, random_state):
    # Multiply total target count by the fraction for each type, rounded down.
    target_numbers = np.array([int(frac * total_target_count)
                               for frac in self._target_type_fractions])

    # Calculate deviations from the ideal ratio incurred by rounding.
    errors = (self._target_type_fractions -
              target_numbers / float(total_target_count))

    # Sort the target types by deviations from ideal ratios.
    target_types_sorted_by_errors = list(np.argsort(errors))

    # Top up individual target classes until we reach the desired total,
    # starting from the class that is furthest away from the ideal ratio.
    current_total = np.sum(target_numbers)
    while current_total < total_target_count:
      target_numbers[target_types_sorted_by_errors.pop()] += 1
      current_total += 1

    if self._shuffle_target_builders:
      random_state.shuffle(self._target_builders)

    all_targets = []
    for target_type, num in enumerate(target_numbers):
      targets = []
      target_builder = self._target_builders[target_type]
      for i in range(num):
        target = target_builder(name='target_{}_{}'.format(target_type, i))
        targets.append(target)
      all_targets.append(targets)
    return all_targets

  def initialize_episode_mjcf(self, random_state):
    super(
        ManyHeterogeneousGoalsMaze, self).initialize_episode_mjcf(random_state)
    for target in itertools.chain(*self._active_targets):
      target.detach()
    target_positions = list(self._maze_arena.target_positions)
    random_state.shuffle(target_positions)
    all_targets = self._get_targets(len(target_positions), random_state)
    for pos, target in zip(target_positions, itertools.chain(*all_targets)):
      self._maze_arena.attach(target)
      mjcf.get_attachment_frame(target.mjcf_model).pos = pos
      target.initialize_episode_mjcf(random_state)
    self._active_targets = all_targets
    self._target_rewarded = [[False] * len(targets) for targets in all_targets]

  def get_reward(self, physics):
    del physics
    reward = self._aliveness_reward
    for target_type, targets in enumerate(self._active_targets):
      for i, target in enumerate(targets):
        if target.activated and not self._target_rewarded[target_type][i]:
          reward += self._target_type_rewards[target_type]
          self._target_rewarded[target_type][i] = True
    return reward

  def should_terminate_episode(self, physics):
    if super(ManyHeterogeneousGoalsMaze,
             self).should_terminate_episode(physics):
      return True
    else:
      for target in itertools.chain(*self._active_targets):
        if not target.activated:
          return False
      # All targets have been activated: successful termination.
      return True


class ManyGoalsMaze(ManyHeterogeneousGoalsMaze):
  """Requires an agent to find all goals in a random maze."""

  def __init__(self,
               walkers,
               maze_arena,
               primary_agent,
               target_builder,
               target_reward_scale=1.0,
               randomize_spawn_position=True,
               randomize_spawn_rotation=True,
               rotation_bias_factor=0,
               aliveness_reward=0.0,
               aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
               contact_termination=True,
               physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
               control_timestep=DEFAULT_CONTROL_TIMESTEP,
               nconmax=100,
               njmax=100,
               z_spawn=0.5,
               enable_global_task_observables=False,
               ):
    super().__init__(
        walkers=walkers,
        maze_arena=maze_arena,
        primary_agent=primary_agent,
        target_builders=[target_builder],
        target_type_rewards=[target_reward_scale],
        target_type_proportions=[1],
        randomize_spawn_position=randomize_spawn_position,
        randomize_spawn_rotation=randomize_spawn_rotation,
        rotation_bias_factor=rotation_bias_factor,
        aliveness_reward=aliveness_reward,
        aliveness_thresh=aliveness_thresh,
        contact_termination=contact_termination,
        physics_timestep=physics_timestep,
        control_timestep=control_timestep,
        nconmax=nconmax,
        njmax=njmax,
        z_spawn=z_spawn,
        enable_global_task_observables=enable_global_task_observables,
    )


class RepeatSingleGoalMazeAugmentedWithTargets(RepeatSingleGoalMaze):
  """Augments the single goal maze with many lower reward targets."""

  def __init__(self,
               walkers,
               main_target,
               maze_arena,
               primary_agent,
               num_subtargets=20,
               target_reward_scale=10.0,
               subtarget_reward_scale=1.0,
               subtarget_colors=((0, 0, 0.4), (0, 0, 0.7)),
               randomize_spawn_position=True,
               randomize_spawn_rotation=True,
               rotation_bias_factor=0,
               aliveness_reward=0.0,
               aliveness_thresh=DEFAULT_ALIVE_THRESHOLD,
               contact_termination=True,
               physics_timestep=DEFAULT_PHYSICS_TIMESTEP,
               control_timestep=DEFAULT_CONTROL_TIMESTEP,
               z_spawn=0.5,
               enable_global_task_observables=False,
               ):
    super().__init__(
        walkers=walkers,
        target=main_target,
        maze_arena=maze_arena,
        primary_agent=primary_agent,
        target_reward_scale=target_reward_scale,
        randomize_spawn_position=randomize_spawn_position,
        randomize_spawn_rotation=randomize_spawn_rotation,
        rotation_bias_factor=rotation_bias_factor,
        aliveness_reward=aliveness_reward,
        aliveness_thresh=aliveness_thresh,
        contact_termination=contact_termination,
        physics_timestep=physics_timestep,
        control_timestep=control_timestep,
        z_spawn=0.5,
        enable_global_task_observables=enable_global_task_observables,
    )
    self._subtarget_reward_scale = subtarget_reward_scale
    self._subtargets = []
    for i in range(num_subtargets):
      subtarget = target_sphere.TargetSphere(
          radius=0.4, rgb1=subtarget_colors[0], rgb2=subtarget_colors[1],
          name='subtarget_{}'.format(i)
      )
      self._subtargets.append(subtarget)
      self._maze_arena.attach(subtarget)
    self._subtarget_rewarded = None

  def initialize_episode_mjcf(self, random_state):
    super(RepeatSingleGoalMazeAugmentedWithTargets,
          self).initialize_episode_mjcf(random_state)
    subtarget_positions = self._maze_arena.target_positions
    for pos, subtarget in zip(subtarget_positions, self._subtargets):
      mjcf.get_attachment_frame(subtarget.mjcf_model).pos = pos
    self._subtarget_rewarded = [False] * len(self._subtargets)

  def get_reward(self, physics):
    main_reward = super(RepeatSingleGoalMazeAugmentedWithTargets,
                        self).get_reward(physics)
    subtarget_reward = 0
    for i, subtarget in enumerate(self._subtargets):
      if subtarget.activated and not self._subtarget_rewarded[i]:
        subtarget_reward += 1
        self._subtarget_rewarded[i] = True
    subtarget_reward *= self._subtarget_reward_scale
    return main_reward + subtarget_reward

  def should_terminate_episode(self, physics):
    if super(RepeatSingleGoalMazeAugmentedWithTargets,
             self).should_terminate_episode(physics):
      return True
    else:
      for subtarget in self._subtargets:
        if not subtarget.activated:
          return False
      # All subtargets have been activated.
      return True
