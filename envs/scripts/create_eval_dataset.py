import argparse
import os
from datetime import datetime

import imageio
import numpy as np
import matplotlib.pyplot as plt
import time

from dm_control import viewer
import common.envs
import training.utils.loading_utils as lu
import elements
from os.path import expanduser
import tensorflow as tf
from training.utils.diagnosis_utils import convert_matplotlib_fig_to_array, get_discounted_rewards
from dreamerv2.utils import parse_flags

from common.replay import save_episodes
import pathlib
physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)
tf.config.run_functions_eagerly(True)

def convert(value):
    value = np.array(value)
    if np.issubdtype(value.dtype, np.floating):
        return value.astype(np.float32)
    elif np.issubdtype(value.dtype, np.signedinteger):
        return value.astype(np.int32)
    elif np.issubdtype(value.dtype, np.uint8):
        return value.astype(np.uint8)
    return value



def fiddle_with_env(config, num_frames=100, get_fps=False):


    task = 'admc_sphero_multiagent_dynamics_test'
    expid = 'GEN-dynamics-1-deep-test-noreset'
    checkpoint_name = 'variables_test_agent_envindex1_000010000.pkl'
    # bufferid = 'GEN-FIXED_ACTION'
    # expid = 'GEN-3-1-test'  # 'GEN-1039-test'
    # checkpoint_name = 'variables_test_agent_envindex1_000100000.pkl'
    # log_names = ['towards_novel', 'towards_familiar']
    # angle_offsets = [ np.pi/4.5, -np.pi/6]
    # task = 'admc_sphero_multiagent_colorchange_test'

    config = config.update(task=task)

    home = expanduser("~")
    datadir = f"{home}/gendreamer/envs/data/{task}"

    os.makedirs(datadir, exist_ok=True)


    # outputs = [
    #     elements.TensorBoardOutput(datadir),
    # ]
    # logger = elements.Logger(elements.Counter(0), outputs, multiplier=config.action_repeat)

    # for angle_offset, log_name in zip(angle_offsets, log_names):
        # env = common.envs.make_env(config, config.task, env_params={'randomize_spawn_rotation':False,
        #                                                           'spawn_rotation_radians':{'0':3*np.pi/2 + angle_offset}})
    if False:
        target = 'novel'

        env = common.envs.make_env(config, config.task, env_params={'randomize_spawn_position': True})
        env.reset()

        def take_action(time_step):

            physics = env._env._env._env._env._env.physics
            target_pos =  physics.bind( env._env._env._env._env._env._task._walkers['2'].root_body).xpos
            curr_pos = time_step.observation['absolute_position_agent0']
            dist = np.linalg.norm((target_pos - curr_pos),ord=2)
            vec = target_pos - curr_pos
            z_angle_target = -(np.pi/2 - np.arctan2(vec[1], vec[0]))
            if time_step.step_type == 0:
                z_angle_target =  np.arctan2(vec[1], vec[0]) #+np.pi/2
                quat = [np.cos(z_angle_target / 2), 0, 0, np.sin(z_angle_target / 2)]
                env._env._env._env._env._env._task._walkers['0'].set_pose(physics, quaternion=quat)
                return np.array([0., 0.])
            quaternion = time_step.observation['absolute_quaternion_agent0']
            z_angle_agent = np.arctan2(
                2 * (quaternion[0] * quaternion[3] + quaternion[1] * quaternion[2]),
                1 - 2 * (quaternion[2] ** 2 + quaternion[3] ** 2))


            action = np.array([-10, -1 * (z_angle_target - z_angle_agent)])#{'action':np.array([-1, -100 * (z_angle_target - z_angle_agent)])}
            return action

        viewer.launch( env._env._env._env._env._env, policy=take_action)
    else:

        env = common.envs.make_env(config, config.task,  env_params={'randomize_spawn_position': True})
        env.reset()
        def take_action(observation, env):
            physics = env._env._env._env._env._env.physics
            target_pos =  physics.bind( env._env._env._env._env._env._task._walkers['2'].root_body).xpos
            curr_pos = observation['absolute_position_agent0']
            vec = target_pos - curr_pos
            z_angle_target = -(np.pi/2 - np.arctan2(vec[1], vec[0]))

            quaternion = observation['absolute_quaternion_agent0']
            z_angle_agent = np.arctan2(
                2 * (quaternion[0] * quaternion[3] + quaternion[1] * quaternion[2]),
                1 - 2 * (quaternion[2] ** 2 + quaternion[3] ** 2))


            action = {'action':np.array([-10, -1 * (z_angle_target - z_angle_agent)])}
            return action
        action = {'action': np.array([0., 0.])}
        ep = []
        all_ep = []
        for i in range(num_frames):

            if i % 100 == 0 and i > 0:
                plt.imshow(ob['image']); plt.show()
                print(f'Step {i+1}/{num_frames}')
            ob, rew, done, info = env.step(action)
            if i == 0:
                physics = env._env._env._env._env._env.physics
                target_pos = physics.bind(env._env._env._env._env._env._task._walkers['2'].root_body).xpos
                curr_pos = ob['absolute_position_agent0']
                vec = target_pos - curr_pos
                z_angle_target =  np.arctan2(vec[1], vec[0])
                quat = [np.cos(z_angle_target / 2), 0, 0, np.sin(z_angle_target / 2)]
                env._env._env._env._env._env._task._walkers['0'].set_pose(physics, quaternion=quat)
            action = take_action(ob, env)
            disc = ob.get('discount', 1 - float(done))
            tran = {**ob, **action, 'reward': rew, 'discount': disc, 'done': done}
            ep.append(tran)
            if (i+1) % 50 == 0 or done:
                all_ep.append({k: convert([t[k] for t in ep]) for k in ep[0]})
                ep = []
                env.reset()
                action = {'action': np.array([0., 0.])}

                physics = env._env._env._env._env._env.physics
                target_pos = physics.bind(env._env._env._env._env._env._task._walkers['2'].root_body).xpos
                curr_pos = ob['absolute_position_agent0']
                vec = target_pos - curr_pos
                z_angle_target =  np.arctan2(vec[1], vec[0])
                quat = [np.cos(z_angle_target / 2), 0, 0, np.sin(z_angle_target / 2)]
                env._env._env._env._env._env._task._walkers['0'].set_pose(physics, quaternion=quat)

        # data = {k: convert([t[k] for t in ep]) for k in ep[0]}
        # data = {key: tf.cast(data[key], dtype=data[key].dtype) for key in data.keys()}
        save_episodes(datadir, all_ep)
        print('done.')
        #
        # '''evaluate wm'''
        # basedir = f"{home}/gendreamer/logs/{expid}"
        #
        # plot_dir = f'{basedir}/model_loss_plots'
        # os.makedirs(plot_dir, exist_ok=True)
        #
        # from tensorflow.keras.mixed_precision import experimental as prec
        #
        # prec.set_policy(prec.Policy('mixed_float16'))
        #
        # ## Load agent from checkpoint
        # agnt = lu.load_agent(basedir,
        #                      checkpoint_name=checkpoint_name,
        #                      batch_size=5,
        #                      deterministic=False
        #                      )
        #
        # model_loss, state, outputs, mets = agnt.wm.loss(data, None)
        # logger.scalar(f'model_loss/{checkpoint_name}', mets['image_loss'])
        #
        # logger.write()

def visualize_episodes():
    task = 'admc_sphero_multiagent_colorchange_test'
    home = expanduser("~")
    directory = f"{home}/gendreamer/envs/data/{task}"
    outputs = [
        elements.TensorBoardOutput(directory),
    ]
    logger = elements.Logger(elements.Counter(0), outputs, multiplier=2)

    directory = pathlib.Path(directory).expanduser()
    cnt = 0
    for filename in reversed(sorted(directory.glob('*.npz'))):
        with filename.open('rb') as f:
            episode = np.load(f, allow_pickle=True)
            episode = {k: episode[k] for k in episode.keys()}
            logger.add({str(filename): tf.constant(episode['image'])})
            logger.write(fps=True)
        cnt += 1
        if cnt == 20:
            break
def main():
    parser = argparse.ArgumentParser(description='Specify training arguments.')
    parser.add_argument('--logdir', dest='logdir', default='/dev/null',
                        help='path to logdir')
    args = parser.parse_args()

    flags = [
        '--configs', 'defaults', 'dmc', #'adapt',
        # '--task', 'admc_sphero_mazemultiagentInteract17',
        '--task', 'admc_sphero_multiagent_colorchange_test',
        # '--task', 'ddmc_walker_walk',
        '--egocentric_camera', 'True',
        ]
    flags.extend(['--logdir', args.logdir])

    config, logdir = parse_flags(flags)
    fiddle_with_env(config, num_frames=5000)
    # visualize_episodes()

if __name__ == "__main__":
    main()