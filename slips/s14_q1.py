import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('/content/Netflix Userbase.csv')

# Select appropriate columns for the scatter plot (replace column names)
x_column = 'Country'
y_column = 'Age'

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df[x_column], df[y_column], alpha=0.5)  # Adjust alpha for transparency
plt.title(f'Scatter Plot between {x_column} and {y_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.grid(True)
plt.show()
