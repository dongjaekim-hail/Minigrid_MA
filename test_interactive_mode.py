#!/usr/bin/env python3

import random
import time

import gym

# Load the gym environment
env = gym.make("MiniGrid-Empty-8x8-v0", new_step_api=True)
env.reset()

for i in range(0, 100):
    print(f"step {i}")

    # Pick a random action
    action = random.randint(0, env.action_space.n - 1)

    obs, reward, terminated, truncated, info = env.step(action)

    env.render()

    time.sleep(0.05)

# Test the close method
env.close()
