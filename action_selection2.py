import numpy as np

def epsilon_greedy(Q_values, epsilon):
    """
    Select action using epsilon-greedy strategy.
    """
    if np.random.rand() < epsilon:
        return np.random.randint(len(Q_values))  # Random action
    return np.argmax(Q_values)  # Best action

def softmax(Q_values, tau):
    """
    Select action using softmax strategy.
    """
    exp_values = np.exp(Q_values / tau)
    probabilities = exp_values / np.sum(exp_values)
    return np.random.choice(len(Q_values), p=probabilities)

def update_Q(Q_values, action, reward, alpha, gamma):
    """
    Update Q-values using Q-learning update formula.
    """
    Q_values[action] += alpha * (reward + gamma * np.max(Q_values) - Q_values[action])
    return Q_values
