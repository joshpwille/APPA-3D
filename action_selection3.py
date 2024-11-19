import torch
import torch.nn as nn
import torch.optim as optim

class QNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, 64)  # First hidden layer
        self.fc2 = nn.Linear(64, 64)  # Second hidden layer
        self.fc3 = nn.Linear(64, action_size)  # Output layer: Q-values for each action
    
    def forward(self, state):
        """
        Forward pass to compute Q-values for a given state.
        Args:
            state (tensor): Input state tensor.
        Returns:
            tensor: Q-values for all actions.
        """
        x = torch.relu(self.fc1(state))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
