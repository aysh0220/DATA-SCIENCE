import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Given data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([7, 14, 15, 18, 19, 21, 26, 23])

# Reshape x into a 2D array (required by sklearn)
x = x.reshape(-1, 1)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Estimated coefficients
b0 = model.intercept_
b1 = model.coef_[0]

# Predicted values based on the model
y_pred = model.predict(x)

# Model performance metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Display the results
print(f"Estimated Coefficient b0 (intercept): {b0:.4f}")
print(f"Estimated Coefficient b1 (slope): {b1:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-squared (R2) Score: {r2:.4f}")
