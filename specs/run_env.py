import gym

if __name__ == '__main__':
    env = gym.make('dmc:Humanoid-run-v1')
    print(env.observation_space, env.action_space)
    obs, info = env.reset()
    done = False
    time_steps = 0
    while not done:
        time_steps += 1
        obs, rew, terminate, truncate, info = env.step(env.action_space.sample())
        done = terminate or truncate
    print(time_steps)
