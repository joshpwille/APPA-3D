from evironment2 import initialize_environment, update_uav_position
from uav_dynamics1 import calculate_velocity
from reward_function1 import calculate_reward
from action_selection2 import epsilon_greedy, update_Q
from visualization1 import visualize_path

# Step 1: Initialize environment
uav_pos, goal_pos, obstacles = initialize_environment()

# Step 2: Update UAV dynamics
current_velocity = (0, 0, 0)
max_speed = 2.0
action = epsilon_greedy([0, 0, 0, 0, 0, 0], epsilon=0.1)
current_velocity = calculate_velocity(current_velocity, action, max_speed)
uav_pos = update_uav_position(uav_pos, action)

# Step 3: Calculate reward
reward = calculate_reward(uav_pos, goal_pos, obstacles[0], 3, 1.5, 0.5)

# Step 4: Update Q-values
Q_values = [0, 0, 0, 0, 0, 0]
Q_values = update_Q(Q_values, action, reward, alpha=0.1, gamma=0.9)

print(f"UAV Position: {uav_pos}, Reward: {reward}, Q-values: {Q_values}")
