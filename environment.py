def initialize_environment():
    """
    Initialize the environment with UAV position, goal, and obstacles.
    Returns:
        tuple: UAV position, goal position, and obstacle list.
    """
    uav_pos = (1, 1, 1)  # Example UAV start position
    goal_pos = (10, 10, 10)  # Goal position
    obstacles = [(3, 4, 2), (6, 7, 3), (4.5,1.3,0.8)]  # List of obstacles
    return uav_pos, goal_pos, obstacles

def update_uav_position(uav_pos, action):
    """
    Update UAV position based on the selected action.
    Args:
        uav_pos (tuple): Current UAV position.
        action (int): Action index.
    Returns:
        tuple: Updated UAV position.
    """
    # Example: Update logic (add or subtract based on the action)
    actions = {
        0: (1, 0, 0),  # Move forward in x
        1: (-1, 0, 0),  # Move backward in x
        2: (0, 1, 0),  # Move forward in y
        3: (0, -1, 0),  # Move backward in y
        4: (0, 0, 1),  # Move up in z
        5: (0, 0, -1)  # Move down in z
    }
    delta = actions[action]
    return tuple(sum(x) for x in zip(uav_pos, delta))
