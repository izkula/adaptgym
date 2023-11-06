from dm_control.utils import containers
from adaptgym.envs.playground.walkers import jumping_ball
from adaptgym.envs.playground.tasks import playgrounds


# _CONTROL_TIMESTEP = .02
# _PHYSICS_TIMESTEP = 0.001

SUITE = containers.TaggedTasks()


@SUITE.add('benchmarking')
def novel_object(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2_single_magenta(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def novel_object_unchanging(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2_single_magenta(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def novel_object_debug(environment_kwargs):
    """Novel object appears after only 1e4 steps of exploration in the empty arena."""
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2_single_magenta_debug1e4(agent, scale, environment_kwargs)
    return env


############################################################
##########    Experimental tasks below    ##################
############################################################

@SUITE.add('benchmarking')
def novel_object_2ball(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2step3_magenta_to_yellow(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def novel_object_2ball_reverse(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2step3_yellow_to_magenta(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def novel_object_2ball_debug(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2step3_magenta_to_yellow_debug5e2(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def novel_object_2ball_reverse_debug(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2step3_yellow_to_magenta_debug5e2(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def labyrinth_black(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_labyrinth_black(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def labyrinth_black_example(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_labyrinth_black_example(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def distal(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20,
                                     wide_fov=environment_kwargs['wide_fov'])
    env = playgrounds.multiagent_distal(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def distal_column1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20,
                                     wide_fov=environment_kwargs['wide_fov'])
    env = playgrounds.multiagent_distal_column1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def distal_column2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20,
                                     wide_fov=environment_kwargs['wide_fov'])
    env = playgrounds.multiagent_distal_column2(agent, scale, environment_kwargs)
    return env

############################################################
##########    Evaluation tasks below      ##################
############################################################

@SUITE.add('benchmarking')
def object_example1_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example1(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example1_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example1(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example1_white(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example1(agent, scale, environment_kwargs, color='white')
    return env

@SUITE.add('benchmarking')
def object_example1_empty(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example1(agent, scale, environment_kwargs, step_appear=1e8)
    return env


@SUITE.add('benchmarking')
def object_example2_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example2(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example2_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example2(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example3_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example3(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example3_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example3(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example4_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example4(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example4_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example4(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example5_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example5(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example5_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example5(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example6_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example6(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example6_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example6(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example7_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example7(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example7_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example7(agent, scale, environment_kwargs, color='yellow')
    return env

@SUITE.add('benchmarking')
def object_example8_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example8(agent, scale, environment_kwargs, color='magenta')
    return env

@SUITE.add('benchmarking')
def object_example8_yellow(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_example8(agent, scale, environment_kwargs, color='yellow')
    return env