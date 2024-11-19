import numpy as np

# Hyperbolic tangent function
def tanh(x):
    return np.tanh(x)

def calculate_reward(uav_pos, goal_pos, obstacle_pos, D_cz, D_max, d_max):
    """
    Calculate the adaptive reward for the UAV based on its position relative to the goal and obstacles.
    Args:
        uav_pos (tuple): UAV's current position (x, y, z).
        goal_pos (tuple): Goal position (x, y, z).
        obstacle_pos (tuple): Nearest obstacle position (x, y, z).
        D_cz (float): Critical zone distance for the obstacle.
        D_max (float): Maximum effective distance for obstacle avoidance.
        d_max (float): Maximum distance to the goal.
    Returns:
        float: Calculated reward (R).
    """
    # Calculate distances
    d_goal = np.linalg.norm(np.array(uav_pos) - np.array(goal_pos))  # Distance to the goal
    d_t_goal_next = d_goal - 1  # Example next-step goal threshold
    d_t_goal = d_goal           # Current goal threshold

    d_barrier = np.linalg.norm(np.array(uav_pos) - np.array(obstacle_pos))  # Distance to the obstacle
    d_t_barrier_next = d_barrier - 1  # Example next-step barrier threshold
    d_t_barrier = d_barrier           # Current barrier threshold

    # Calculate Ra
    Ra = tanh(d_max - d_goal) * ((d_t_goal_next - d_t_goal) / (d_t_goal_next - d_t_goal) if d_t_goal_next != d_t_goal else 1)

    # Calculate Rcz
    if d_t_barrier_next != d_t_barrier and d_t_goal_next != d_t_goal:
        Rcz = (tanh(D_cz - d_t_barrier) * ((d_t_goal_next - d_t_barrier_next) / (d_t_barrier - d_t_barrier_next))) + \
              (tanh(d_max - d_goal) * ((d_t_goal_next - d_t_goal) / (d_t_goal_next - d_t_goal)))
    else:
        Rcz = 0

    # Calculate Rmz
    if d_t_barrier_next != d_t_barrier:
        Rmz = tanh(D_cz - d_t_barrier) * ((d_t_barrier_next - d_t_barrier) / (d_t_barrier_next - d_t_barrier))
    else:
        Rmz = 0

    # Determine R based on the conditions
    if d_barrier >= D_cz or (D_cz < d_barrier <= D_max):
        R = Ra
    elif D_max <= d_barrier <= D_cz:
        R = Rcz
    else:  # d_barrier < D_cz
        R = Rmz

    return R, Ra, Rcz, Rmz
