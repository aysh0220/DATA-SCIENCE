import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset (replace with your dataset)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Set up subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Distribution Plot for Age
sns.histplot(data=df, x='Age', ax=axes[0, 0], bins=5, kde=True)
axes[0, 0].set_title('Age Distribution Plot')

# Distribution Plot for Income
sns.histplot(data=df, x='Income', ax=axes[0, 1], bins=5, kde=True)
axes[0, 1].set_title('Income Distribution Plot')

# Box Plot for Age
sns.boxplot(data=df, y='Age', ax=axes[1, 0])
axes[1, 0].set_title('Age Box Plot')

# Box Plot for Income
sns.boxplot(data=df, y='Income', ax=axes[1, 1])
axes[1, 1].set_title('Income Box Plot')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
