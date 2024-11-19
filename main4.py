from evironment2 import initialize_environment, update_uav_position
from uav_dynamics1 import calculate_velocity
from reward_function2 import calculate_reward
from action_selection2 import epsilon_greedy, update_Q
from visualization4 import visualize_path

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
D_cz = 5                      # Critical zone distance
D_max = 10                    # Maximum effective obstacle avoidance distance
d_max = 20                    # Maximum distance to the goal

# Initialize path and rewards for visualization
uav_path = [uav_pos]
rewards = []
reward_details = []  # To store Ra, Rcz, and Rmz for debugging

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
    total_reward = 0
    step_reward_details = {"Ra": 0, "Rcz": 0, "Rmz": 0}
    for obstacle in obstacles:  # Handle multiple obstacles
        R, Ra, Rcz, Rmz = calculate_reward(uav_pos, goal_pos, obstacle, D_cz, D_max, d_max)
        total_reward += R
        step_reward_details["Ra"] += Ra
        step_reward_details["Rcz"] += Rcz
        step_reward_details["Rmz"] += Rmz
    rewards.append(total_reward)
    reward_details.append(step_reward_details)
    print(f"Reward Received: {total_reward}")
    print(f"Step Reward Details: {step_reward_details}")

    # Step 4: Update Q-values
    Q_values = update_Q(Q_values, action, total_reward, alpha, gamma)
    print(f"Updated Q-values: {Q_values}")

# Step 5: Visualize path and rewards
visualize_path(uav_path, rewards, obstacles)
