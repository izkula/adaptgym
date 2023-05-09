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


def mazemultiagentEmpty0(agent, scale, environment_kwargs):
  """Still spheres in each corner. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  }
  return env

def mazemultiagentPosition1(agent, scale, environment_kwargs):
  """Spheres in each corner, target position #1."""
  m, v, h, w = custom_mazes.get_custom_maze(id=8)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=100)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)

  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env


def mazemultiagentPosition2(agent, scale, environment_kwargs):
  """Spheres in each corner, target position #2."""
  m, v, h, w = custom_mazes.get_custom_maze(id=9)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=100)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env


def mazemultiagentPosition3(agent, scale, environment_kwargs):
  """Spheres in each corner, target position #2."""
  m, v, h, w = custom_mazes.get_custom_maze(id=9)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=100)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env

def mazemultiagentVelocity1(agent, scale, environment_kwargs):
  """Spheres in each corner, target velocity in x direction."""
  m, v, h, w = custom_mazes.get_custom_maze(id=8)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=100)

  reward_args = {'goal': 'velocity', 'xvel': 3.0, 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env


def mazemultiagentVelocity2(agent, scale, environment_kwargs):
  """Spheres in each corner, target velocity in x direction."""
  m, v, h, w = custom_mazes.get_custom_maze(id=8)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=100)

  reward_args = {'goal': 'velocity', 'yvel': 3.0, 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env


def mazemultiagentDoors1(agent, scale, environment_kwargs):
  """Position target, no spheres blocking doors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=10)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=0.5),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentDoors1a(agent, scale, environment_kwargs):
  """Position target, big stationary spheres blocking doors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=10)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentDoors2(agent, scale, environment_kwargs):
  """Position target, easier position relative to doors, no spheres blocking doors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=14)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=0.5),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentDoors2a(agent, scale, environment_kwargs):
  """Position target, easier position relative to doors, no spheres blocking doors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=14)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=1)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=1)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=0.5),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentSteps1(agent, scale, environment_kwargs):
  """Steps, no obstacles"""
  m, v, h, w = custom_mazes.get_custom_maze(id=11)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=2000)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentSteps2(agent, scale, environment_kwargs):
  m, v, h, w = custom_mazes.get_custom_maze(id=12)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentSteps3(agent, scale, environment_kwargs):
  """Steps, push ball, roll over ball."""
  m, v, h, w = custom_mazes.get_custom_maze(id=13)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentSteps4(agent, scale, environment_kwargs):
  """Steps, no obstacles, always moving towards target"""
  m, v, h, w = custom_mazes.get_custom_maze(id=15)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=2000)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentSteps5(agent, scale, environment_kwargs):
  """Steps, no obstacles, always moving towards target"""
  m, v, h, w = custom_mazes.get_custom_maze(id=15)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=2000)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.random, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract2(agent, scale, environment_kwargs):
  """Spheres in each corner, a few walls and stairs to climb up."""
  m, v, h, w = custom_mazes.get_custom_maze(id=5)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 * scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env


def mazemultiagentInteract3(agent, scale, environment_kwargs):
  """Sequences of doorways with spheres rolling back and forth in front of them."""
  m, v, h, w = custom_mazes.get_custom_maze(id=7)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 *scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 *scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8 *scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8 *scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=100)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  if scale == 0.1:
    env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                    'ball3': functools.partial(pol.circle_periodic, scale=1.0),
                    'ball4': functools.partial(pol.still, scale=1.0),
                    'ball5': functools.partial(pol.line_periodic, scale=1.0, period=200),
                  }
  elif scale == 0.7:
    env.policies = {'ball2': functools.partial(pol.line_periodic, scale=2.0, period=400),
                    'ball3': functools.partial(pol.circle_periodic, scale=1.0),
                    'ball4': functools.partial(pol.still, scale=1.0),
                    'ball5': functools.partial(pol.line_periodic, scale=3.0, period=400),
                  }
  return env

def mazemultiagentInteract4(agent, scale, environment_kwargs):
  """Spheres in each corner, a few walls and stairs to climb up."""
  m, v, h, w = custom_mazes.get_custom_maze(id=5)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, random_seed=None,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env

def mazemultiagentInteract5(agent, scale, environment_kwargs):
  """Spheres in each corner, a few walls and stairs to climb up. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=5)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env

def mazemultiagentInteract6(agent, scale, environment_kwargs):
  """Spheres in each corner, a few walls and stairs to climb up."""
  m, v, h, w = custom_mazes.get_custom_maze(id=5)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                  'ball3': functools.partial(pol.circle_periodic, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.random, scale=0.5),
                  }
  return env


def mazemultiagentInteract7(agent, scale, environment_kwargs):
  """Still spheres in each corner, a few walls and stairs to climb up. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=5)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract8(agent, scale, environment_kwargs):
  """Still spheres in each corner, a few walls and stairs to climb up. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=5)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract9(agent, scale, environment_kwargs):
  """Still spheres in each corner. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract9_1(agent, scale, environment_kwargs):
  """Still spheres in each corner. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract9_2(agent, scale, environment_kwargs):
  """Still spheres in each corner. Removing two spheres that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract9_3(agent, scale, environment_kwargs):
  """Still spheres in each corner. Removing two spheres that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract10(agent, scale, environment_kwargs):
  """Still spheres in each corner. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract10_2(agent, scale, environment_kwargs):
  """Still spheres in each corner. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=17)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract11(agent, scale, environment_kwargs):
  """Smaller Still spheres in each corner. Removing one sphere that will become novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.7 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.7 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.7 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.7 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract12(agent, scale, environment_kwargs):
  """Smaller still spheres in each corner. Adding in novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.7 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.7 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.7 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.7 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract13(agent, scale, environment_kwargs):
  """Still spheres in each corner. Two (heavy) spheres."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=2e9)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[1., 1., 0], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=2e9)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract14(agent, scale, environment_kwargs):
  """Still spheres in each corner. Unique colors. Two (heavy) spheres. Playground for Interact15"""
  m, v, h, w = custom_mazes.get_custom_maze(id=16_2)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=2e9)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.9 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=2e9)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.9 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15(agent, scale, environment_kwargs):
  """Two (heavy) spheres and two light spheres blocking target."""
  m, v, h, w = custom_mazes.get_custom_maze(id=18)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=2e9)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.9 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=2e9)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.9 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_2(agent, scale, environment_kwargs):
  """Two (heavy) spheres and two light spheres blocking doors, doors closer together than in 15."""
  m, v, h, w = custom_mazes.get_custom_maze(id=19)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=2e9)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.9 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=2e9)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.9 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_3(agent, scale, environment_kwargs):
  """Same as 15_2 but no obstacles"""
  m, v, h, w = custom_mazes.get_custom_maze(id=19)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=2e9)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.9 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=2e9)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.9 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_4(agent, scale, environment_kwargs):
  """Two (heavy) spheres and two light spheres blocking doors, doors closer together than in 15, with a wall."""
  m, v, h, w = custom_mazes.get_custom_maze(id=21)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=2e9)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.9 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=2e9)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.9 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_5(agent, scale, environment_kwargs):
  """Same as 15_4 but with no objects blocking doors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=21)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.9 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.9 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=2e9)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.9 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=2e9)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.9 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_6(agent, scale, environment_kwargs):
  """Same as 15_5 but with no walls."""
  m, v, h, w = custom_mazes.get_custom_maze(id=22)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_7(agent, scale, environment_kwargs):
  """One set of walls"""
  m, v, h, w = custom_mazes.get_custom_maze(id=23)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract15_example_8(agent, scale, environment_kwargs):
  """Same as 15_7 but with starting position shifted over to use for example episode."""
  m, v, h, w = custom_mazes.get_custom_maze(id=24)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  rotation = np.pi
  reward_args = {'goal': 'position', 'dense_reward_scaling': 1}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             randomize_spawn_rotation=False,
                                             spawn_rotation_radians=3*np.pi/2,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract16(agent, scale, environment_kwargs):
  """Jumping spheres. Playground for Interact15"""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.JumpingBall(name="ball2", size=1.2 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=0.1)
  agents['3'] = jumping_ball.JumpingBall(name="ball3", size=1.2 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1)
  agents['4'] = jumping_ball.JumpingBall(name="ball4", size=1.2 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=0.1)
  agents['5'] = jumping_ball.JumpingBall(name="ball5", size=1.2 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=0.1)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1, z_height=10.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.jump_periodic, scale=1),
                  'ball3': functools.partial(pol.jump_periodic, scale=1),
                  'ball4': functools.partial(pol.jump_periodic, scale=1),
                  'ball5': functools.partial(pol.jump_periodic, scale=1),
                  }
  return env

def mazemultiagentInteract17(agent, scale, environment_kwargs):
  """Jumping spheres."""
  m, v, h, w = custom_mazes.get_custom_maze(id=20)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.JumpingBall(name="ball2", size=1.2 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=0.1)
  agents['3'] = jumping_ball.JumpingBall(name="ball3", size=1.2 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1)
  agents['4'] = jumping_ball.JumpingBall(name="ball4", size=1.2 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=0.1)
  agents['5'] = jumping_ball.JumpingBall(name="ball5", size=1.2 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=0.1)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1, z_height=4.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.jump_periodic, scale=1),
                  'ball3': functools.partial(pol.jump_periodic, scale=1),
                  'ball4': functools.partial(pol.jump_periodic, scale=1),
                  'ball5': functools.partial(pol.jump_periodic, scale=1),
                  }
  return env

def mazemultiagentInteract17_1(agent, scale, environment_kwargs):
  """Same as 17 but removing the ball obstacles."""
  m, v, h, w = custom_mazes.get_custom_maze(id=20)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.JumpingBall(name="ball2", size=1.2 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=0.1)
  # agents['3'] = jumping_ball.JumpingBall(name="ball3", size=1.2 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1)
  # agents['4'] = jumping_ball.JumpingBall(name="ball4", size=1.2 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=0.1)
  # agents['5'] = jumping_ball.JumpingBall(name="ball5", size=1.2 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=0.1)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1, z_height=4.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.jump_periodic, scale=1),
                  'ball3': functools.partial(pol.jump_periodic, scale=1),
                  'ball4': functools.partial(pol.jump_periodic, scale=1),
                  'ball5': functools.partial(pol.jump_periodic, scale=1),
                  }
  return env

def mazemultiagentInteract18(agent, scale, environment_kwargs):
  """Jumping spheres in each corner. Unique colors. Two (heavy) spheres. Playground for Interact15"""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.JumpingBall(name="ball2", size=1.2 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=0.1)
  agents['3'] = jumping_ball.JumpingBall(name="ball3", size=1.2 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1)
  agents['4'] = jumping_ball.JumpingBall(name="ball4", size=1.2 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=0.1)
  agents['5'] = jumping_ball.JumpingBall(name="ball5", size=1.2 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=0.1)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=2.5,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.jump_periodic, scale=1),
                  'ball3': functools.partial(pol.jump_periodic, scale=1),
                  'ball4': functools.partial(pol.jump_periodic, scale=1),
                  'ball5': functools.partial(pol.jump_periodic, scale=1),
                  }
  return env

def mazemultiagentInteract19_1_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_2_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_3_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_4_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_5_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object.
  Switched blue and purple colors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_6_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object.
  Switched blue and purple colors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_6_2_play(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object.
  Switched blue and purple colors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_1_novel(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=20.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_5_novel(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object.
  Switched blue and purple colors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_6_novel(agent, scale, environment_kwargs):
  """Still spheres in each corner, simpler color scheme. Adding novel object.
  Switched blue and purple colors."""
  m, v, h, w = custom_mazes.get_custom_maze(id=16)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_7_play_ball3(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_7_play_ball4(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.03  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_7_play_ball4_reset(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=252)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color=None,
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  # reset_position_freq = 100000
  env.policies = {
                  'ball4': functools.partial(pol.reset_position, walker = agents['4'],  reset_position_freq = reset_position_freq,
                                              start_pos = [7, 7]),
                  # 'ball4': functools.partial(pol.still, scale=1),
                  'agent0': functools.partial(pol.reset_position, walker = agents['0'], reset_position_freq = reset_position_freq,
                                              start_pos = [0, 0]),  ### XXX
                  }
  return env

def mazemultiagentInteract19_7_play_ball4_reset_white(agent, scale, environment_kwargs):
  """Still spheres in each corner, walls are white.
  One object: magenta (ball4) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=252)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='white',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  # reset_position_freq = 100000
  env.policies = {
                  'ball4': functools.partial(pol.reset_position, walker = agents['4'],  reset_position_freq = reset_position_freq,
                                              start_pos = [7, 7]),
                  # 'ball4': functools.partial(pol.still, scale=1),
                  'agent0': functools.partial(pol.reset_position, walker = agents['0'], reset_position_freq = reset_position_freq,
                                              start_pos = [0, 0]),  ### XXX
                  }
  return env

def mazemultiagentInteract19_7_play_ball4_reset_black(agent, scale, environment_kwargs):
  """Still spheres in each corner, walls are black.
  One objects: magenta (ball4) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=252)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  # reset_position_freq = 100000
  env.policies = {
                  'ball4': functools.partial(pol.reset_position, walker = agents['4'],  reset_position_freq = reset_position_freq,
                                              start_pos = [7, 7]),
                  # 'ball4': functools.partial(pol.still, scale=1),
                  'agent0': functools.partial(pol.reset_position, walker = agents['0'], reset_position_freq = reset_position_freq,
                                              start_pos = [0, 0]),  ### XXX
                  }
  return env

def mazemultiagentInteract19_7_play_ball4_reset_gray(agent, scale, environment_kwargs):
  """Still spheres in each corner, walls are gray.
  One object: magenta (ball4) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=252)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='gray',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  # reset_position_freq = 100000
  env.policies = {
                  'ball4': functools.partial(pol.reset_position, walker = agents['4'],  reset_position_freq = reset_position_freq,
                                              start_pos = [7, 7]),
                  # 'ball4': functools.partial(pol.still, scale=1),
                  'agent0': functools.partial(pol.reset_position, walker = agents['0'], reset_position_freq = reset_position_freq,
                                              start_pos = [0, 0]),  ### XXX
                  }
  return env

def mazemultiagentInteract19_7_play_ball4_setposition(agent, scale, environment_kwargs):
  """Still spheres in each corner, walls are black.
  One objects: magenta (ball4) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=252)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black',
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  reset_position_freq = environment_kwargs['reset_position_freq']
  # reset_position_freq = 100000
  env.policies = {
                  'ball4': functools.partial(pol.hardcode_trajectory, walker = agents['4'],  reset_position_freq = reset_position_freq,
                                              start_pos = [7, 7]),
                  # 'ball4': functools.partial(pol.still, scale=1),
                  # 'agent0': functools.partial(pol.reset_position, walker = agents['0'], reset_position_freq = reset_position_freq,
                  #                             start_pos = [0, 0]),  ### XXX
                  }
  return env

def mazemultiagentInteract19_7_novel(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres. """
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_7_novel_example_b3(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball3 (yellow)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=27)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = 0 * np.pi / 2,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_7_novel_example_b3_black(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball3 (yellow)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=27)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black')
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_7_novel_example_b4(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball4 (magenta)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=28)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_7_novel_example_b4_black(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball4 (magenta)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=28)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': 0 * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black')
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_7_novel_example_b3_2(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball3 (yellow), going diagonal from starting in center"""
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': (0.5) * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_7_novel_example_b3_2_black(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball3 (yellow), going diagonal from starting in center"""
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': (0.52) * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black')
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_7_novel_example_b4_2(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball4 (magenta), going diagonal from starting in center"""
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': -(0.5) * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_7_novel_example_b4_2_black(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Two objects: magenta (ball4) and yellow (ball3) spheres.
  Set up to make example episode, running into ball4 (magenta), going diagonal from starting in center"""
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False,
                                             spawn_rotation_radians = {'0': -(0.6) * np.pi / 2},
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             wall_overwrite_color='black')
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_8_novel(agent, scale, environment_kwargs):
  """Novel room (maze), with two spheres. Door open to new chamber """
  m, v, h, w = custom_mazes.get_custom_maze(id=31) #29
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_8_novel_b3(agent, scale, environment_kwargs):
  """Novel room (maze), with one yellow sphere. Door open to new chamber """
  m, v, h, w = custom_mazes.get_custom_maze(id=31)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_8_novel_b4(agent, scale, environment_kwargs):
  """Novel room (maze), with one magenta sphere. Door open to new chamber """

  m, v, h, w = custom_mazes.get_custom_maze(id=31)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env


def mazemultiagentInteract19_9_novel(agent, scale, environment_kwargs):
  """Novel room (non-maze), with two spheres. Door open to new chamber """
  m, v, h, w = custom_mazes.get_custom_maze(id=29) #29
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_9_novel_b3(agent, scale, environment_kwargs):
  """Novel room (non-maze), with one yellow sphere. Door open to new chamber """
  m, v, h, w = custom_mazes.get_custom_maze(id=29)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_9_novel_b4(agent, scale, environment_kwargs):
  """Novel room (non-maze), with one magenta sphere. Door open to new chamber """

  m, v, h, w = custom_mazes.get_custom_maze(id=29)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_10_novel(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Three objects: magenta (ball4), yellow (ball3) spheres, red (ball5)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=251)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 0.], rgb2=[0.8, 0, 0.0], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_10_play_b3(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Three objects: magenta (ball4), yellow (ball3) spheres, red (ball5)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=251)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 0.], rgb2=[0.8, 0, 0.0], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract19_10_play_b4(agent, scale, environment_kwargs):
  """Still spheres in each corner, front and back walls are different textures.
  Three objects: magenta (ball4), yellow (ball3) spheres, red (ball5)"""
  m, v, h, w = custom_mazes.get_custom_maze(id=251)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  # agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 0.], rgb2=[0.8, 0, 0.0], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentInteract20_tv(agent, scale, environment_kwargs):
  """TV attempt"""
  m, v, h, w = custom_mazes.get_custom_maze(id=25)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 0, 0], rgb2=[0.8, 0, 0], mass=20)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  # agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)
  # agents['5'] = jumping_ball.RollingBall(name="ball5", size=1.1 * scale, rgb1=[1., 0, 1.], rgb2=[0.8, 0, 0.8], mass=20)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=2, randomize_spawn_rotation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1),
                  'ball4': functools.partial(pol.still, scale=1),
                  'ball5': functools.partial(pol.still, scale=1),
                  }
  return env

def mazemultiagentExplore1(agent, scale, environment_kwargs):
  """Simpler maze."""
  m, v, h, w = custom_mazes.get_custom_maze(id=100)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8 * scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=2)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8 * scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)

  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=0, vel_cost_scale=0, target_height=0.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )

  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)

  add_expl_tracker(env, primary_agent, environment_kwargs)

  env.reset()
  env.policies = {'ball2': functools.partial(pol.still, scale=1),
                  'ball3': functools.partial(pol.still, scale=1)}

  return env

def mazemultiagentExplore2(agent, scale, environment_kwargs):
  """More complex maze."""
  m, v, h, w = custom_mazes.get_custom_maze(id=101)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=0, vel_cost_scale=0, target_height=0.0,
                                             random_seed=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {}
  return env




def mazemultiagentExplore3(agent, scale, environment_kwargs):
  """More complex maze with very tall walls."""
  m, v, h, w = custom_mazes.get_custom_maze(id=101)
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=0, vel_cost_scale=0, target_height=0.0,
                                             random_seed=1, z_height=10.0,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(
                             time_limit=MAX_TIME, #1000
                             task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {}
  return env

############################################################################

def multiagent_dynamics_train(agent, scale, environment_kwargs):
  """ball with circle periodic for training"""
  m, v, h, w = custom_mazes.get_custom_maze(id='dynamics')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)

  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)

  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=42,
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.circle_periodic, scale=1),
                  'ball2': functools.partial(pol.circle_periodic, scale=1),
                  }
  return env


def multiagent_dynamics_test(agent, scale, environment_kwargs):
  """ball with circle periodic for training, ball with jump periodic for testing (new dynamics)"""
  m, v, h, w = custom_mazes.get_custom_maze(id='dynamics')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=20)
  agents['2'] = jumping_ball.JumpingBall(name="novel", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1)
  if environment_kwargs['env_params']:
      randomize_spawn_rotation = environment_kwargs['env_params'].get('randomize_spawn_rotation', True)
      spawn_rotation_radians = environment_kwargs['env_params'].get('spawn_rotation_radians', None)
  else:
      randomize_spawn_rotation = True
      spawn_rotation_radians = None
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=randomize_spawn_rotation, spawn_rotation_radians=spawn_rotation_radians,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.circle_periodic, scale=1),
                  'novel': functools.partial(pol.jump_periodic, scale=10, period=10),
                  }
  return env

################################################################################################


def multiagent_corridor_train(agent, scale, environment_kwargs):
  """corridors with the same color"""
  m, v, h, w = custom_mazes.get_custom_maze(id='corridor')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  }
  return env


def multiagent_corridor_test(agent, scale, environment_kwargs):
  """corridors with the different color"""
  m, v, h, w = custom_mazes.get_custom_maze(id='corridor_new_texture')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {
                  }
  return env


############################################################################

def multiagent_violation1_train(agent, scale, environment_kwargs):
  """ball with line periodic for training"""
  m, v, h, w = custom_mazes.get_custom_maze(id='violation1')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1, friction=1.)


  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False, spawn_rotation_radians={'1': 0, '2': 0},
                                             z_height=12, border_scale=1,
                                             use_violation=False,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.line_periodic, period=100, scale=100),
                  'ball2': functools.partial(pol.line_periodic, period=100, scale=-100),
                  }
  return env


def multiagent_violation1_test(agent, scale, environment_kwargs):
  """ball going through wall"""
  m, v, h, w = custom_mazes.get_custom_maze(id='violation1')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="novel", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=False, spawn_rotation_radians={'1': 0, '2': 0},
                                             z_height=12, border_scale=1,
                                             use_violation=True,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent , environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.line_periodic, period=100, scale=100),
                  'novel': functools.partial(pol.line_periodic, period=150, scale=500),
                  }
  return env



############################################################################

def multiagent_violation2_train(agent, scale, environment_kwargs):
  """ball with line periodic for training"""
  m, v, h, w = custom_mazes.get_custom_maze(id='violation2')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)


  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  env.policies = {
      'ball1': functools.partial(pol.line_periodic, period=200, scale=10),
      'ball2': functools.partial(pol.line_periodic, period=200, scale=10),
      # 'ball1': functools.partial(pol.line_periodic_teleport,  walker=agents['1'], period_line=200, period_tp=50, scale=10, dist=2.5),
                  }
  return env


def multiagent_violation2_test(agent, scale, environment_kwargs):
  """ball teleportation"""
  m, v, h, w = custom_mazes.get_custom_maze(id='violation2')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="novel", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.line_periodic, period=200, scale=10),
                  'novel': functools.partial(pol.line_periodic_teleport,  walker=agents['2'], period_line=200, period_tp=50, scale=10, dist=2.5),
                  }
  return env


############################################################################

def multiagent_colorchange_train(agent, scale, environment_kwargs):
  """ball still"""
  m, v, h, w = custom_mazes.get_custom_maze(id='colorchange')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[1.0, 1., 0], mass=20, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[1.0, 1., 0], mass=20, friction=1.)

  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.still),
                  'ball2': functools.partial(pol.still),
                  }
  return env

def multiagent_colorchange_test(agent, scale, environment_kwargs):
  """ball with mass and elasticity difference"""
  m, v, h, w = custom_mazes.get_custom_maze(id='colorchange')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0.],  rgb2=[1.0, 1.0, 0.], mass=20, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="novel", size=1.1 * scale, rgb1=[1.0, 1., 0.],  rgb2=[1.0, 1.0,  0.], mass=20, friction=1.)
  if environment_kwargs['env_params']:
      randomize_spawn_rotation = environment_kwargs['env_params'].get('randomize_spawn_rotation', True)
      spawn_rotation_radians = environment_kwargs['env_params'].get('spawn_rotation_radians', None)
      randomize_spawn_position = environment_kwargs['env_params'].get('randomize_spawn_position', False)
  else:
      randomize_spawn_rotation = True
      spawn_rotation_radians = None
      randomize_spawn_position = False
  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_position=randomize_spawn_position,randomize_spawn_rotation=randomize_spawn_rotation, spawn_rotation_radians=spawn_rotation_radians,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=None,
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.still),
                  'novel': functools.partial(pol.color_change, walker=agents['2'], rgb=np.array([0.0,1.0,0.0]), period=10),
                  }
  return env

def multiagent_colorchange_random(agent, scale, environment_kwargs):
  """ball with mass and elasticity difference"""
  m, v, h, w = custom_mazes.get_custom_maze(id='colorchange')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0.],  rgb2=[1.0, 1.0, 0.], mass=20, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="novel", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=20, friction=1.)
  if environment_kwargs['env_params']:
      randomize_spawn_rotation = environment_kwargs['env_params'].get('randomize_spawn_rotation', True)
      spawn_rotation_radians = environment_kwargs['env_params'].get('spawn_rotation_radians', None)
      randomize_spawn_position = environment_kwargs['env_params'].get('randomize_spawn_position', False)
  else:
      randomize_spawn_rotation = True
      spawn_rotation_radians = None
      randomize_spawn_position = False
  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_position=randomize_spawn_position,randomize_spawn_rotation=randomize_spawn_rotation, spawn_rotation_radians=spawn_rotation_radians,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=None,
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.still),
                  'novel': functools.partial(pol.color_change, walker=agents['2'], rgb=np.array([0.0,0.5,0.5]), period=10, do_random=1),
                  }
  return env

def multiagent_colorchange_multi(agent, scale, environment_kwargs):
  """Immoveable balls that all change color with a predictable sequence"""
  m, v, h, w = custom_mazes.get_custom_maze(id='colorchange_collision')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  if environment_kwargs['env_params']:
      randomize_spawn_rotation = environment_kwargs['env_params'].get('randomize_spawn_rotation', True)
      spawn_rotation_radians = environment_kwargs['env_params'].get('spawn_rotation_radians', None)
      randomize_spawn_position = environment_kwargs['env_params'].get('randomize_spawn_position', False)
  else:
      randomize_spawn_rotation = True
      spawn_rotation_radians = None
      randomize_spawn_position = False
  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_position=randomize_spawn_position,randomize_spawn_rotation=randomize_spawn_rotation, spawn_rotation_radians=spawn_rotation_radians,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=None,
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  rgbs = [np.array([1.0,0.0,0.0]), np.array([0.0,1.0,0.0]), np.array([0.0,0.0,1.0]), np.array([1.0,1.0,0.0]), np.array([0.0,1.0,1.0])]
  env.policies = {'ball1': functools.partial(pol.color_change_multi, walker=agents['1'], rgbs=rgbs, period=2),
                  'ball2': functools.partial(pol.color_change_multi, walker=agents['2'], rgbs=rgbs, period=2),
                  'ball3': functools.partial(pol.color_change_multi, walker=agents['3'], rgbs=rgbs, period=2),
                  'ball4': functools.partial(pol.color_change_multi, walker=agents['4'], rgbs=rgbs, period=2),
                  }
  return env


def multiagent_colorchange_collision(agent, scale, environment_kwargs):
  """Immoveable balls that change to a random color upon collision"""
  m, v, h, w = custom_mazes.get_custom_maze(id='colorchange_collision')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  agents['3'] = jumping_ball.RollingBall(name="ball3", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  agents['4'] = jumping_ball.RollingBall(name="ball4", size=1.1 * scale, rgb1=[1.0, 1., 1.0],  rgb2=[1.0, 1.0,  1.0], mass=200000000, friction=10000.)
  if environment_kwargs['env_params']:
      randomize_spawn_rotation = environment_kwargs['env_params'].get('randomize_spawn_rotation', True)
      spawn_rotation_radians = environment_kwargs['env_params'].get('spawn_rotation_radians', None)
      randomize_spawn_position = environment_kwargs['env_params'].get('randomize_spawn_position', False)
  else:
      randomize_spawn_rotation = True
      spawn_rotation_radians = None
      randomize_spawn_position = False
  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_position=randomize_spawn_position,randomize_spawn_rotation=randomize_spawn_rotation, spawn_rotation_radians=spawn_rotation_radians,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=None,
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  last_collision_step = np.array([0])
  env.policies = {'ball1': functools.partial(pol.color_change_collision, walker=agents['1'], primary_agent='agent0', last_collision_step=last_collision_step),
                  'ball2': functools.partial(pol.color_change_collision, walker=agents['2'], primary_agent='agent0', last_collision_step=last_collision_step),
                  'ball3': functools.partial(pol.color_change_collision, walker=agents['3'], primary_agent='agent0', last_collision_step=last_collision_step),
                  'ball4': functools.partial(pol.color_change_collision, walker=agents['4'], primary_agent='agent0', last_collision_step=last_collision_step),
                  }
  return env

############################################################################

def multiagent_object_appear(agent, scale, environment_kwargs):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='object_appear')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="novel", size=[1.4 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.line_periodic, period=200, scale=10),
                  'novel': functools.partial(pol.object_appear, walker=agents['2'], step_appear=100, scale=10, dist=2.5),
                  }
  return env

############################################################################

def multiagent_massdiff_train(agent, scale, environment_kwargs):
  """ball still"""
  m, v, h, w = custom_mazes.get_custom_maze(id='massdiff')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent

  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=100, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="ball2", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=100, friction=1.)

  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent,environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.still),
                  'ball2': functools.partial(pol.still),
                  }
  return env


def multiagent_massdiff_test(agent, scale, environment_kwargs):
  """ball with mass and elasticity difference"""
  m, v, h, w = custom_mazes.get_custom_maze(id='massdiff')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="ball1", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=100, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="novel", size=1.1 * scale, rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=0.001, friction=0.0001)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1, randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  env.policies = {'ball1': functools.partial(pol.still),
                  'novel': functools.partial(pol.still),
                  }
  return env








############################################################################
#### BEGIN ARENAS ##########################################################
############################################################################

def multiagent_homecage(agent, scale, environment_kwargs):
  m, v, h, w = custom_mazes.get_custom_maze(id='homecage')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  env.policies = {#'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=10*fs, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  }
  return env

def multiagent_single_object(agent, scale, environment_kwargs):
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=1, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'],
                                              reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_black(agent, scale, environment_kwargs, include_tracker=True):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[0.7 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

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
  fs = int(1.0/control_timestep)
  s = scale*1.0
  b = 60*20 # seconds per block
  p = 5 # padding in homecage before any objects appear
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=(1+p)*b*fs, step_disappear=(3+p)*b*fs, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=(2+p)*b*fs, step_disappear=(5+p)*b*fs, start_pos=[5*s, (-5-2)*s]),
                  'object3': functools.partial(pol.object_appear, walker=agents['3'], step_appear=(4+p)*b*fs, step_disappear=(7+p)*b*fs, start_pos=[-5*s,(-5-2.1)*s]),
                  'object4': functools.partial(pol.object_appear, walker=agents['4'], step_appear=(6+p)*b*fs, step_disappear=(8+p)*b*fs, start_pos=[-5*s, (5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'],
                                              reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_test(agent, scale, environment_kwargs, include_tracker=True):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

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
  ## Note: step_appear and step_disappear are in the environment space (i.e. they are not divided by action_repeat)
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=300, step_disappear=600, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=300, step_disappear=600, start_pos=[5*s, (-5-2)*s]),
                  'object3': functools.partial(pol.object_appear, walker=agents['3'], step_appear=300, step_disappear=600, start_pos=[-5 * s, (-5 - 2) * s]),
                  'object4': functools.partial(pol.object_appear, walker=agents['4'], step_appear=300, step_disappear=600, start_pos=[-5 * s, (5 - 2) * s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_simple_black(agent, scale, environment_kwargs, include_tracker=True):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
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
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=2e6, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=1e6, step_disappear=2e6, start_pos=[5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_simple500_black(agent, scale, environment_kwargs, include_tracker=True):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
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
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=1e6, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=5e5, step_disappear=1e6, start_pos=[5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_step1(agent, scale, environment_kwargs, include_tracker=True):
  """Arena for novel object"""
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


def multiagent_novel_objects_step1_obj(agent, scale, environment_kwargs, include_tracker=True):
  """Arena for novel object"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[.8, .8, .8],  rgb2=[0.6, 0.6, 0.6], mass=1, friction=1.)
  agents['3'] = jumping_ball.RollingBall(name="object3", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[.6, .6, .6],  rgb2=[0.4, 0.4, 0.4], mass=1, friction=1.)
  agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[.4, .4, .4],  rgb2=[0.2, 0.2, 0.2], mass=1, friction=1.)

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
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=0, step_disappear=None, start_pos=[5*s, (-5-2)*s]),
                  'object3': functools.partial(pol.object_appear, walker=agents['3'], step_appear=0,
                                               step_disappear=None, start_pos=[-5*s, (5-2)*s]),
                  'object4': functools.partial(pol.object_appear, walker=agents['4'], step_appear=0,
                                               step_disappear=None, start_pos=[-5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env



def multiagent_novel_objects_step2(agent, scale, environment_kwargs, include_tracker=True):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
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
  fs = int(1.0/control_timestep)
  fm = 60*fs # frames per minute
  s = scale*1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=30*fm, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=15*fm, step_disappear=30*fm, start_pos=[5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_step2_reset(agent, scale, environment_kwargs, include_tracker=True):
  """Teleport a novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
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
  fs = int(1.0/control_timestep)
  fm = 60*fs # frames per minute
  s = scale*1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {'object1': functools.partial(pol.reset_position, walker=agents['1'], reset_position_freq=15*fm, step_disappear=30*fm, start_pos=[3*s, (3-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=15*fm, step_disappear=30*fm, start_pos=[3*s, (-3-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env

def multiagent_novel_objects_step2_inf(agent, scale, environment_kwargs, include_tracker=True):
  """Yellow and magenta balls in an arena, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
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
  fs = int(1.0/control_timestep)
  fm = 60*fs # frames per minute
  s = scale*1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=0, step_disappear=None, start_pos=[5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env


def multiagent_novel_objects_step2_long(agent, scale, environment_kwargs, include_tracker=True):
  """Yellow and magenta balls in an arena, never disappear."""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
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
  fs = int(1.0/control_timestep)
  fm = 60*fs # frames per minute
  s = scale*1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0*s, -2*s]
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=1e6, step_disappear=None, start_pos=[5*s, (-5-2)*s]),
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
                                 step_appear=5e5,  # 0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
  }
  return env

def multiagent_novel_objects_step1step2_single_magenta_debug3e4(agent, scale, environment_kwargs, include_tracker=True):
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
                                 step_appear=3e4,  # 0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
  }
  return env

def multiagent_novel_objects_step1step2_single_magenta_debug1e4(agent, scale, environment_kwargs, include_tracker=True):
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
                                 step_appear=1e4,  # 0, #3e4,
                                 step_disappear=None,
                                 start_pos=[5 * s, (-5 - 2) * s],
                                 # reset_position_freq=reset_position_freq,
                                 ),
    'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq,
                                start_pos=start_pos),
  }
  return env


def multiagent_novel_objects_step1step2(agent, scale, environment_kwargs, include_tracker=True):
  """Magenta then yellow ball in an arena after a small burnin period with empty room, never disappear."""
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
  fm = 60 * fs  # frames per minute
  s = scale * 1.0
  reset_position_freq = environment_kwargs['reset_position_freq']
  start_pos = [0 * s, -2 * s]
  s0 = 5e5
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'],
                                               step_appear=(s0 + 0),
                                               step_disappear=None,
                                               # step_disappear=(s0 + 30 * fm),
                                               start_pos=[5 * s, (5 - 2) * s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'],
                                               step_appear=(s0 + 15 * fm),
                                               step_disappear=None,
                                               # step_disappear=(s0 + 30 * fm),
                                               start_pos=[5 * s, (-5 - 2) * s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'],
                                              reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env


def multiagent_flashing_object(agent, scale, environment_kwargs):
  """Teleport a flashing novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1, friction=1.)

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
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0*fs, step_disappear=None, start_pos=[5*s, (3-2)*s]),
                  'object2': functools.partial(pol.object_appear_and_color_change, walker=agents['2'], step_appear=0*fs,
                                               step_disappear=None, start_pos=[5*s, (-3-2)*s], period=10, do_random=True),
                  }
  return env


def multiagent_flashing_objects(agent, scale, environment_kwargs):
  """Teleport a multiple flashing novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  s = 0.95
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['3'] = jumping_ball.RollingBall(name="object3", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['4'] = jumping_ball.RollingBall(name="object4", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)

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
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  dx = 3
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0*fs, step_disappear=None, start_pos=[dx*s, (-1-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=0 * fs, step_disappear=None, start_pos=[dx * s, (1 - 2) * s]),
                  'object3': functools.partial(pol.object_appear_and_color_change, walker=agents['3'], step_appear=0*fs,
                                               step_disappear=None, start_pos=[-dx*s, (-1-2)*s], period=10, do_random=True),
                  'object4': functools.partial(pol.object_appear_and_color_change, walker=agents['4'],
                                               step_appear=0 * fs,
                                               step_disappear=None, start_pos=[-dx * s, (1 - 2) * s], period=10,
                                               do_random=True),
                  }
  return env

def multiagent_interactive_flashing_object(agent, scale, environment_kwargs):
  """Teleport a flashing novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  s = 0.95
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['3'] = jumping_ball.RollingBall(name="object3", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['4'] = jumping_ball.RollingBall(name="object4", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)

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
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  # control_timestep = 0.02  # Check this against config file!
  control_timestep = float(environment_kwargs['control_timestep'])
  fs = int(1.0/control_timestep)
  s = scale*1.0
  last_collision_step = np.array([0])
  dx = 3
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0*fs, step_disappear=None, start_pos=[dx*s, (-1-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=0*fs, step_disappear=None, start_pos=[dx*s, (1-2)*s]),
                  'object3': functools.partial(pol.object_appear_and_color_change_collision, walker=agents['3'],
                                               step_appear=0 * fs,
                                               step_disappear=None, start_pos=[-dx * s, (-1 - 2) * s], do_random=True,
                                               primary_agent='agent0', last_collision_step=last_collision_step,
                                               other_agents_to_change=['object4']),
                  'object4': functools.partial(pol.object_appear_and_color_change_collision, walker=agents['4'],
                                               step_appear=0 * fs,
                                               step_disappear=None, start_pos=[-dx * s, (1 - 2) * s], do_random=True,
                                               primary_agent='agent0', last_collision_step=last_collision_step,
                                               other_agents_to_change=['object3']),
                  }
  return env

def multiagent_interactive_flashing_object_test(agent, scale, environment_kwargs):
  """Teleport a flashing novel object into the arena"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  s = 0.9
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['3'] = jumping_ball.RollingBall(name="object3", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)
  agents['4'] = jumping_ball.RollingBall(name="object4", size=[s * scale, s * scale, s * scale], rgb1=[1., 1., 1.],  rgb2=[0.8, 0.8, 0.8], mass=1e10, friction=1.)

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
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  last_collision_step = np.array([0])
  env.policies = {'object1': functools.partial(pol.object_appear_and_color_change_collision, walker=agents['1'],
                                               step_appear=0*fs,
                                               step_disappear=None, start_pos=[2*s, (0-2)*s], do_random=True,
                                               primary_agent='agent0', last_collision_step=last_collision_step),
                  'object2': functools.partial(pol.object_appear_and_color_change_collision, walker=agents['2'],
                                               step_appear=0*fs,
                                               step_disappear=None, start_pos=[2*s, (-2-2)*s], do_random=True,
                                               primary_agent='agent0', last_collision_step=last_collision_step),
                  'object3': functools.partial(pol.object_appear_and_color_change_collision, walker=agents['3'],
                                               step_appear=0 * fs,
                                               step_disappear=None, start_pos=[-2 * s, (-2 - 2) * s], do_random=True,
                                               primary_agent='agent0', last_collision_step=last_collision_step,
                                               other_agents_to_change=['object4']),
                  'object4': functools.partial(pol.object_appear_and_color_change_collision, walker=agents['4'],
                                               step_appear=0 * fs,
                                               step_disappear=None, start_pos=[-2 * s, (0 - 2) * s], do_random=True,
                                               primary_agent='agent0', last_collision_step=last_collision_step,
                                               other_agents_to_change=['object3']),
                  }
  return env

def multiagent_openfield(agent, scale, environment_kwargs):
  m, v, h, w = custom_mazes.get_custom_maze(id='openfield')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=50.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  env.policies = {#'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=10*fs, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  }
  return env

def multiagent_openfield_shelter(agent, scale, environment_kwargs):
  pass

def multiagent_labyrinth(agent, scale, environment_kwargs, include_tracker=True):
  m, v, h, w = custom_mazes.get_custom_maze(id='labyrinth')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=40.0,
                                             random_seed=1,randomize_spawn_rotation=True,
                                             z_height=12, border_scale=1,
                                             control_timestep=float(environment_kwargs['control_timestep']),
                                             physics_timestep=float(environment_kwargs['physics_timestep']),
                                             indiv_squares=False,
                                             )
  env = composer.Environment(time_limit=MAX_TIME, task=task,
                             random_state=np.random.RandomState(12345),
                             strip_singleton_obs_buffer_dim=True)
  if include_tracker:
    add_expl_tracker(env, primary_agent, environment_kwargs)
  env.reset()
  control_timestep = 0.02  # Check this against config file!
  fs = int(1.0/control_timestep)
  s = scale*1.0
  env.policies = {#'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=10*fs, step_disappear=None, start_pos=[5*s, (5-2)*s]),
                  }
  return env

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


def multiagent_location_target(agent, scale, environment_kwargs, include_tracker=True):
  """Sparse extrinsic reward"""
  m, v, h, w = custom_mazes.get_custom_maze(id='novel_objects')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)

  # reward_args = {'goal': 'velocity', 'xvel': 3.0}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=None,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
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
  env.policies = {'object1': functools.partial(pol.object_appear, walker=agents['1'], step_appear=0, step_disappear=2e6, start_pos=[5*s, (5-2)*s]),
                  'object2': functools.partial(pol.object_appear, walker=agents['2'], step_appear=1e6, step_disappear=2e6, start_pos=[5*s, (-5-2)*s]),
                  'agent0': functools.partial(pol.reset_position, walker=agents['0'], reset_position_freq=reset_position_freq, start_pos=start_pos),
                  }
  return env


def multiagent_sparse_goal(agent, scale, environment_kwargs, include_tracker=True):
  """A position goal with a sparse reward"""
  m, v, h, w = custom_mazes.get_custom_maze(id='sparse_goal')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 0, 'target_reward_scaling': 100}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
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

def multiagent_dense_goal(agent, scale, environment_kwargs, include_tracker=True):
  """A position goal with a sparse reward"""
  m, v, h, w = custom_mazes.get_custom_maze(id='sparse_goal')
  primary_agent = '0'
  agents = {}
  agents[primary_agent] = agent
  # agents['1'] = jumping_ball.RollingBall(name="object1", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 1., 0],  rgb2=[0.8, 0.8, 0], mass=1, friction=1.)
  # agents['2'] = jumping_ball.RollingBall(name="object2", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[1.0, 0., 1.],  rgb2=[0.8, 0., 0.8], mass=1, friction=1.)
  # agents['3'] = jumping_ball.RollingBall(name="object3", size=[0.7 * scale, 0.7 * scale, 1.1 * scale], rgb1=[1.0, 0., 0],  rgb2=[0.8, 0., 0], mass=2, friction=1.)
  # agents['4'] = jumping_ball.RollingBall(name="object4", size=[1.1 * scale, 1.1 * scale, 1.1 * scale], rgb1=[0.0, 0., 1.0],  rgb2=[0., 0., 0.8], mass=0.1, friction=1.)

  reward_args = {'goal': 'position', 'dense_reward_scaling': 1, 'target_reward_scaling': 10}
  arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w, reward_args=reward_args,
                                             aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
                                             accel_cost_scale=50.0, vel_cost_scale=0.0, target_height=3.0,
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