# Introduction to Reinforcement Learning with Lunar Lander

Reinforcement Learning (RL) is a fascinating subset of machine learning where an agent learns to make optimal decisions by interacting with its environment to maximize cumulative rewards. Imagine training a dog to perform tricks: each time the dog successfully performs a trick, you reward it with a treat. Over time, the dog learns to associate the trick with the reward and performs it more frequently. This simple yet powerful concept is the foundation of reinforcement learning.

In this tutorial, we will embark on an exciting journey to teach an AI agent how to land on the moon. We will achieve this by setting up an environment using Stable Baselines 3 and OpenAI Gymnasium to run the Lunar Lander simulation. Along the way, we will delve into essential RL concepts such as action space, observation space, and the Proximal Policy Optimization (PPO) algorithm.

![alt text](lunar_lander_intro.gif)

## Setting Up the Environment

To get started, you need to install the necessary libraries. You can do this using pip:

```bash
pip install stable-baselines3 gymnasium
```

## Understanding the Lunar Lander Environment

The Lunar Lander environment is a classic control problem where the goal is to land a lunar module safely on the moon's surface. The environment provides a simulation where the agent (the lunar module) can perform actions to control its movement.

### Action Space

The action space defines the set of all possible actions that the agent can take at any given time. In the Lunar Lander environment, the action space is discrete with four possible actions:

1. Do nothing
2. Fire left orientation engine
3. Fire main engine
4. Fire right orientation engine