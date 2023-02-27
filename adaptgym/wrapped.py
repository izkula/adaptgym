"""Wrapped version of environments that includes rendering of image observation."""

import os
import gym
import numpy as np

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

  def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, unconstrain_at_step=5e5,
               config=None):
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
        specify_background = '0,0,1e6;1,1e6,2e6;0,2e6,1e9'
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

