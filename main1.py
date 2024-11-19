import numpy as np
from evironment1 import initialize_environment
from action_selection1 import epsilon_greedy, softmax, update_Q
from visualization1 import visualize_path

# Initialize environment
uav_pos, goal_pos, obstacles = initialize_environment()

# Example Q-values and parameters
Q_values = [0.2, 0.5, 0.1, 0.4, 0.3, 0.6]
epsilon = 0.1
tau = 0.5

# Select action
action = epsilon_greedy(Q_values, epsilon)

# Update Q-values (example)
reward = -10
Q_values = update_Q(Q_values, action, reward)

# Visualize results
uav_path = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
visualize_path(uav_path, Q_values)
