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