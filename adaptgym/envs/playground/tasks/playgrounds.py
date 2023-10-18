"""Central repository of playground tasks that can be run with different agents."""

import functools
import numpy as np
import matplotlib.pyplot as plt

import warnings
with warnings.catch_warnings():
  warnings.filterwarnings("ignore", category=DeprecationWarning)
  import dm_control
  from dm_control.composer.variation import distributions
  from dm_control.utils import containers
  from dm_control import composer

from adaptgym.envs.playground.walkers import jumping_ball
from adaptgym.envs.playground.walkers import rodent

from adaptgym.envs.playground.tasks import templates
import adaptgym.envs.playground.policies.policies as pol
from adaptgym.envs.playground.tasks import custom_mazes
# from training.utils.exploration_tracker import ExplorationTracker
from adaptgym.envs.playground.exploration_tracker import ExplorationTracker

MAX_TIME = int(1e9)

def add_expl_tracker(env, primary_agent, environment_kwargs):
  """Add exploration tracker (which logs positions of agents) to environment."""
  exploration_tracker = ExplorationTracker(env_name='sphero-playground',
                                           run_id=np.random.randint(100, 1000),
                                           walkers=env.task._walkers,
                                           primary_agent_id=primary_agent,
                                           target_name='target',
                                           params=environment_kwargs['logging_params'])
  env.add_extra_hook('after_step', exploration_tracker.after_step)
  env.add_extra_hook('initialize_episode', exploration_tracker.initialize_episode)
  env.exploration_tracker = exploration_tracker #add tracker for accessing data




############################################################################
#### BEGIN ARENAS ##########################################################
############################################################################

def multiagent_novel_objects_step1(agent, scale, environment_kwargs, include_tracker=True):
  """Empty arena for novel object, with no object appearing."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  s = scale*1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {#'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=2e6, start_pos=[5*s, (5-2)*s]),
                  #'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=1e6, step_disappear=2e6, start_pos=[5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env


def multiagent_novel_objects_step2_single_magenta(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                       rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  fm = 60 * fs  # frames per minute
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
   # 'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=None,
   #                              start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=0, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env

def multiagent_novel_objects_step1step2_single_magenta(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after time allowed to explore the empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                       rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  fm = 60 * fs  # frames per minute
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    # 'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=None,
    #                              start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=5e5,  # 0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
  }
  return env


def multiagent_novel_objects_step1step2_single_magenta_debug1e4(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a very short time to explore the empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                       rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  fm = 60 * fs  # frames per minute
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    # 'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=None,
    #                              start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=1e4,  # 0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
  }
  return env


############################################################
##########    Experimental tasks below    ##################
############################################################


def multiagent_labyrinth_black(agent, scale, environment_kwargs, include_tracker=True):
  id = 'labyrinth_fast'
  m, v, h, w = custom_mazes.get_custom_maze(id=id)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=10, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             indiv_squares=False,
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  if id == 'labyrinth_fast':
    start_pos = [-20, 0]
  elif id == 'labyrinth':
    start_pos = [-10, 0]
  env.policies = {#'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=10*fs, step_disappear=None, start_pos=[5*s, (5-2)*s]),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),  ### XXX
  }
  return env


def multiagent_labyrinth_black_example(agent, scale, environment_kwargs, include_tracker=True):
  id = 'labyrinth_fast'
  m, v, h, w = custom_mazes.get_custom_maze(id=id)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=False,
                                             spawn_rotation_radians={'0': 0 * np.pi / 2},
                                             z_height=10, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             indiv_squares=False,
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  if id == 'labyrinth_fast':
    start_pos = [-20, 0]
  elif id == 'labyrinth':
    start_pos = [-10, 0]
  env.policies = {#'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=10*fs, step_disappear=None, start_pos=[5*s, (5-2)*s]),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),  ### XXX
  }
  return env


def multiagent_novel_objects_step2step3_magenta_to_yellow(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=500e3,
                                step_disappear=None,
                                start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=0, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_novel_objects_step2step3_yellow_to_magenta(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=0,
                                step_disappear=None,
                                start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=500e3, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_novel_objects_step2step3_magenta_to_yellow_debug1e4(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=2e4,
                                step_disappear=None,
                                start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=1e4, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_novel_objects_step2step3_yellow_to_magenta_debug1e4(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=1e4,
                                step_disappear=None,
                                start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=2e4, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env

def multiagent_novel_objects_step2step3_magenta_to_yellow_debug5e2(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=10e2,
                                step_disappear=None,
                                start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=5e2, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env

def multiagent_novel_objects_step2step3_yellow_to_magenta_debug5e2(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                         rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=5e2,
                                step_disappear=None,
                                start_pos=[5 * s, (5 - 2) * s]),
    'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                 step_appear=10e2, #0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env




def multiagent_distal(agent, scale, environment_kwargs, include_tracker=True):
  """Arena with distal cues."""
  m, v, h, w = custom_mazes.get_custom_maze(id='distal')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                       rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=5.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=20, border_scale=0.3,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    # 'object1': functools.partial(pol.object_appear, walker=agents['1'],
    #                             step_appear=0,
    #                             step_disappear=None,
    #                             start_pos=[5 * s, (5 - 2) * s]),
    # 'object2': functools.partial(pol.object_appear, walker=agents['2'],
    #                              step_appear=500e3, #0, #3e4,
    #                              step_disappear=None,
    #                              start_pos=[5 * s, (-5 - 2) * s],
    #                              # reset_position_freq=reset_position_freq,
    #                              ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env



def multiagent_distal_column1(agent, scale, environment_kwargs, include_tracker=True):
  """Arena with distal cues."""
  m, v, h, w = custom_mazes.get_custom_maze(id='distal_c1')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                       rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=5.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=20, border_scale=0.3,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    # 'object1': functools.partial(pol.object_appear, walker=agents['1'],
    #                             step_appear=0,
    #                             step_disappear=None,
    #                             start_pos=[5 * s, (5 - 2) * s]),
    # 'object2': functools.partial(pol.object_appear, walker=agents['2'],
    #                              step_appear=500e3, #0, #3e4,
    #                              step_disappear=None,
    #                              start_pos=[5 * s, (-5 - 2) * s],
    #                              # reset_position_freq=reset_position_freq,
    #                              ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_distal_column2(agent, scale, environment_kwargs, include_tracker=True):
  """Arena with distal cues."""
  m, v, h, w = custom_mazes.get_custom_maze(id='distal_c2')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                       rgb1=[1.0, 1., 0], rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=5.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=20, border_scale=0.3,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    # 'object1': functools.partial(pol.object_appear, walker=agents['1'],
    #                             step_appear=0,
    #                             step_disappear=None,
    #                             start_pos=[5 * s, (5 - 2) * s]),
    # 'object2': functools.partial(pol.object_appear, walker=agents['2'],
    #                              step_appear=500e3, #0, #3e4,
    #                              step_disappear=None,
    #                              start_pos=[5 * s, (-5 - 2) * s],
    #                              # reset_position_freq=reset_position_freq,
    #                              ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env




############################################################
##########    Evaluation tasks below      ##################
############################################################

def multiagent_object_example1(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[0 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_object_example2(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear. Object slightly off center"""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[2 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_object_example3(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear. Start somewhat close to object."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example2')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[0 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env

def multiagent_object_example4(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear. Start very close to object."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example3')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[0 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env

def multiagent_object_example5(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example4')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[0 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_object_example6(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example4')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3.3 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[0 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env

def multiagent_object_example7(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball in an arena after a small burnin period with empty room, never disappear."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example4')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             # spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             spawn_rotation_radians={'0': 3.32 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[0 * s, 8 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env


def multiagent_object_example8(agent, scale, environment_kwargs, include_tracker=True, color='magenta', step_appear=0):
  """Magenta ball starts off to the side of the ball, goes straight past the ball."""
  if color == 'yellow':
    rgb1 = [1.0, 1., 0]
    rgb2 = [0.8, 0.8, 0]
  elif color == 'magenta':
    rgb1 = [1.0, 0, 1.0]
    rgb2 = [0.8, 0, 0.8]
  elif color == 'white':
    rgb1 = [1.0, 1.0, 1.0]
    rgb2 = [0.8, 0.8, 0.8]


  m, v, h, w = custom_mazes.get_custom_maze(id='object_example')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
                                        rgb1=rgb1, rgb2=rgb2, mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale],
  #                                        rgb1=[1.0, 0., 1.], rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': 3 * np.pi / 2},
                                             # spawn_rotation_radians={'0': 3.32 * np.pi / 2},
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0 / control_timestep)
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  env.policies = {
    'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                step_appear=step_appear,
                                step_disappear=None,
                                start_pos=[3 * s, 0 * s]),

    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
    }
  return env
