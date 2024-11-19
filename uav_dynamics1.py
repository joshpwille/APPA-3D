def calculate_velocity(current_velocity, action, max_speed):
    """
    Calculate the UAV's velocity based on the action and constraints.
    Args:
        current_velocity (tuple): Current velocity (vx, vy, vz).
        action (int): Action index.
        max_speed (float): Maximum allowable speed.
    Returns:
        tuple: Updated velocity.
    """
    # Example action to velocity mapping
    velocity_changes = {
        0: (1, 0, 0),  # Increase vx
        1: (-1, 0, 0),  # Decrease vx
        2: (0, 1, 0),  # Increase vy
        3: (0, -1, 0),  # Decrease vy
        4: (0, 0, 1),  # Increase vz
        5: (0, 0, -1)  # Decrease vz
    }
    delta_velocity = velocity_changes[action]
    new_velocity = tuple(sum(x) for x in zip(current_velocity, delta_velocity))
    
    # Clamp velocity to max_speed
    return tuple(min(max(v, -max_speed), max_speed) for v in new_velocity)
