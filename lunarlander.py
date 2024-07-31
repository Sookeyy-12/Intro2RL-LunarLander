import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("LunarLander-v2")

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10000)

model.save("ppo-lunar-lander")

model = PPO.load("ppo-lunar-lander")

episodes = 10
for episode in range(episodes):
    obs = env.reset()
    done = False
    total_reward = 0
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        total_reward += reward
        
    print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

obs = env.reset()
done = False

while not done:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()

env.close()