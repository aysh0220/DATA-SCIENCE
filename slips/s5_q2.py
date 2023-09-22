import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample dataset (replace this with your actual dataset)
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [2, 4, 1, 3, 5, 8, 7, 6, 9, 10],
    'C': [1, 3, 2, 4, 5, 7, 6, 8, 10, np.nan],
    'D': [1, 2, 1, np.nan, 5, 6, 5, 8, 9, 10]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Step 1: Create a heatmap to identify correlations
correlation_matrix = df.corr()

# Set the figure size
plt.figure(figsize=(8, 6))

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")

plt.show()

# Step 2: Find and handle missing values
# Find missing values
missing_values = df.isna().sum()
print("Missing Values:")
print(missing_values)

# Handle missing values (replace NaN with the mean of the column)
df.fillna(df.mean(), inplace=True)

# Check for missing values again
remaining_missing_values = df.isna().sum()
print("\nMissing Values After Handling:")
print(remaining_missing_values)
