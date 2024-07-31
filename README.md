# Introduction to Reinforcement Learning with Lunar Lander

Reinforcement Learning (RL) is a fascinating subset of machine learning where an agent learns to make optimal decisions by interacting with its environment to maximize cumulative rewards. Imagine training a dog to perform tricks: each time the dog successfully performs a trick, you reward it with a treat. Over time, the dog learns to associate the trick with the reward and performs it more frequently. This simple yet powerful concept is the foundation of reinforcement learning.

In this tutorial, we will embark on an exciting journey to teach an AI agent how to land on the moon. We will achieve this by setting up an environment using Stable Baselines 3 and OpenAI Gymnasium to run the Lunar Lander simulation. Along the way, we will delve into essential RL concepts such as action space, observation space, and the Proximal Policy Optimization (PPO) algorithm.

![alt text](Resources/lunar_lander_intro.gif)

## Setting Up the Environment

To get started, you need to install the necessary libraries. You can do this using pip:

```bash
pip install stable-baselines3 gymnasium
```

## Understanding the Lunar Lander Environment

The Lunar Lander environment is a classic control problem where the goal is to land a lunar module safely on the moon's surface. The environment provides a simulation where the agent (the lunar module) can perform actions to control its movement.

### Action Space

The action space defines the set of all possible actions that the agent can take at any given time. In the Lunar Lander environment, the action space is discrete with four possible actions:

- `0`: Do nothing<br>
- `1`: Fire left orientation engine
- `2`: Fire main engine
- `3`: Fire right orientation engine

### Observation Space

The observation space defines the set of all possible states that the environment can be in. In the Lunar Lander environment, the observation space is a continuous space consisting of 8 variables:

1. X position
2. Y position
3. X velocity
4. Y velocity
5. Angle
6. Angular velocity
7. Left leg contact
8. Right leg contact

### Reward Structure

After every step (or you can say, a frame) a reward is granted. The total reward of an episode is the sum of the rewards for all the steps within that episode.

For each step, the reward:

- is increased/decreased the closer/further the lander is to the landing pad.
- is increased/decreased the slower/faster the lander is moving.
- is decreased the more the lander is tilted (angle not horizontal).
- is increased by 10 points for each leg that is in contact with the ground.
- is decreased by 0.03 points each frame a side engine is firing.
- is decreased by 0.3 points each frame the main engine is firing.

The episode receive an additional reward of -100 or +100 points for crashing or landing safely respectively.

An episode is considered a solution if it scores at least 200 points.

### Starting State

The lander starts at the top center of the viewport with a random initial force applied to its center of mass.

### Episode Termination
The episode finishes if:

- the lander crashes (the lander body gets in contact with the moon);
- the lander gets outside of the viewport (x coordinate is greater than 1);
- the lander is not awake. A body which is not awake is a body which doesn’t move and doesn’t collide with any other body:

