import numpy as np

def calculate_reward(uav_pos, goal_pos, obstacle_pos, safe_zone, collision_zone, mandatory_zone):
    """
    Calculate the reward based on UAV position relative to goal and obstacles.
    """
    d_goal = np.linalg.norm(np.array(uav_pos) - np.array(goal_pos))
    d_barrier = np.linalg.norm(np.array(uav_pos) - np.array(obstacle_pos))

    if d_barrier > safe_zone:
        return -d_goal  # Encourage moving closer to the goal
    elif collision_zone < d_barrier <= safe_zone:
        return -d_goal + (safe_zone - d_barrier)  # Balance goal progression and avoidance
    elif mandatory_zone <= d_barrier <= collision_zone:
        return -1000  # Penalize being too close to obstacles
