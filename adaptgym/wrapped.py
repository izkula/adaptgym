"""Wrapped version of environments, that includes rendering of image observation.
This is the format accepted by dreamerv2.
"""

import os
import gym
import numpy as np

import dm_env
from dm_env import specs
import adaptgym.envs.playground.policies as pol


class ADMC:

  def __init__(self, name, action_repeat=2, size=(64, 64), camera=None,
               aesthetic='default', # 'outdoor_natural'
               egocentric_camera=True, multiple_agents=False,
               env_params=None, logging_params=None,
               control_timestep=0.03, physics_timestep=0.005,
               reset_position_freq=0, use_global_step=True,
               logdir=None, mode='train',
               record_every_k_timesteps=20,
               flush_logger_every=2000,
               grid_density=20,
               episodes_for_summary_metrics=20,
               spoof_done_every=500,
               wide_fov=False,
               ):

    if logdir is None:
      print('No logdir provided, not logging playground trajectories.')
    else:
      logging_params = {'logger': None, 'grid_density': grid_density, 'episode_length': None,
                        'record_every_k_timesteps': record_every_k_timesteps,
                        'flush_logger_every': flush_logger_every,
                        'episodes_for_summary_metrics': episodes_for_summary_metrics,
                        'logdir': logdir, 'env_raw_output_file_name': f'log_{mode}_env0.csv'}

    domain, task = name.split('_', 1)
    if isinstance(domain, str):
      from adaptgym.envs.playground import suite
      self._env = suite.load(domain, task, environment_kwargs=dict(env_params=env_params,
                                                                   logging_params=logging_params,
                                                                   control_timestep=control_timestep,
                                                                   physics_timestep=physics_timestep,
                                                                   reset_position_freq=reset_position_freq,
                                                                   use_global_step=use_global_step,
                                                                   aesthetic=aesthetic,
                                                                   wide_fov=wide_fov,
                                                                   ))
      # self._env = suite.load(domain, task, environment_kwargs=dict(aesthetic=aesthetic))

    else:
      assert task is None
      self._env = domain()

    # if 'multiagent' in task:
    print('----> APPLYING SpecifyPrimaryAgent WRAPPER.')
    primary_agent = self._env._task._walkers[self._env._task._primary_agent] # This is specified in the task.
    primary_agent_name = primary_agent._mjcf_root.model # Gets the name specified in the task, i.e. 'agent0'
    self._env = SpecifyPrimaryAgent(self._env, primary_agent_name, self._env.policies, use_global_step=use_global_step)

    self._env = SpoofEpisodicWrapper(self._env, done_every=spoof_done_every)


    self._action_repeat = action_repeat
    self._size = size
    if camera is None:
      camera = dict(quadruped=2, ant=2, humanoid=1, rodent=1).get(domain, 0)
      if 'maze' in task:
        # camera = dict(quadruped=2, ant=3, humanoid=1, rodent=1).get(domain, 0)
        camera = dict(quadruped=2, ant=3, humanoid=1, rodent=1, sphero=1).get(domain, 0)
      if egocentric_camera:
        camera = dict(ant=3, humanoid=3, rodent=4, sphero=2).get(domain, 0)
        if 'maze' in task:
          camera = dict(quadruped=2, ant=4, humanoid=1, rodent=5, sphero=2).get(domain, 0)
    self._camera = camera
    self._multiple_agents = multiple_agents

    self._ignored_keys = []
    for key, value in self._env.observation_spec().items():
      if value.shape == (0,):
        print(f"Ignoring empty observation key '{key}'.")
        self._ignored_keys.append(key)

  @property
  def observation_space(self):
    spaces = {}
    for key, value in self._env.observation_spec().items():
      spaces[key] = gym.spaces.Box(
          -np.inf, np.inf, value.shape, dtype=np.float32)
    spaces['image'] = gym.spaces.Box(
        0, 255, self._size + (3,), dtype=np.uint8)
    return gym.spaces.Dict(spaces)

  @property
  def obs_space(self):  # If different format than observation_space is needed.
    spaces = {
        'image': gym.spaces.Box(0, 255, self._size + (3,), dtype=np.uint8),
        'reward': gym.spaces.Box(-np.inf, np.inf, (), dtype=np.float32),
        'is_first': gym.spaces.Box(0, 1, (), dtype=bool),
        'is_last': gym.spaces.Box(0, 1, (), dtype=bool),
        'is_terminal': gym.spaces.Box(0, 1, (), dtype=bool),
    }
    for key, value in self._env.observation_spec().items():
      if key in self._ignored_keys:
        continue
      if value.dtype == np.float64:
        spaces[key] = gym.spaces.Box(-np.inf, np.inf, value.shape, np.float32)
      elif value.dtype == np.uint8:
        spaces[key] = gym.spaces.Box(0, 255, value.shape, np.uint8)
      else:
        raise NotImplementedError(value.dtype)
    return spaces

  @property
  def action_space(self):
    spec = self._env.action_spec()
    if isinstance(spec, list):
      spec = spec[0]
    action = gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)

    return gym.spaces.Dict({'action': action})

  @property
  def act_space(self): # If different format than action_space is needed.
    return {'action': self.action_space['action']}

  def step(self, action):
    assert np.isfinite(action['action']).all(), action['action']
    reward = 0.0
    for _ in range(self._action_repeat):
      time_step = self._env.step(action['action'])
      reward += time_step.reward or 0.0
      if time_step.last():
        break
    assert time_step.discount in (0, 1)
    obs = {
        'reward': reward,
        'is_first': False,
        'is_last': time_step.last(),
        'is_terminal': time_step.discount == 0,
        'image': self._env.physics.render(*self._size, camera_id=self._camera),
    }
    obs.update({
        k: v for k, v in dict(time_step.observation).items()
        if k not in self._ignored_keys})
    if hasattr(self._env._base_env, 'exploration_tracker'):
      collision_tracker = self._env._base_env.exploration_tracker.collision_tracker
      attention_tracker = self._env._base_env.exploration_tracker.attention_tracker
      info = {'discount': np.array(time_step.discount, np.float32),
              'collision_tracker':collision_tracker, 'attention_tracker': attention_tracker}
    else:
      info = {'discount': np.array(time_step.discount, np.float32)}
    return obs

  def reset(self):
    time_step = self._env.reset()
    obs = {
        'reward': 0.0,
        'is_first': True,
        'is_last': False,
        'is_terminal': False,
        'image': self._env.physics.render(*self._size, camera_id=self._camera),
    }
    obs.update({
        k: v for k, v in dict(time_step.observation).items()
        if k not in self._ignored_keys})
    return obs


  # def step(self, action):
  #   action = action['action']
  #   assert np.isfinite(action).all(), action
  #   reward = 0
  #   for _ in range(self._action_repeat):
  #     time_step = self._env.step(action)
  #     reward += time_step.reward or 0
  #     if time_step.last():
  #       break
  #   obs = dict(time_step.observation)
  #   obs['image'] = self.render()
  #   done = time_step.last()
  #   if hasattr(self._env._base_env, 'exploration_tracker'):
  #     collision_tracker = self._env._base_env.exploration_tracker.collision_tracker
  #     attention_tracker = self._env._base_env.exploration_tracker.attention_tracker
  #     info = {'discount': np.array(time_step.discount, np.float32),
  #             'collision_tracker':collision_tracker, 'attention_tracker': attention_tracker}
  #   else:
  #     info = {'discount': np.array(time_step.discount, np.float32)}
  #   return obs, reward, done, info

  # def reset(self):
  #   time_step = self._env.reset()
  #   if self._multiple_agents:
  #     obs = dict(time_step.observation[0])
  #   else:
  #     obs = dict(time_step.observation)
  #   obs['image'] = self.render()
  #   return obs

  def render(self, *args, **kwargs):
    if kwargs.get('mode', 'rgb_array') != 'rgb_array':
      raise ValueError("Only render mode 'rgb_array' is supported.")
    return self._env.physics.render(*self._size, camera_id=self._camera)

  def __getattr__(self, name):
    return getattr(self._env, name)


class CDMC:
  def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, unconstrain_at_step=5e5):
    os.environ['MUJOCO_GL'] = 'egl'
    ################################################################################
    # Implementation of Cheetah/Walker Run Sparse follows
    # https://github.com/younggyoseo/RE3
    self._name = name
    if name == 'cheetah_run_sparse':
      name = 'cheetah_run'
    if name == 'walker_run_sparse':
      name = 'walker_run'
    ################################################################################
    domain, task = name.split('_', 1)
    if domain == 'cup':  # Only domain with multiple words.
      domain = 'ball_in_cup'
    if isinstance(domain, str):
      from adaptgym.envs.cdmc import suite
      self._env = suite.load(domain, task)
      self._env.task._unconstrain_at_step = unconstrain_at_step
    else:
      assert task is None
      self._env = domain()
    self._action_repeat = action_repeat
    self._size = size
    if camera is None:
      camera = dict(quadruped=2).get(domain, 0)
    self._camera = camera

  @property
  def observation_space(self):
    spaces = {}
    for key, value in self._env.observation_spec().items():
      spaces[key] = gym.spaces.Box(
          -np.inf, np.inf, value.shape, dtype=np.float32)
    spaces['image'] = gym.spaces.Box(
        0, 255, self._size + (3,), dtype=np.uint8)
    return gym.spaces.Dict(spaces)

  @property
  def action_space(self):
    spec = self._env.action_spec()
    action = gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)
    return gym.spaces.Dict({'action': action})

  def step(self, action):
    action = action['action']
    assert np.isfinite(action).all(), action
    reward = 0
    for _ in range(self._action_repeat):
      time_step = self._env.step(action)
      ################################################################################
      step_reward = time_step.reward
      if step_reward is not None:
        if self._name in ('cheetah_run_sparse', 'walker_run_sparse'):
          reward += 0 if step_reward < 0.25 else step_reward
        else:
          reward += step_reward
      ################################################################################
      if time_step.last():
        break
    obs = dict(time_step.observation)
    obs['image'] = self.render()
    done = time_step.last()
    info = {'discount': np.array(time_step.discount, np.float32)}
    return obs, reward, done, info

  def reset(self):
    time_step = self._env.reset()
    obs = dict(time_step.observation)
    obs['image'] = self.render()
    return obs

  def render(self, *args, **kwargs):
    if kwargs.get('mode', 'rgb_array') != 'rgb_array':
      raise ValueError("Only render mode 'rgb_array' is supported.")
    return self._env.physics.render(*self._size, camera_id=self._camera)


class DDMC:
  def __init__(self, name, action_repeat=1, size=(64, 64), camera=None,
               unconstrain_at_step=5e5, config=None):
    os.environ['MUJOCO_GL'] = 'egl'
    ################################################################################
    # Implementation of Cheetah/Walker Run Sparse follows
    # https://github.com/younggyoseo/RE3
    self._name = name
    if name == 'cheetah_run_sparse':
      name = 'cheetah_run'
    if name == 'walker_run_sparse':
      name = 'walker_run'
    ################################################################################
    domain, task = name.split('_', 1)
    if domain == 'cup':  # Only domain with multiple words.
      domain = 'ball_in_cup'
    if isinstance(domain, str):
      from adaptgym.envs.distracting_control import suite

      if config is None:
        print('Default DDMC config.')
        dynamic = False
        num_videos = 3
        randomize_background = 0
        shuffle_background = 0
        do_color_change = 0
        ground_plane_alpha = 0.1
        background_dataset_videos = ['boat', 'bmx-bumps', 'flamingo']
        continuous_video_frames = True
        do_just_background = True
        difficulty = 'easy'
        specify_background = '0,0,1e6;1,1e6,2e6;0,2e6,1e9'  # ABA
      else:
        dynamic = config.dynamic_ddmc
        num_videos = config.num_videos_ddmc
        randomize_background = config.randomize_background_ddmc
        shuffle_background = config.shuffle_background_ddmc
        do_color_change = config.do_color_change_ddmc
        ground_plane_alpha = config.ground_plane_alpha_ddmc
        background_dataset_videos = config.background_dataset_videos_ddmc
        continuous_video_frames = config.continuous_video_frames_ddmc
        do_just_background = config.do_just_background_ddmc
        difficulty = config.difficulty_ddmc
        specify_background = config.specify_background_ddmc

      self._env = suite.load(domain, task, difficulty=difficulty,
                             pixels_only=False, do_just_background=do_just_background,
                             do_color_change=do_color_change,
                             background_dataset_videos=background_dataset_videos,
                             background_kwargs=dict(num_videos=num_videos,
                                                    dynamic=dynamic,
                                                    randomize_background=randomize_background,
                                                    shuffle_buffer_size=shuffle_background*500,
                                                    seed=1,
                                                    ground_plane_alpha=ground_plane_alpha,
                                                    continuous_video_frames=continuous_video_frames,
                                                    specify_background=specify_background,
                                                    ))
    else:
      assert task is None
      self._env = domain()
    self._action_repeat = action_repeat
    self._size = size
    if camera is None:
      camera = dict(quadruped=2).get(domain, 0)
    self._camera = camera

  @property
  def observation_space(self):
    spaces = {}
    for key, value in self._env.observation_spec().items():
      spaces[key] = gym.spaces.Box(
          -np.inf, np.inf, value.shape, dtype=np.float32)
    spaces['image'] = gym.spaces.Box(
        0, 255, self._size + (3,), dtype=np.uint8)
    return gym.spaces.Dict(spaces)

  @property
  def action_space(self):
    spec = self._env.action_spec()
    action = gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)
    return gym.spaces.Dict({'action': action})

  def step(self, action):
    action = action['action']
    assert np.isfinite(action).all(), action
    reward = 0
    for _ in range(self._action_repeat):
      time_step = self._env.step(action)
      ################################################################################
      step_reward = time_step.reward
      if step_reward is not None:
        if self._name in ('cheetah_run_sparse', 'walker_run_sparse'):
          reward += 0 if step_reward < 0.25 else step_reward
        else:
          reward += step_reward
      ################################################################################
      if time_step.last():
        break
    obs = dict(time_step.observation)
    obs['image'] = self.render()
    # del obs['pixels']  # Remove 'pixels', to match original format.
    done = time_step.last()
    info = {'discount': np.array(time_step.discount, np.float32)}
    return obs, reward, done, info

  def reset(self):
    time_step = self._env.reset()
    obs = dict(time_step.observation)
    obs['image'] = self.render()
    # del obs['pixels']  # Remove 'pixels' to match original format.
    return obs

  def render(self, *args, **kwargs):
    if kwargs.get('mode', 'rgb_array') != 'rgb_array':
      raise ValueError("Only render mode 'rgb_array' is supported.")
    return self._env.physics.render(*self._size, camera_id=self._camera)


class SpecifyPrimaryAgent:
  """Specify a primary agent and policies to control all
  other agents in the env, forming a facade such that
  higher level methods think there is only one agent."""

  def __init__(self, env, primary_agent, policies=None, just_primary_agent_obs=True, base_env=None, use_global_step=False):
    """
    :param primary_agent: Name of the agent as specified in by the env, i.e. 'agent0'
    :param policies: dict with policy function handle for each non-primary agent. If contains
                     just a single policy function handle, then that is applied to all agents.
    :param just_primary_agent_obs: bool. Whether to make visible observations of all agents,
          as opposed to just the primary agent.
    :param base_env: The base environment, before any wrappers are applied. This is in case
          any wrappers have been applied prior to calling this wrapper.
    :param use_global_step: Bool. If True then env policies will use a global step (as opposed to resetting when the environment resets).
    """
    self._env = env
    self._primary_agent = primary_agent
    self._just_primary_agent_obs = just_primary_agent_obs
    self._policies = policies
    self._step_number = 0
    self._use_global_step = use_global_step

    if base_env is None:
      self._base_env = env
    else:
      self._base_env = base_env

    self._prev_full_time_step = None   # Previous time step with info for all agents

    # Extract action indices for each agent
    action_names = self._base_env.action_spec().name.split('\t')
    agent_names = list(set(([x.split('/')[0] for x in action_names])))
    agent_inds = {}
    for name in agent_names:
      agent_inds[name] = np.where([name in x for x in action_names])[0]     # TODO: Is this a potential bug?
    self._agent_action_inds = agent_inds


  def __getattr__(self, name):
    return getattr(self._env, name)

  @property
  def observation_space(self):
    spec = self.observation_spec()
    spaces = {}
    for key, value in spec.items():
      spaces[key] = gym.spaces.Box(
        -np.inf, np.inf, value.shape, dtype=np.float32)

    return gym.spaces.Dict(spaces)

  @property
  def action_space(self):
    spec = self.action_spec()
    space = gym.space.Box(
      spec.minimum, spec.maximum, dtype=np.float32)

    return space

  def _trim_time_step(self, full_time_step):
    """
    If self._just_primary_agent_obs == True,
    then removes every entry from the time step that is not
    related to the primary agent.

    :param full_time_step: Time step containing observations for all agents.
    :return: time_step: Time step with observations potentially just for primary agent.
    """
    if self._just_primary_agent_obs:
      full_obs = full_time_step.observation
      obs = dict()
      for key, value in full_obs.items():
        if self._primary_agent in key:
          obs[key] = value
      time_step = dm_env.TimeStep(
        step_type=full_time_step.step_type,
        reward=full_time_step.reward,
        discount=full_time_step.discount,
        observation=obs)
    else:
      time_step = full_time_step

    return time_step

  def step(self, action):
    # If there is a 'policy' for the primary_agent, which may just be for resetting its position, apply that
    if self._primary_agent in self._policies.keys():
      spec = self.agent_action_spec(self._primary_agent)()
      self._policies[self._primary_agent](self._prev_full_time_step, self.physics, self._primary_agent, spec, self._step_number)
      # print('APPLYING PRIMARY_AGENT POLICY')

    # First, get actions for all non-primary agents
    agent_actions = dict()
    for agent, inds in self._agent_action_inds.items():
      if not agent == self._primary_agent:
        spec = self.agent_action_spec(agent)()
        if self._policies is None:
          agent_actions[agent] = pol.random(self._prev_full_time_step, self.physics,agent, spec, self._step_number)
        else:
          if isinstance(self._policies, dict):
            agent_actions[agent] = self._policies[agent](self._prev_full_time_step, self.physics,agent, spec, self._step_number)
          else:
            agent_actions[agent] = self._policies(self._prev_full_time_step, self.physics, agent, spec, self._step_number)

    command = np.zeros(self._base_env.action_spec().shape)
    for agent in self._agent_action_inds.keys():
      if not agent == self._primary_agent:
        command[self._agent_action_inds[agent]] = agent_actions[agent]

    # Include specified action for primary agent.
    command[self._agent_action_inds[self._primary_agent]] = action

    # Take simulation step, and record observation.
    full_time_step = self._base_env.step(command)
    self._prev_full_time_step = full_time_step

    # Now trim entries in time_step so that the observation matches spec
    time_step = self._trim_time_step(full_time_step)         # TODO: Is this a potential bug?

    self._step_number += 1

    return time_step

  def reset(self):
    full_time_step = self._env.reset()
    self._prev_full_time_step = full_time_step
    time_step = self._trim_time_step(full_time_step)
    if not self._use_global_step:
      self._step_number = 0
    else:
      print(f'!!!! Using global step: {self._step_number}')

    return time_step

  def agent_action_spec(self, agent):
    """Clone the action_spec, but only including
    agent-specific actions."""
    full_spec = self._env.action_spec()
    inds = self._agent_action_inds[agent]
    spec = specs.BoundedArray(shape=inds.shape,
                              dtype=full_spec.dtype,
                              minimum=full_spec.minimum[inds],
                              maximum=full_spec.maximum[inds],
                              name='\t'.join([full_spec.name.split('\t')[i] for i in inds]))
    return lambda: spec

  def agent_observation_spec(self, agent):
    """Clone the observation_spec, but only including
    agent-specific observations."""
    full_spec = self._env.observation_spec()
    spec = type(full_spec)()
    for key, value in full_spec.items():
      if agent in key:
        spec[key] = value

    return lambda: spec

  def full_action_spec(self):
    return self._env.action_spec

  @property
  def action_spec(self):
    """Only makes visible the spec for the primary agent.
    If want to see full spec for all agents, use full_action_spec()."""
    return self.agent_action_spec(self._primary_agent)

  @property
  def observation_spec(self):
    if self._just_primary_agent_obs:
      return self.agent_observation_spec(self._primary_agent)
    else:
      return self._env.observation_spec

  @property
  def physics(self):
    return self._env.physics


class SpoofEpisodicWrapper:
  def __init__(self, env, done_every=500):
    # super().__init__(env)
    self._env = env
    self.done_every = done_every
    self.step_count = 0
    self.last_time_step = None
    self.environment_done = None

  def step(self, action):
    self.step_count += 1

    time_step = self._env.step(action)
    self.last_time_step = time_step
    self.environment_done = time_step.last()
    # self.environment_done = time_step['is_last']

    if self.step_count % self.done_every == 0:
      print(f'SpoofEpisodicWrapper: Sending done based on step_count ({self.step_count}) and done_every {self.done_every}')
      time_step = dm_env.TimeStep(dm_env.StepType.LAST, time_step.reward, time_step.discount, time_step.observation)
      # time_step['is_last'] = True

    return time_step

  def reset(self):
    if self.last_time_step is None or self.environment_done:
      print('SpoofEpisodicWrapper: True environment reset')
      return self._env.reset()
    else:
      print('SpoofEpisodicWrapper: Intercepting reset')
      return self.last_time_step

  def __getattr__(self, name):
    return getattr(self._env, name)
