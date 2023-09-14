import functools
import numpy as np
import matplotlib.pyplot as plt

from dm_control.composer.variation import distributions

from dm_control.utils import containers
from dm_control import composer

from adaptgym.envs.playground.walkers import jumping_ball
from adaptgym.envs.playground.walkers import rodent

from adaptgym.envs.playground.tasks import templates
import adaptgym.envs.playground.policies.policies as pol
from adaptgym.envs.playground.tasks import custom_mazes
from adaptgym.envs.playground.tasks import playgrounds
from adaptgym.envs.playground.exploration_tracker import ExplorationTracker


# _CONTROL_TIMESTEP = .02
# _PHYSICS_TIMESTEP = 0.001

SUITE = containers.TaggedTasks()


@SUITE.add('benchmarking')
def novel_object(environment_kwargs):
    # same as multiagent_novel_objects_step1step2_single_magenta()
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2_single_magenta(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def novel_object_unchanging(environment_kwargs):
    # same as multiagent_novel_objects_step2_single_magenta()
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2_single_magenta(agent, scale, environment_kwargs)
    return env


########################################################################################################
############## BELOW ARE TEST/EXPLORATION PLAYGROUNDS ##################################################
########################################################################################################


@SUITE.add('benchmarking')
def mazemultiagentInteract3(environment_kwargs):
    scale = 0.1
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract3(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract4(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract4(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract5(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract5(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def mazemultiagentInteract6(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract6(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract7(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract7(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract8(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract8(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract9(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract9(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract9_1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract9_1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract9_2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract9_2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract9_3(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract9_3(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract10(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract10(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract10_2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract10_2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract11(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract11(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract12(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract12(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def mazemultiagentInteract13(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract13(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract14(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract14(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_3(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_3(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_4(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_4(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_5(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_5(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_6(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_6(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_7(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_7(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract15_example_8(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract15_example_8(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract16(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract16(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def mazemultiagentInteract17(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentInteract17(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentInteract17_1(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract17_1(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract18(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract18(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_1_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_1_play(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_2_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_2_play(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_3_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_3_play(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_4_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_4_play(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_5_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_5_play(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_6_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_6_play(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_6_2_play(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_6_2_play(agent, scale, environment_kwargs)
  return env


@SUITE.add('benchmarking')
def mazemultiagentInteract19_1_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_1_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_5_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_5_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_6_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_6_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball3(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball3(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball4(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball4(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball4_reset(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball4_reset(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball4_reset_white(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball4_reset_white(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball4_reset_black(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball4_reset_black(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball4_reset_gray(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball4_reset_gray(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_play_ball4_setposition(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_play_ball4_setposition(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b3(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b3(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b4(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b4(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b3_2(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b3_2(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b4_2(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b4_2(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b3_black(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b3_black(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b4_black(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b4_black(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b3_2_black(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b3_2(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_7_novel_example_b4_2_black(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_7_novel_example_b4_2_black(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_8_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_8_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_8_novel_b3(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_8_novel_b3(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_8_novel_b4(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_8_novel_b4(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_9_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_9_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_9_novel_b3(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_9_novel_b3(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_9_novel_b4(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_9_novel_b4(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_10_novel(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_10_novel(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_10_play_b3(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_10_play_b3(agent, scale, environment_kwargs)
  return env

@SUITE.add('benchmarking')
def mazemultiagentInteract19_10_play_b4(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract19_10_play_b4(agent, scale, environment_kwargs)
  return env


@SUITE.add('benchmarking')
def mazemultiagentInteract20_tv(environment_kwargs):
  scale = 0.7
  agent = jumping_ball.RollingBall(name="agent0", size=0.8 * scale,
                                   rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
  env = playgrounds.mazemultiagentInteract20_tv(agent, scale, environment_kwargs)
  return env


@SUITE.add('benchmarking')
def mazemultiagentVelocity1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentVelocity1(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def mazemultiagentVelocity2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentVelocity2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentPosition1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentPosition1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentPosition2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentPosition2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentDoors1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentDoors1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentDoors1a(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentDoors1a(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentDoors2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentDoors2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentDoors2a(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentDoors2a(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentSteps1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentSteps1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentSteps2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentSteps2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentSteps3(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentSteps3(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentSteps4(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentSteps4(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentSteps5(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentSteps5(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentEmpty0(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentEmpty0(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentExplore1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentExplore1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentExplore2(environment_kwargs):
    scale = 1
    agent = jumping_ball.RollingBall(name="agent0", size=0.5*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentExplore2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def mazemultiagentExplore3(environment_kwargs):
    scale = 1
    agent = jumping_ball.RollingBall(name="agent0", size=0.5*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.mazemultiagentExplore3(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_dynamics_train(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_dynamics_train(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_dynamics_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_dynamics_test(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def multiagent_corridor_train(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_corridor_train(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def multiagent_corridor_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_corridor_test(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def multiagent_violation1_train(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_violation1_train(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def multiagent_violation1_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_violation1_test(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def multiagent_violation2_train(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_violation2_train(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def multiagent_violation2_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_violation2_test(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_colorchange_train(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_colorchange_train(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def multiagent_colorchange_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_colorchange_test(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_colorchange_random(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_colorchange_random(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_colorchange_multi(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_colorchange_multi(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def multiagent_colorchange_collision(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_colorchange_collision(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_object_appear(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_object_appear(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def multiagent_massdiff_train(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_massdiff_train(agent, scale, environment_kwargs)
    return env



@SUITE.add('benchmarking')
def multiagent_massdiff_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_massdiff_test(agent, scale, environment_kwargs)
    return env


##########################################################################################
@SUITE.add('benchmarking')
def multiagent_homecage(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_homecage(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_single_object(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_single_object(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_black(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_black(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_simple_black(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_simple_black(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_simple500_black(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_simple500_black(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def multiagent_novel_objects_step1(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step1_obj(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1_obj(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step2_reset(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2_reset(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step2_inf(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2_inf(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step2_long(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2_long(agent, scale, environment_kwargs)
    return env


@SUITE.add('benchmarking')
def multiagent_novel_objects_step2_single_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step2_single_magenta(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step1step2_single_magenta(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2_single_magenta(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step1step2_single_magenta_debug3e4(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2_single_magenta_debug3e4(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step1step2_single_magenta_debug1e4(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2_single_magenta_debug1e4(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_step1step2(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_step1step2(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_novel_objects_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_novel_objects_test(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_labyrinth(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_labyrinth(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_labyrinth_black(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_labyrinth_black(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_openfield(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_openfield(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_flashing_object(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_flashing_object(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_flashing_objects(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_flashing_objects(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_interactive_flashing_object(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_interactive_flashing_object(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_interactive_flashing_object_test(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_interactive_flashing_object_test(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_sparse_goal(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_sparse_goal(agent, scale, environment_kwargs)
    return env

@SUITE.add('benchmarking')
def multiagent_dense_goal(environment_kwargs):
    scale = 0.7
    agent = jumping_ball.RollingBall(name="agent0", size=0.8*scale,
                                     rgb1=[1.0, 1.0, 1.0], rgb2=[0.0, 0.0, 0.0], mass=20)
    env = playgrounds.multiagent_dense_goal(agent, scale, environment_kwargs)
    return env

