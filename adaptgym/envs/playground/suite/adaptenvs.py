import functools
import numpy as np
import matplotlib.pyplot as plt



from dm_control.locomotion import arenas
from dm_control.composer.variation import distributions
from dm_control.composer.variation import noises
from dm_control.locomotion.arenas import floors

from dm_control.utils import containers
from dm_control import composer

# Run through corridor example
from dm_control.locomotion.walkers import cmu_humanoid, ant, jumping_ball
from dm_control.locomotion.tasks import corridors as corr_tasks
from dm_control.locomotion.arenas import corridors as corr_arenas
from dm_control.locomotion.walkers import rodent

from dm_control.locomotion.examples import basic_rodent_2020 as basic_rodent
from dm_control.locomotion.arenas import labmaze_textures
from dm_control.locomotion.arenas import mazes
from dm_control.locomotion.tasks import random_goal_maze
from dm_control.locomotion.props import target_sphere

_CONTROL_TIMESTEP = .02
_PHYSICS_TIMESTEP = 0.001

SUITE = containers.TaggedTasks()

def rodent_maze(random_state=None):
    walker = rodent.Rat(
        observable_options={'egocentric_camera': dict(enabled=True)})

    skybox_texture = labmaze_textures.SkyBox(style='sky_03')
    wall_textures = labmaze_textures.WallTextures(style='style_01')
    floor_textures = labmaze_textures.FloorTextures(style='style_01')

    arena = mazes.RandomMazeWithTargets(
        x_cells=11,
        y_cells=11,
        xy_scale=0.5,
        max_rooms=4,
        z_height=0.3,
        room_min_size=4,
        room_max_size=5,
        spawns_per_room=1,
        targets_per_room=3,
        wall_textures=wall_textures,
        aesthetic='outdoor_natural')

    task = random_goal_maze.ManyGoalsMaze(
        walker=walker,
        maze_arena=arena,
        target_builder=functools.partial(
            target_sphere.TargetSphere,
            radius=0.05,
            height_above_ground=0.125,
            rgb1=(0, 0, 0.4),
            rgb2=(0, 0, 0.7)),
        control_timestep=.03,
        physics_timestep=.005,
    )
    random_state = np.random.RandomState(12345)

    return composer.Environment(time_limit=30,
                                task=task,
                                random_state=random_state,
                                strip_singleton_obs_buffer_dim=True)



def run_gaps(random_state=None):
  """Requires a rodent to run down a corridor with gaps."""

  # Build a position-controlled rodent walker.
  walker = rodent.Rat(
      observable_options={'egocentric_camera': dict(enabled=True)})
  walker = cmu_humanoid.CMUHumanoidPositionControlledV2020(
      observable_options={'egocentric_camera': dict(enabled=True)})
  walker = ant.Ant(
      observable_options={'egocentric_camera': dict(enabled=True)})
  # walker = jumping_ball.JumpingBallWithHead(
  #     observable_options={'egocentric_camera': dict(enabled=True)})

  # Build a corridor-shaped arena with gaps, where the sizes of the gaps and
  # platforms are uniformly randomized.
  arena = corr_arenas.GapsCorridor(
      # platform_length=distributions.Uniform(.4, .8),
      # gap_length=distributions.Uniform(.05, .2),
      platform_length=distributions.Uniform(1, 2),
      gap_length=distributions.Uniform(1, 2),
      corridor_width=2,
      corridor_length=40,
      aesthetic='outdoor_natural')

  # Build a task that rewards the agent for running down the corridor at a
  # specific velocity.
  task = corr_tasks.RunThroughCorridor(
      walker=walker,
      arena=arena,
      walker_spawn_position=(5, 0, 0),
      walker_spawn_rotation=0,
      target_velocity=1.0,
      contact_termination=False,
      terminate_at_height=-0.3,
      physics_timestep=_PHYSICS_TIMESTEP,
      control_timestep=_CONTROL_TIMESTEP)

  return composer.Environment(time_limit=30,
                              task=task,
                              random_state=random_state,
                              strip_singleton_obs_buffer_dim=True)

def humanoid_walls():
    walker = cmu_humanoid.CMUHumanoidPositionControlledV2020(
        observable_options={'egocentric_camera': dict(enabled=True)})
    arena = corr_arenas.WallsCorridor(
        wall_gap=3.,
        wall_width=distributions.Uniform(2., 3.),
        wall_height=distributions.Uniform(2.5, 3.5),
        corridor_width=4.,
        corridor_length=30.,
    )
    task = corr_tasks.RunThroughCorridor(
        walker=walker,
        arena=arena,
        walker_spawn_position=(0.5, 0, 0),
        target_velocity=3.0,
        physics_timestep=0.005,
        control_timestep=0.03,
    )
    env = composer.Environment(
        task=task,
        time_limit=10,
        random_state=np.random.RandomState(42),
        strip_singleton_obs_buffer_dim=True,
    )
    env.reset()
    pixels = []
    for camera_id in range(3):
        pixels.append(env.physics.render(camera_id=camera_id, width=240))
    # PIL.Image.fromarray(np.hstack(pixels))
    # plt.imshow(np.hstack(pixels))

    return env

@SUITE.add('benchmarking')
def humanoid_corridor():
    walker = cmu_humanoid.CMUHumanoidPositionControlledV2020(
        observable_options={'egocentric_camera': dict(enabled=True)})
    arena = corr_arenas.EmptyCorridor(
        corridor_width=4,
        corridor_length=40,
        visible_side_planes=False,
    )
    task = corr_tasks.RunThroughCorridor(
        walker=walker,
        arena=arena,
        walker_spawn_position=(0.5, 0, 0),
        target_velocity=3.0,
        physics_timestep=0.005,
        control_timestep=0.03,
    )
    env = composer.Environment(
        task=task,
        time_limit=10,
        random_state=np.random.RandomState(42),
        strip_singleton_obs_buffer_dim=True,
    )
    env.reset()
    pixels = []
    for camera_id in range(3):
        pixels.append(env.physics.render(camera_id=camera_id, width=240))
    plt.imshow(np.hstack(pixels))
    plt.show()

    return env

@SUITE.add('benchmarking')
def ant_corridor(do_gaps=False):
    walker = ant.Ant(
        observable_options={'egocentric_camera': dict(enabled=True)})

    if do_gaps:
        arena = corr_arenas.GapsCorridor(
            platform_length=distributions.Uniform(1, 2),
            gap_length=distributions.Uniform(1, 2),
            corridor_width=4,
            corridor_length=40)
    else:
        arena = corr_arenas.EmptyCorridor(
            corridor_width=4,
            corridor_length=40,
            visible_side_planes=False,
        )

    task = corr_tasks.RunThroughCorridor(
        walker=walker,
        arena=arena,
        walker_spawn_position=(0.5, 0, 0),
        target_velocity=3.0,
        physics_timestep=0.005,
        control_timestep=0.03,
    )
    env = composer.Environment(
        task=task,
        time_limit=10,
        random_state=np.random.RandomState(42),
        strip_singleton_obs_buffer_dim=True,
    )
    env.reset()
    pixels = []
    for camera_id in range(3):
        pixels.append(env.physics.render(camera_id=camera_id, width=240))
    plt.imshow(np.hstack(pixels))
    plt.show()

    return env