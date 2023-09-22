import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(0)

# Generate random data (replace this with your own data or data generation method)
num_samples = 100
X = np.random.rand(num_samples)  # Independent variable
y = 2 * X + 1 + np.random.randn(num_samples) * 0.2  # Dependent variable (with noise)

# Split the data into training and testing sets
train_ratio = 0.8  # Proportion of data for training
train_size = int(train_ratio * num_samples)

X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Create scatter plots for training and testing data
plt.figure(figsize=(10, 5))
plt.scatter(X_train, y_train, label='Training Data', alpha=0.7)
plt.scatter(X_test, y_test, label='Testing Data', alpha=0.7)
plt.xlabel('X (Independent Variable)')
plt.ylabel('y (Dependent Variable)')
plt.title('Training and Testing Data')
plt.legend()
plt.grid(True)
plt.show()
