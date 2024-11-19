import numpy as np

def epsilon_greedy(Q_values, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(len(Q_values))
    return np.argmax(Q_values)

def softmax(Q_values, tau):
    exp_values = np.exp(Q_values / tau)
    probabilities = exp_values / np.sum(exp_values)
    return np.random.choice(len(Q_values), p=probabilities)

def update_Q(Q_values, action, reward, alpha=0.1, gamma=0.9):
    Q_values[action] += alpha * (reward + gamma * np.max(Q_values) - Q_values[action])
    return Q_values
