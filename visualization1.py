import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_path(uav_positions, rewards):
    x, y, z = zip(*uav_positions)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, marker='o', label='UAV Path')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Reward')
    ax.legend()
    plt.title('UAV Path and Rewards')
    plt.show()
