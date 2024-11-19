import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_path(uav_positions, rewards, obstacles):
    """
    Visualize the UAV path, start point, end point, and obstacles in 3D.
    Args:
        uav_positions (list of tuples): List of UAV (x, y, z) positions.
        rewards (list of float): Rewards corresponding to each step.
        obstacles (list of tuples): List of obstacle (x, y, z) positions.
    """
    # Extract x, y, z coordinates for UAV path
    x, y, z = zip(*uav_positions)
    
    # Extract obstacle coordinates
    obstacle_x, obstacle_y, obstacle_z = zip(*obstacles)

    # Create a 3D plot for the UAV path and obstacles
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the UAV path
    ax.plot(x, y, z, marker='o', label='UAV Path')
    
    # Highlight the start point
    ax.scatter(x[0], y[0], z[0], color='green', s=100, label='Start Point')  # Green marker
    
    # Highlight the end point
    ax.scatter(x[-1], y[-1], z[-1], color='red', s=100, label='End Point')  # Red marker
    
    # Plot obstacles
    ax.scatter(obstacle_x, obstacle_y, obstacle_z, color='blue', s=80, marker='x', label='Obstacles')  # Blue X markers
    
    # Add labels, legend, and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.title('UAV Path with Start, End, and Obstacles')
    
    # Show 3D plot
    plt.show()

    # Create a 2D plot for rewards over time
    plt.figure()
    plt.plot(rewards, marker='o', linestyle='-', label='Rewards')
    plt.xlabel('Steps')
    plt.ylabel('Reward')
    plt.title('Rewards Over Time')
    plt.legend()
    plt.grid()
    plt.show()
