import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset (replace with your dataset)
data = {
    'X': np.arange(1, 11),
    'Y': [2.3, 3.0, 4.1, 4.8, 6.2, 7.0, 8.1, 8.9, 10.2, 11.0]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Fit a simple linear regression model (replace with your regression model)
from sklearn.linear_model import LinearRegression

X = df[['X']]
y = df['Y']

model = LinearRegression()
model.fit(X, y)

# Calculate the residuals
residuals = y - model.predict(X)

# Create a residual plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X['X'], y=residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('X')
plt.ylabel('Residuals')
plt.show()
