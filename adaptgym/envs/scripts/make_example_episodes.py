"""
Generate example episodes.
"""
import os
import common
import numpy as np
import elements
import collections
import datetime
import pathlib
from dreamerv2 import agent
import common.envs

from moviepy.editor import ImageSequenceClip

examples = {
  # 0: {'env_name': 'admc_sphero_mazemultiagentInteract15_example_8', 'action': [(-1, 0)]},
  1: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b3', 'action': [(-1, 0)]},
  2: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b4', 'action': [(-1, 0)]},
  3: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b3_2', 'action': [(-1, 0)]},
  4: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b4_2', 'action': [(-1, 0)]},
}

examples = {
  # 0: {'env_name': 'admc_sphero_mazemultiagentInteract15_example_8', 'action': [(-1, 0)]},
  1: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b3_black', 'action': [(-1, 0)]},
  2: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b4_black', 'action': [(-1, 0)]},
  3: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b3_2_black', 'action': [(-1, 0)]},
  4: {'env_name': 'admc_sphero_mazemultiagentInteract19_7_novel_example_b4_2_black', 'action': [(-1, 0)]},
}

examples = {
  # 0: {'env_name': 'admc_sphero_mazemultiagentInteract15_example_8', 'action': [(-1, 0)]},
  1: {'env_name': 'admc_sphero_object_example1_magenta', 'action': [(-1, 0)]},
  2: {'env_name': 'admc_sphero_object_example1_yellow', 'action': [(-1, 0)]},
  3: {'env_name': 'admc_sphero_object_example1_white', 'action': [(-1, 0)]},
  4: {'env_name': 'admc_sphero_object_example1_empty', 'action': [(-1, 0)]},
}


if __name__ == "__main__":
  for which_example in [1,2,3,4]:
    print(which_example)
    home = os.path.expanduser("~")
    logdir = pathlib.PosixPath(f'{home}/logs/EXAMPLE_EPS/')
    # logdir = pathlib.PosixPath(f'{home}/logs/GEN-EXAMPLE_EPS_black/')
    os.makedirs(logdir, exist_ok=True)
    gifdir = logdir / 'gifs'
    os.makedirs(gifdir, exist_ok=True)

    env_name = examples[which_example]['env_name']
    action = examples[which_example]['action']
    config = {
      'action_repeat': 2,
      'image_size': [64, 64],
      'aesthetic': 'default',
      'egocentric_camera': True,
      'num_envs': 1,
      'time_limit': 120,
      'replay_size': 5e5,
      'control_timestep': 0.03,
      'physics_timestep': 0.005,
      'reset_position_freq': 0,
    }
    config = elements.Config(config)

    env_index = 0
    logging_params = {'logger': None, 'grid_density': 20, 'episode_length': None,
                      'record_every_k_timesteps': 20, 'episodes_for_summary_metrics': 20,
                      'logdir': logdir}
    train_logging_params = logging_params.copy()
    train_logging_params['env_raw_output_file_name'] = f'log_train_env{env_index}.csv'

    replay = common.Replay(logdir / f'train_replay_0', config.replay_size)

    # Define actions
    envs = [common.envs.make_env(config, env_name, train_logging_params) for _ in range(config.num_envs)]
    action_space = envs[0].action_space['action']
    driver = common.Driver(envs, logdir=logdir)

    step = elements.Counter(0)
    driver.on_step(lambda _: step.increment())
    driver.on_episode(lambda ep: replay.add(ep))
    driver.reset()
    policy = lambda x, y:  ({'action': action}, y)
    driver(policy, episodes=1)


    # Make a gif
    eps = list(replay._episodes.keys())
    eps.sort()
    path = eps[-1]
    ep = np.load(path)
    imgs = ep['image']

    clip = ImageSequenceClip(list(imgs), fps=20)
    clip.write_gif(f'{gifdir}/{which_example}.gif', fps=20)

  print('done')