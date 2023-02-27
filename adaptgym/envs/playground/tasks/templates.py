import numpy as np
# from dm_control.locomotion.arenas import labmaze_textures
from dm_control.locomotion.props import target_sphere
from adaptgym.envs.playground.arenas import mazes, labmaze_textures


# def maze_vel_template(maze_str, var_str, agents, primary_agent, scale=1.0,
#                       height_str=None, wall_str=None, reward_args=None,
#                       aliveness_reward=0.01, aliveness_thresh=-0.5):
#
#   from labmaze import fixed_maze
#   maze = fixed_maze.FixedMazeWithRandomGoals(
#     entity_layer=maze_str,
#     variations_layer=var_str,
#     spawn_token='P',
#     num_objects=None,
#     object_token='G',
#     random_state=np.random.RandomState(12346)
#   )
#   if height_str is None:
#     wall_heights = 0.8*scale
#   else:
#     wall_heights = height_str
#
#   arena = mazes.MazeWithTargets(
#     maze,
#     xy_scale=2.0*scale,
#     z_height=2.0*scale,
#     skybox_texture=None,
#     # wall_textures=labmaze_textures.WallTextures(style='style_01'),
#     wall_textures={'*': labmaze_textures.WallTextures(style='style_01'),
#                    '&': labmaze_textures.WallTextures(style='style_02'),
#                    '^': labmaze_textures.WallTextures(style='style_03'),
#                    '%': labmaze_textures.WallTextures(style='style_04')},
#     floor_textures=None,
#     aesthetic='outdoor_natural',
#     agent_spawn_tokens=agents.keys(),
#     wall_heights=wall_heights,
#     wall_positions=wall_str,
#   )
#
#   from envs.playground.tasks import multiagent_goal_maze
#   task = multiagent_goal_maze.RepeatSingleGoalMaze(
#     walkers=agents,
#     maze_arena=arena,
#     target=target_sphere.TargetSphere(radius=0.5 * scale, height_above_ground=2 * scale),
#     control_timestep=.03,
#     physics_timestep=.005,
#     contact_termination=False,
#     randomize_spawn_position=False,
#     randomize_spawn_rotation=False,
#     nconmax=600,
#     njmax=600,
#     z_spawn=0.5,
#     enable_global_task_observables=True,
#     dense_reward_scaling=1,
#     aliveness_reward=aliveness_reward,
#     aliveness_thresh=aliveness_thresh,
#     target_reward_scale=1,  # For time_limit=1e3
#     primary_agent=primary_agent,
#     reward_args=reward_args,
#   )
#
#   return arena, task

def maze_goal_template(maze_str, var_str, agents, primary_agent, scale=1.0,
                       height_str=None, wall_str=None, reward_args=None,
                       aliveness_reward=0.01, aliveness_thresh=-0.5, continuous_aliveness=False,
                       accel_cost_scale=0.0, vel_cost_scale=0.0,
                       target_height=0.5, random_seed=None,
                       z_height=2.0, border_scale=6,
                       randomize_spawn_position=False,
                       randomize_spawn_rotation=False,
                       spawn_rotation_radians=None,
                       control_timestep=None,
                       physics_timestep=None,
                       wall_overwrite_color=None,
                       indiv_squares=True
                       ):
  if control_timestep is None or physics_timestep is None:
    raise('Must set control_timestep and physics_timestep in config.')
  from labmaze import fixed_maze
  maze = fixed_maze.FixedMazeWithRandomGoals(
    entity_layer=maze_str,
    variations_layer=var_str,
    spawn_token='P',
    num_objects=None,
    object_token='G',
    random_state=np.random.RandomState(12346)
  )

  if height_str is None:
    wall_heights = 0.8*scale
  else:
    wall_heights = height_str

  wall_textures = {'*': labmaze_textures.WallTextures(style='style_01'),
                   '&': labmaze_textures.WallTextures(style='style_02'),
                   '^': labmaze_textures.WallTextures(style='style_03'),
                   '%': labmaze_textures.WallTextures(style='style_04'),
                   '@': labmaze_textures.WallTextures(style='style_05'),
                   'w': labmaze_textures.WallTextures(style='style_white'),
                   'b': labmaze_textures.WallTextures(style='style_black'),
                   'g': labmaze_textures.WallTextures(style='style_gray')}
  if wall_overwrite_color is not None:
    wall_textures = {k: labmaze_textures.WallTextures(style=f'style_{wall_overwrite_color}') for k in wall_textures.keys()}
    wall_textures['w'] = labmaze_textures.WallTextures(style='style_white')
    wall_textures['b'] = labmaze_textures.WallTextures(style='style_black')
    wall_textures['g'] = labmaze_textures.WallTextures(style='style_gray')

  arena = mazes.MazeWithTargets(
    maze,
    xy_scale=2.0*scale,
    z_height=z_height*scale,
    border_scale=border_scale,
    skybox_texture=None,
    # wall_textures=labmaze_textures.WallTextures(style='style_01'),
    wall_textures=wall_textures,
    floor_textures=None,
    aesthetic='outdoor_natural',
    agent_spawn_tokens=agents.keys(),
    wall_heights=wall_heights,
    wall_positions=wall_str,
    indiv_squares=indiv_squares,
  )

  if reward_args is not None:
    dense_reward_scaling = reward_args['dense_reward_scaling']
    if 'target_reward_scaling' in reward_args.keys():
      target_reward_scale = reward_args['target_reward_scaling']
  else:
    dense_reward_scaling = 0
    target_reward_scale = 0

  from adaptgym.envs.playground.tasks import multiagent_goal_maze
  task = multiagent_goal_maze.RepeatSingleGoalMaze(
    walkers=agents,
    maze_arena=arena,
    target=target_sphere.TargetSphere(radius=0.5*scale, height_above_ground=target_height*scale),
    control_timestep=control_timestep,
    physics_timestep=physics_timestep,
    contact_termination=False,
    randomize_spawn_position=randomize_spawn_position,
    randomize_spawn_rotation=randomize_spawn_rotation,
    spawn_rotation_radians=spawn_rotation_radians,
    nconmax=600,
    njmax=600,
    z_spawn=2.0*scale,
    enable_global_task_observables=True,
    dense_reward_scaling=dense_reward_scaling,
    aliveness_reward=aliveness_reward,
    aliveness_thresh=aliveness_thresh,
    target_reward_scale=target_reward_scale,  # For time_limit=1e3
    primary_agent=primary_agent,
    reward_args=reward_args,
    continuous_aliveness=continuous_aliveness,
    accel_cost_scale=accel_cost_scale,
    vel_cost_scale=vel_cost_scale,
    random_seed=random_seed,
  )
  return arena, task