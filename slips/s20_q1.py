import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
csv_file = '/content/diabetes.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
