import argparse
import os
from datetime import datetime

import imageio
import numpy as np
import matplotlib.pyplot as plt
import time

from dm_control import viewer

import cv2

def main():
    name = 'cdmc_cheetah_run'
    name = 'cdmc_cartpole_swingup_sparse'
    name = 'ddmc_walker_walk'
    name = 'admc_sphero_multiagent_novel_objects_step2_single_magenta'
    name = 'admc_sphero_novel_object'
    name = 'admc_sphero_novel_object_unchanging'
    name = 'admc_sphero_novel_object_2ball_debug'
    name = 'admc_sphero_novel_object_2ball_reverse_debug'
    name = 'admc_sphero_object_example8_magenta'
    name = 'admc_sphero_labyrinth_black_example'
    name = 'admc_sphero_distal_column2'
    # name = 'admc_rodent_multiagent_novel_objects_step2_single_magenta'
    envname, taskname = name.split('_', 1)

    from adaptgym import wrapped
    if envname == 'cdmc':
      env = wrapped.CDMC(taskname)
    elif envname == 'ddmc':
      env = wrapped.DDMC(taskname)
    elif envname == 'admc':
      env = wrapped.ADMC(taskname, wide_fov=False)

    mode = 'gif'
    mode = 'display'
    # mode = 'interactive'
    if mode == 'display':
        display(env, num_frames=200)
    elif mode == 'gif':
        gif(env, num_frames=200)
    elif mode == 'interactive':
        interactive(env, envname)


def interactive(env, envname, do_random=True, n_wrappers=0):
    if envname == 'admc':
        n_wrappers += 1
    for i in range(n_wrappers+1):
        env = env._env
    action_spec = env.action_spec()
    if do_random:
        def policy(time_step):
            del time_step  # Unused.
            return np.random.uniform(low=action_spec.minimum,
                                     high=action_spec.maximum,
                                     size=action_spec.shape)
    else:
        def policy(time_step):
            del time_step
            action = np.zeros(action_spec.shape)
            # action[0] = 0.01
            return action

    # Launch the viewer GUI application.
    viewer.launch(env, policy=policy)


def gif(env, num_ep=3, num_frames=3000):
    env.reset()
    acts = env.action_space
    for j in range(num_ep):
        for i in range(num_frames):
            action = acts.sample()
            results = [env.step(action)]
            # obs, _, done = zip(*[p[:3] for p in results])
            # obs = list(obs)
            # img = obs[0]['image']
            img = results[0]['image']
            plt.imshow(img), plt.savefig(f'{i}.png')
            # if done[0]: # Assumes a single environment
            if results[0]['is_last']:  # Assumes a single environment
                break

        images = []
        for filename in [f'{i}.png' for i in range(num_frames)]:
            images.append(imageio.imread(filename))
            os.remove(filename)
        imageio.mimsave(f'{j}.gif', images, duration=0.1)

        # Reset
        env.reset()


def display(env, num_ep=3, num_frames=3000):
    env.reset()
    acts = env.action_space

    for j in range(num_ep):
        for i in range(num_frames):
            # action = np.random.uniform(acts.minimum, acts.maximum, acts.shape)
            action = acts.sample()
            results = [env.step(action)]
            # obs, _, done = zip(*[p[:3] for p in results])
            # obs = list(obs)
            # img = obs[0]['image']
            img = results[0]['image']
            resized = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)
            resized = np.flip(resized, axis=2)
            img = resized.astype('uint8')
            do_overlay_text = True
            if do_overlay_text:
                img = cv2.putText(resized.astype('uint8'), f'ep {j}, step {i}',
                                  (50, 330),
                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                  fontScale=1,
                                  color=(255, 255, 255),
                                  thickness=3,
                                  lineType=2)

            cv2.imshow('image', img)
            cv2.waitKey(10)
            # if done[0]:  # Assumes a single environment
            if results[0]['is_last']:  # Assumes a single environment
                break
        # Reset
        env.reset()


if __name__ == "__main__":
    main()