# APPA-3D Path Planning Algorithm Implementation

**Description:**
This repository implements the pipeline of Algorithm 1 from the paper APPA-3D: An Autonomous 3D Path Planning Algorithm for UAVs in Unknown Complex Environments. The focus is on enabling autonomous, collision-free UAV navigation through reinforcement learning (RL) with an adaptive reward function and improved exploration strategies. 

# Pipeline Description

The pipeline follows the structure outlined in Algorithm 1 of the paper. The key components include:

/project.<br>
├── main_simulation.py.<br>
├── environment.py.<br>
├── action_selection.py.<br>
├── reward_function.py.<br>
├── uav_dynamics.py.<br>
└── visualization.py.<br>

**Environment Setup:**<br>
Define the UAV's initial position, target, and environment constraints (e.g., obstacles, no-fly zones).<br><br>
**Action Selection:**<br>
Balance exploration and exploitation using an optimized action exploration strategy.<br><br>
**Reward Calculation:**<br>
Adaptive reward functions combining potential field forces and dynamic environmental feedback.<br><br>
**Learning and Updating:**<br>
Apply Q-learning-based RL to update policies and converge to an optimal path.<br><br>
**UAV Dynamics:**<br>
Ensure realistic simulation with physical constraints like maximum speed, turning radius, and inertia<br><br>
**Simulation and Visualization:**<br>
Evaluate the algorithm in simulated 3D environments with static and dynamic obstacles.

# Algorithm Implementation

Step 1: Initialize Environment
Define UAV initial state s0, target state sg, and obstacles.

Step 2: Select an Action
Use the optimized exploration strategy based on state-action probabilities.

Step 3: Execute Action
Simulate the UAV's movement and observe the resulting state and reward.

Step 4: Update Policy
Update the Q-table using the Bellman equation:

Step 5: Repeat
Repeat until convergence or a stopping criterion (e.g., UAV reaches the target).

# Features

Adaptive Reward Function: Combines gravitational and repulsive forces to ensure smooth convergence.
Optimized Action Exploration: Balances exploration and exploitation with state-based adjustments.
Scalable Environment: Supports 3D environments with static and dynamic obstacles.

# Function Versioning

To maintain a clear history of changes, each function is assigned a version number. The version number is updated whenever the corresponding function is modified. This helps in:

Update the function's version number and document the change in the README.md.
