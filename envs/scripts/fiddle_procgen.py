import gym
import matplotlib.pyplot as plt


if __name__ == "__main__":
    env = gym.make("procgen:procgen-maze-v0",
                   num_levels=3, start_level=0,
                   distribution_mode='easy',
                   use_sequential_levels=True,
                   restrict_themes=True,
                   )
    obs = env.reset()
    prev_obs = obs
    for i in range(10):
        plt.imshow(obs)
        plt.title(i)
        plt.show()
        # obs, rew, done, info = env.step(env.action_space.sample())
        while True:
            obs, rew, done, info = env.step(env.action_space.sample())
            # plt.imshow(obs)
            # plt.show()
            # env.render()
            if done:
                plt.imshow(prev_obs)
                plt.title(f'{i}:{rew}')
                plt.show()
                break
            prev_obs = obs
    print('done')
