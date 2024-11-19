from evironment2 import initialize_environment, update_uav_position
from uav_dynamics1 import calculate_velocity
from reward_function1 import calculate_reward
from action_selection1 import epsilon_greedy, update_Q
from visualization1 import visualize_path

import numpy as np

# Step 1: Initialize environment
uav_pos, goal_pos, obstacles = initialize_environment()
print(f"UAV Position: {uav_pos}, Goal Position: {goal_pos}, Obstacles: {obstacles}")

# Initialize parameters
current_velocity = (0, 0, 0)  # Initial velocity
max_speed = 2.0               # Maximum speed
Q_values = [0, 0, 0, 0, 0, 0]  # Initialize Q-values for 6 actions
epsilon = 0.1                 # Exploration probability for epsilon-greedy
alpha = 0.1                   # Learning rate
gamma = 0.9                   # Discount factor
tau = 1.0                     # Temperature for softmax
safe_zone = 3.0               # Safe zone distance
collision_zone = 1.5          # Collision zone distance
mandatory_zone = 0.5          # Mandatory zone distance

# Initialize path and rewards for visualization
uav_path = [uav_pos]
rewards = []

# Simulate multiple steps
for step in range(10):  # Simulate 10 steps
    print(f"\nStep {step + 1}:")
    
    # Step 2: Select action using epsilon-greedy
    action = epsilon_greedy(Q_values, epsilon)
    print(f"Selected Action (Epsilon-Greedy): {action}")
    
    # Update UAV dynamics (position and velocity)
    current_velocity = calculate_velocity(current_velocity, action, max_speed)
    uav_pos = update_uav_position(uav_pos, action)
    uav_path.append(uav_pos)

    # Step 3: Calculate reward
    reward = 0
    for obstacle in obstacles:  # Handle multiple obstacles
        reward += calculate_reward(uav_pos, goal_pos, obstacle, safe_zone, collision_zone, mandatory_zone)
    rewards.append(reward)
    print(f"Reward Received: {reward}")

    # Step 4: Update Q-values
    Q_values = update_Q(Q_values, action, reward, alpha, gamma)
    print(f"Updated Q-values: {Q_values}")

# Step 5: Visualize path and rewards
visualize_path(uav_path, rewards)
