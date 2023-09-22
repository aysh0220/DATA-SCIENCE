import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
X = np.array([1, 2, 3, 4, 5])  # Independent variable
y = np.array([2, 4, 5, 4, 5])  # Dependent variable
# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X.reshape(-1, 1), y)
b0 = model.intercept_  # Intercept (b0)
b1 = model.coef_[0]    # Slope (b1)
# Make predictions
y_pred = model.predict(X.reshape(-1, 1))

# Calculate Mean Squared Error
mse = mean_squared_error(y, y_pred)

# Calculate R-squared
r2 = r2_score(y, y_pred)

# Print the coefficients and performance metrics
print(f"Estimated Coefficients: b0 = {b0:.2f}, b1 = {b1:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")
