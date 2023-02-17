import functools
import numpy as np
import matplotlib.pyplot as plt

from dm_control.composer.variation import distributions

from dm_control.utils import containers
from dm_control import composer

# Run through corridor example
# from dm_control.locomotion.walkers import rodent
from dm_control.locomotion.tasks import corridors as corr_tasks

from dm_control.locomotion.arenas import labmaze_textures
# from dm_control.locomotion.arenas import mazes
# from dm_control.locomotion.tasks import random_goal_maze
from dm_control.locomotion.props import target_sphere

# from dm_control.locomotion.arenas import corridors as corr_arenas
from envs.playground.arenas import corridors as corr_arenas
from envs.playground.arenas import mazes
from envs.playground.tasks import random_goal_maze
from envs.playground.walkers import jumping_ball
from envs.playground.walkers import rodent

from envs.playground.tasks import templates
import envs.playground.policies.policies as pol
from envs.playground.tasks import custom_mazes
from envs.playground.tasks import playgrounds

_CONTROL_TIMESTEP = .02
_PHYSICS_TIMESTEP = 0.001

SUITE = containers.TaggedTasks()

@SUITE.add('benchmarking')
def empty(environment_kwargs=None):
    if not environment_kwargs:
        aesthetic = 'default'
    else:
        aesthetic = environment_kwargs['aesthetic']

    walker = rodent.Rat(
        observable_options={'egocentric_camera': dict(enabled=True)})

    arena = corr_arenas.EmptyCorridor(
        corridor_width=4,
        corridor_length=40,
        visible_side_planes=False,
        aesthetic=aesthetic,
    )

    task = corr_tasks.RunThroughCorridor(
        walker=walker,
        arena=arena,
        walker_spawn_position=(0.5, 0, 0),
        target_velocity=3.0,
        physics_timestep=0.005,
        control_timestep=0.03,
        contact_termination=False,
    )
    env = composer.Environment(
        task=task,
        time_limit=10,
        random_state=np.random.RandomState(42),
        strip_singleton_obs_buffer_dim=True,
    )
    env.reset()
    pixels = []
    for camera_id in range(5):
        pixels.append(env.physics.render(camera_id=camera_id, width=240))
    plt.imshow(np.hstack(pixels))
    plt.show()

    return env


@SUITE.add('benchmarking')
def gaps(environment_kwargs=None):
    if not environment_kwargs:
        aesthetic = 'default'
    else:
        aesthetic = environment_kwargs['aesthetic']

    walker = rodent.Rat(
        observable_options={'egocentric_camera': dict(enabled=True)})

    arena = corr_arenas.GapsCorridor(
        platform_length=distributions.Uniform(0.01, 0.02),
        gap_length=distributions.Uniform(1, 2),
        corridor_width=0.5,
        corridor_length=40,
        aesthetic=aesthetic,
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
    for camera_id in range(5):
        pixels.append(env.physics.render(camera_id=camera_id, width=240))
    plt.imshow(np.hstack(pixels))
    plt.show()

    return env

@SUITE.add('benchmarking')
def walls(environment_kwargs=None):
    if not environment_kwargs:
        aesthetic = 'default'
    else:
        aesthetic = environment_kwargs['aesthetic']

    walker = rodent.Rat(
        observable_options={'egocentric_camera': dict(enabled=True)})

    arena = corr_arenas.WallsCorridor(
        wall_gap=3.,
        wall_width=distributions.Uniform(3., 3.5),
        wall_height=distributions.Uniform(0.1, 0.5),
        corridor_width=4.,
        corridor_length=30.,
        aesthetic=aesthetic,
    )
    task = corr_tasks.RunThroughCorridor(
        walker=walker,
        arena=arena,
        walker_spawn_position=(0.5, 0, 0),
        target_velocity=3.0,
        physics_timestep=0.005,
        control_timestep=0.03,
        contact_termination=False,
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
def maze(environment_kwargs):
    if not environment_kwargs:
        aesthetic = 'default'
    else:
        aesthetic = environment_kwargs['aesthetic']

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
        contact_termination=False,
    )
    random_state = np.random.RandomState(12345)

    env = composer.Environment(time_limit=30,
                                task=task,
                                random_state=random_state,
                                strip_singleton_obs_buffer_dim=True)
    env.reset()

    return env


@SUITE.add('benchmarking')
def maze3agent(environment_kwargs):
    agents = []

    # Add ball objects
    agents.append(rodent.Rat(name="agent1"))
    # agents.append(rodent.Rat(name="agent2"))
    agents.append(jumping_ball.RollingBall(
        name="ball1", size=0.04,
        rgb1=[1.0, .5, .1], rgb2=[.1, .1, 1.0]))
    agents.append(jumping_ball.RollingBall(
        name="ball2", size=0.06,
        rgb1=[1.0, .5, .1], #rgb2=[.5, .1, 1.0]
        rgb2=[1.0, .5, .1]))
    agents.append(jumping_ball.RollingBall(
        name="ball3", size=0.08,
        rgb1=[1.0, .5, .1], rgb2=[.9, .05, .05]))

    skybox_texture = labmaze_textures.SkyBox(style='sky_03')
    wall_textures = labmaze_textures.WallTextures(style='style_01')
    floor_textures = labmaze_textures.FloorTextures(style='style_01')

    do_random_maze = False
    if do_random_maze:
        arena = mazes.RandomMazeWithTargets(
            x_cells=11,
            y_cells=11,
            xy_scale=0.1,
            max_rooms=4,
            z_height=0.3,
            room_min_size=4,
            room_max_size=8,
            spawns_per_room=4,
            targets_per_room=2,
            wall_textures=wall_textures,
            aesthetic='outdoor_natural')
    else:
        from labmaze import fixed_maze
        maze_str = "*******\n" \
                   "* P P *\n" \
                   "*G P G*\n" \
                   "* P P *\n" \
                   "*G P G*\n" \
                   "*******\n"
        var_str =  ".......\n" \
                   ".AAAAA.\n" \
                   ".AAAAA.\n" \
                   ".AAAAA.\n" \
                   ".AAAAA.\n" \
                   ".......\n"
        ### I should also specify heights here too eventually?
        maze = fixed_maze.FixedMazeWithRandomGoals(
            entity_layer=maze_str,
            variations_layer=var_str,
            spawn_token='P',
            object_token='G',
            random_state=np.random.RandomState(12346)
        )
        arena = mazes.MazeWithTargets(
            maze,
            xy_scale=0.5,
            z_height=0.4,
            skybox_texture=None,
            wall_textures=wall_textures,
            floor_textures=None,
            aesthetic='outdoor_natural',
        )

    from envs.playground.tasks import multiagent_goal_maze
    task = multiagent_goal_maze.NullGoalMaze(
        walkers=agents,
        maze_arena=arena,
        control_timestep=.03,
        physics_timestep=.005,
        contact_termination=False,
        randomize_spawn_position=False,
        randomize_spawn_rotation=False,
        nconmax=600,
        njmax=600,
        z_spawn=0.5,
        enable_global_task_observables=True,
    )
    random_state = np.random.RandomState(12345)

    env = composer.Environment(time_limit=30,
                                task=task,
                                random_state=random_state,
                                strip_singleton_obs_buffer_dim=True)
    env.reset()

    return env

# @SUITE.add('benchmarking')
# def mazevelocitymultiagent(environment_kwargs):
#     print('---> Using mazevelocitymultiagent.')
#     scale = 0.2
#
#     agents = {}
#     primary_agent = '0'
#     agents[primary_agent] = rodent.Rat(name="agent0")
#     agents['2'] = jumping_ball.RollingBall(
#         name="ball2", size=0.8*scale,
#         rgb1=[1.0, 0, 0],
#         rgb2=[1.0, 0, 0])
#     agents['3'] = jumping_ball.RollingBall(
#         name="ball3", size=0.8*scale,
#         rgb1=[0, 1., 0],
#         rgb2=[0, 1., 0])
#     agents['4'] = jumping_ball.RollingBall(
#         name="ball4", size=0.8*scale,
#         rgb1=[0, 0, 1.],
#         rgb2=[0, 0, 1.])
#     agents['5'] = jumping_ball.RollingBall(
#         name="ball5", size=0.8*scale,
#         rgb1=[1.0, .5, .1],
#         rgb2=[1.0, .5, .1])
#
#     skybox_texture = labmaze_textures.SkyBox(style='sky_03')
#     wall_textures = labmaze_textures.WallTextures(style='style_01')
#     floor_textures = labmaze_textures.FloorTextures(style='style_01')
#
#     from labmaze import fixed_maze
#     maze_str = "**********************\n" \
#                "****               ***\n" \
#                "*                   **\n" \
#                "*                    *\n" \
#                "*    2          4    *\n" \
#                "*                    *\n" \
#                "*          0        G*\n" \
#                "*                    *\n" \
#                "*                    *\n" \
#                "*    5         3     *\n" \
#                "*                    *\n" \
#                "*  *                **\n" \
#                "**********************\n"
#     var_str =  "......................\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                ".AAAAAAAAAAAAAAAAAAAA.\n" \
#                "......................\n"
#
#     maze = fixed_maze.FixedMazeWithRandomGoals(
#         entity_layer=maze_str,
#         variations_layer=var_str,
#         spawn_token='P',
#         num_objects=None,
#         object_token='G',
#         random_state=np.random.RandomState(12346)
#     )
#     arena = mazes.MazeWithTargets(
#         maze,
#         xy_scale=scale,
#         z_height=1.0*scale,
#         skybox_texture=None,
#         wall_textures=wall_textures,
#         floor_textures=None,
#         aesthetic='outdoor_natural',
#         agent_spawn_tokens=agents.keys()
#     )
#
#     from envs.playground.tasks import multiagent_goal_maze
#     task = multiagent_goal_maze.VelocityMaze(
#         walkers=agents,
#         maze_arena=arena,
#         primary_agent=primary_agent,
#         control_timestep=.03,
#         physics_timestep=.005,
#         contact_termination=False,
#         randomize_spawn_position=False,
#         randomize_spawn_rotation=False,
#         nconmax=600,
#         njmax=600,
#         z_spawn=0.5,
#         aliveness_reward=0.01,
#         target_velocity=2.5,
#     )
#
#     random_state = np.random.RandomState(12345)
#
#     env = composer.Environment(time_limit=30,
#                                 task=task,
#                                 random_state=random_state,
#                                 strip_singleton_obs_buffer_dim=True)
#     env.reset()
#
#     import envs.playground.policies.policies as pol
#     env.policies = functools.partial(pol.circle_periodic, scale=1*scale)
#     #env.policies = functools.partial(pol.still, scale=1)
#     return env


@SUITE.add('benchmarking')
def mazemultiagentTarget1(environment_kwargs):
    print('---> Using mazemultiagentTarget1.')
    scale = 0.2
    maze_str = custom_mazes.mazes[0]
    var_str = custom_mazes.vars[0]
    primary_agent = '0'
    agents = {}
    agents[primary_agent] = rodent.Rat(name="agent0")
    agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1.0, 0, 0])
    agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8*scale, rgb1=[0, 1., 0], rgb2=[0, 1., 0])
    agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8*scale, rgb1=[0, 0, 1.], rgb2=[0, 0, 1.])
    agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8*scale, rgb1=[1.0, .5, .1], rgb2=[1.0, .5, .1])

    reward_args = {'goal': 'velocity', 'xvel': 3.0}
    arena, task = templates.maze_vel_template(maze_str, var_str, agents, primary_agent, reward_args, scale)

    env = composer.Environment(time_limit=30,
                                task=task,
                                random_state=np.random.RandomState(12345),
                                strip_singleton_obs_buffer_dim=True)
    env.reset()

    env.policies = functools.partial(pol.circle_periodic, scale=scale)
    return env

@SUITE.add('benchmarking')
def mazemultiagent3(environment_kwargs):
    print('---> Using mazemultiagent3.')
    scale = 0.1
    maze_str = custom_mazes.mazes[3]
    var_str = custom_mazes.vars[3]
    primary_agent = '0'
    agents = {}
    agents[primary_agent] = rodent.Rat(name="agent0")
    agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1])
    agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8*scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0])
    agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8*scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0])
    agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8*scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.])

    arena, task = templates.maze_goal_template(maze_str, var_str, agents, primary_agent, scale)
    env = composer.Environment(time_limit=100,
                                task=task,
                                random_state=np.random.RandomState(12345),
                                strip_singleton_obs_buffer_dim=True)
    env.reset()
    env.policies = functools.partial(pol.circle_periodic, scale=scale)
    return env


@SUITE.add('benchmarking')
def mazemultiagentInteract1(environment_kwargs):
    scale = 0.1
    maze_str = custom_mazes.mazes[4]
    var_str = custom_mazes.vars[4]
    height_str = custom_mazes.heights[4]
    wall_str = custom_mazes.walls[4]
    # wall_str = None
    # height_str = None
    primary_agent = '0'
    agents = {}
    agents[primary_agent] = rodent.Rat(name="agent0")
    agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
    agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8*scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
    agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8*scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=100000)
    agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8*scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)
    agents['6'] = jumping_ball.RollingBall(name="ball6", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=10)
    agents['7'] = jumping_ball.RollingBall(name="ball7", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=10)
    agents['8'] = jumping_ball.RollingBall(name="ball8", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=10)
    agents['9'] = jumping_ball.RollingBall(name="ball9", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=10)
    agents['A'] = jumping_ball.RollingBall(name="ballA", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=1)
    agents['a'] = jumping_ball.RollingBall(name="balla", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=1)
    agents['b'] = jumping_ball.RollingBall(name="ballb", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=1)
    agents['c'] = jumping_ball.RollingBall(name="ballc", size=0.3*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=1)
    agents['d'] = jumping_ball.RollingBall(name="balld", size=0.5*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=1)
    agents['$'] = jumping_ball.RollingBall(name="ball$", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1., 0, 0], mass=1)

    arena, task = templates.maze_goal_template(maze_str, var_str, agents, primary_agent, scale, height_str, wall_str,
                                               aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True)
    env = composer.Environment(time_limit=100,
                                task=task,
                                random_state=np.random.RandomState(12345),
                                strip_singleton_obs_buffer_dim=True)
    env.reset()
    env.policies = {'ball2': functools.partial(pol.line, scale=0.5),
                    'ball3': functools.partial(pol.line, scale=1),
                    'ball4': functools.partial(pol.still, scale=1),
                    'ball5': functools.partial(pol.circle_periodic, scale=1),
                    'ball6': functools.partial(pol.circle_periodic, scale=2),
                    'ball7': functools.partial(pol.circle_periodic, scale=2),
                    'ball8': functools.partial(pol.line, scale=2),
                    'ball9': functools.partial(pol.line_periodic, scale=2),
                    'ballA': functools.partial(pol.line_periodic, scale=2),
                    'balla': functools.partial(pol.line_periodic, scale=2),
                    'ballb': functools.partial(pol.line_periodic, scale=2),
                    'ballc': functools.partial(pol.line_periodic, scale=2),
                    'balld': functools.partial(pol.circle_periodic, scale=2),
                    'ball$': functools.partial(pol.line_periodic, scale=2),

                    }
    # env.policies = functools.partial(pol.circle_periodic, scale=1)

    return env

# @SUITE.add('benchmarking')
# def mazemultiagentInteract2(environment_kwargs):
#     scale = 0.1
#     m, v, h, w = custom_mazes.get_custom_maze(id=5)
#     primary_agent = '0'
#     agents = {}
#     agents[primary_agent] = rodent.Rat(name="agent0")
#     agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
#     agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8*scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
#     agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8*scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
#     agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8*scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)
#
#     # reward_args = {'goal': 'velocity', 'xvel': 3.0}
#     arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w,
#                                                aliveness_reward=0.01, aliveness_thresh=-1.1, continuous_aliveness=True,
#                                                accel_cost_scale=50.0, vel_cost_scale=0.0)
#     env = composer.Environment(time_limit=100, task=task,
#                                random_state=np.random.RandomState(12345),
#                                strip_singleton_obs_buffer_dim=True)
#     env.reset()
#     env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
#                     'ball3': functools.partial(pol.circle_periodic, scale=1),
#                     'ball4': functools.partial(pol.still, scale=1),
#                     'ball5': functools.partial(pol.random, scale=0.5),
#                     }
#     return env

@SUITE.add('benchmarking')
def mazemultiagentInteract2(environment_kwargs):
    scale = 0.1
    agent = rodent.Rat(name="agent0")
    env = playgrounds.mazemultiagentInteract2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract3(environment_kwargs):
    scale = 0.1
    agent = rodent.Rat(name="agent0")
    env = playgrounds.mazemultiagentInteract3(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def mazemultiagentSteps1(environment_kwargs):
  scale = 0.1
  agent = rodent.Rat(name="agent0")
  env = playgrounds.mazemultiagentSteps1(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15(environment_kwargs):
  scale = 0.1
  agent = rodent.Rat(name="agent0")
  env = playgrounds.mazemultiagentInteract15(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel(environment_kwargs):
  scale = 0.1
  agent = rodent.Rat(name="agent0")
  env = playgrounds.mazemultiagentInteract19_7_novel(agent, scale, environment_kwargs)
  return env


# Ideas:
# 1) T-Maze where colors guide you through it
# 2) Ball sliding back and forth in front of a door
# 3) Recognizing that it has to go around a wall (wall vs non wall)
# 4) Climb over stuff

@SUITE.add('benchmarking')
def multiagent_novel_objects(environment_kwargs):
    scale = 0.03
    agent = rodent.Rat(name="agent0")
    env = playgrounds.multiagent_novel_objects(agent, scale, environment_kwargs, include_tracker=False)
    return env

@SUITE.add('benchmarking')
def multiagent_labyrinth(environment_kwargs):
    scale = 0.1
    agent = rodent.Rat(name="agent0")
    env = playgrounds.multiagent_labyrinth(agent, scale, environment_kwargs, include_tracker=False)
    return env