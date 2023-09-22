import numpy as np
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(0)

# Generate random data for training and testing
data_size = 100
X = np.random.rand(data_size)  # Random input values
y = 2 * X + 1 + np.random.randn(data_size) * 0.2  # Simulated linear relationship with noise

# Split the data into training and testing sets (80% training, 20% testing)
split_ratio = 0.8
split_index = int(data_size * split_ratio)

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Create scatter plots for training and testing data
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train, c='b', marker='o', label='Training Data')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Training Data')

plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, c='r', marker='x', label='Testing Data')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Testing Data')

plt.tight_layout()
plt.show()
