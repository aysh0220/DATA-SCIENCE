import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset (replace with your own dataset)
data = {
    'Values': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
}

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the style for the plots
sns.set_style('whitegrid')

# Create a Distribution Plot (Histogram)
plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1)
sns.histplot(df['Values'], kde=True)
plt.title('Histogram')

# Create a Distribution Plot (Kernel Density Estimation)
plt.subplot(2, 2, 2)
sns.kdeplot(df['Values'], shade=True)
plt.title('Kernel Density Estimation')

# Create a Distribution Plot (Box Plot)
plt.subplot(2, 2, 3)
sns.boxplot(x=df['Values'])
plt.title('Box Plot')

# Create a Distribution Plot (Violin Plot)
plt.subplot(2, 2, 4)
sns.violinplot(x=df['Values'])
plt.title('Violin Plot')

plt.tight_layout()
plt.show()
