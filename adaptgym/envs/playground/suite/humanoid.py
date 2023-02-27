import functools
import numpy as np
import matplotlib.pyplot as plt

from dm_control.composer.variation import distributions

from dm_control.utils import containers
from dm_control import composer

# Run through corridor example
# from dm_control.locomotion.walkers import cmu_humanoid

from dm_control.locomotion.tasks import corridors as corr_tasks

from adaptgym.envs.playground.arenas import corridors as corr_arenas
from adaptgym.envs.playground.walkers import jumping_ball
from adaptgym.envs.playground.walkers import cmu_humanoid

from adaptgym.envs.playground.tasks import templates
import adaptgym.envs.playground.policies.policies as pol
from adaptgym.envs.playground.tasks import custom_mazes


_CONTROL_TIMESTEP = .02
_PHYSICS_TIMESTEP = 0.001

SUITE = containers.TaggedTasks()

@SUITE.add('benchmarking')
def empty(environment_kwargs=None):
    if not environment_kwargs:
        aesthetic = 'default'
    else:
        aesthetic = environment_kwargs['aesthetic']

    walker = cmu_humanoid.CMUHumanoidPositionControlledV2020(
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
    for camera_id in range(3):
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

    walker = cmu_humanoid.CMUHumanoidPositionControlledV2020(
        observable_options={'egocentric_camera': dict(enabled=True)})

    arena = corr_arenas.GapsCorridor(
        platform_length=distributions.Uniform(1, 2),
        gap_length=distributions.Uniform(1, 2),
        corridor_width=4,
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
def walls(environment_kwargs=None):
    if not environment_kwargs:
        aesthetic = 'default'
    else:
        aesthetic = environment_kwargs['aesthetic']

    walker = cmu_humanoid.CMUHumanoidPositionControlledV2020(
        observable_options={'egocentric_camera': dict(enabled=True)})

    arena = corr_arenas.WallsCorridor(
        wall_gap=3.,
        wall_width=distributions.Uniform(3., 3.5),
        # wall_height=distributions.Uniform(2.5, 3.5),
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
def mazemultiagentInteract1(environment_kwargs):
    print('---> Using mazemultiagent3.')
    scale = 0.5
    maze_str = custom_mazes.mazes[4]
    var_str = custom_mazes.vars[4]
    height_str = custom_mazes.heights[4]
    wall_str = custom_mazes.walls[4]
    # wall_str = None
    # height_str = None
    primary_agent = '0'
    agents = {}
    agents[primary_agent] = cmu_humanoid.CMUHumanoidPositionControlledV2020(
        observable_options={'egocentric_camera': dict(enabled=True)})
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

    arena, task = templates.maze_goal_template(maze_str, var_str, agents, primary_agent, scale, height_str, wall_str)
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

@SUITE.add('benchmarking')
def mazemultiagentInteract2(environment_kwargs):
    scale = 0.5
    m, v, h, w = custom_mazes.get_custom_maze(id=5)
    primary_agent = '0'
    agents = {}
    agents[primary_agent] = cmu_humanoid.CMUHumanoidPositionControlledV2020(
        observable_options={'egocentric_camera': dict(enabled=True)})
    agents['2'] = jumping_ball.RollingBall(name="ball2", size=0.8*scale, rgb1=[1.0, 0, 0], rgb2=[1.0, .5, .1], mass=20)
    agents['3'] = jumping_ball.RollingBall(name="ball3", size=0.8*scale, rgb1=[0, 1., 0], rgb2=[1.0, 0, 0], mass=20)
    agents['4'] = jumping_ball.RollingBall(name="ball4", size=0.8*scale, rgb1=[0, 0, 1.], rgb2=[0, 1., 0], mass=1)
    agents['5'] = jumping_ball.RollingBall(name="ball5", size=0.8*scale, rgb1=[1.0, .5, .1], rgb2=[0, 0, 1.], mass=20)

    # reward_args = {'goal': 'velocity', 'xvel': 3.0}
    arena, task = templates.maze_goal_template(m, v, agents, primary_agent, scale, h, w,
                                               aliveness_reward=0.00, aliveness_thresh=-1.1, continuous_aliveness=True,
                                               accel_cost_scale=50.0, vel_cost_scale=0.0)
    env = composer.Environment(time_limit=100, task=task,
                               random_state=np.random.RandomState(12345),
                               strip_singleton_obs_buffer_dim=True)
    env.reset()
    env.policies = {'ball2': functools.partial(pol.line_periodic, scale=0.5, period=200),
                    'ball3': functools.partial(pol.circle_periodic, scale=1),
                    'ball4': functools.partial(pol.still, scale=1),
                    'ball5': functools.partial(pol.random, scale=0.5),
                    }
    return env

