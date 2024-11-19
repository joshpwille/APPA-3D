import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_path(uav_positions, rewards):
    x, y, z = zip(*uav_positions)  # Extract UAV x, y, z positions
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, marker='o', label='UAV Path')  # Plot UAV path
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')  # Correct label for the z-axis
    ax.legend()
    plt.title('UAV Path in 3D Space')
    plt.show()

    # Additionally, plot rewards over time
    plt.figure()
    plt.plot(rewards, marker='o', linestyle='-', label='Rewards')
    plt.xlabel('Steps')
    plt.ylabel('Reward')
    plt.title('Rewards Over Time')
    plt.legend()
    plt.grid()
    plt.show()
