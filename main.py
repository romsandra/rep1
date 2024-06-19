import gymnasium as gym
import numpy as np
import csv

#env = gym.make("LunarLander-v2", render_mode="human")  # Отключили визуализацию для сбора данных
env = gym.make("LunarLander-v2", render_mode="rgb_array")
   

observation, info = env.reset(seed=42)

# Создаем CSV файл для сохранения данных
with open("imitation_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Observation", "Action"])  # Записываем заголовок столбцов
    for _ in range(1000):
        # Выберите действие. 
        # В данном случае используется случайное действие (env.action_space.sample())
        # Замените это на ваше управление или обученный алгоритм
        action = env.action_space.sample()  

        # Выполните шаг в среде
        observation, reward, terminated, truncated, info = env.step(action)

        # Сохраняем состояние и действие в CSV файл
        writer.writerow([observation.flatten(), action])

        # Если эпизод завершен, перезапустите среду
        if terminated or truncated:
            observation, info = env.reset()

env.close()
