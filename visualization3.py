import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_path(uav_positions, rewards):
    """
    Visualize the UAV path, start point, and end point in 3D.
    Args:
        uav_positions (list of tuples): List of UAV (x, y, z) positions.
        rewards (list of float): Rewards corresponding to each step.
    """
    # Extract x, y, z coordinates
    x, y, z = zip(*uav_positions)
    
    # Create a 3D plot for the UAV path
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the UAV path
    ax.plot(x, y, z, marker='o', label='UAV Path')
    
    # Highlight the start point
    ax.scatter(x[0], y[0], z[0], color='green', s=100, label='Start Point')  # Larger green point
    
    # Highlight the end point
    ax.scatter(x[-1], y[-1], z[-1], color='red', s=100, label='End Point')  # Larger red point
    
    # Add labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.title('UAV Path with Start and End Points')
    
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
