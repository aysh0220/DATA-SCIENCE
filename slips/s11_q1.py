import matplotlib.pyplot as plt
import numpy as np

# Example data (replace with your own data)
X = np.array([1, 2, 3, 4, 5, 6])
y_actual = np.array([1.1, 1.9, 3.2, 4.0, 5.2, 5.8])

# Fit a linear regression model (replace with your own model)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X.reshape(-1, 1), y_actual)

# Predicted values
y_pred = model.predict(X.reshape(-1, 1))

# Calculate residuals
residuals = y_actual - y_pred

# Create residual plot
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()
