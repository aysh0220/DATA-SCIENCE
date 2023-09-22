import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset (replace with your dataset)
data = {
    'Values': [10, 15, 20, 25, 30, 35, 200, 45, 50, 55, 60, 65, 70, 75]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Identify outliers using the interquartile range (IQR) method
Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Values'] < lower_bound) | (df['Values'] > upper_bound)]

# Draw a box plot
plt.figure(figsize=(6, 4))
plt.boxplot(df['Values'], vert=False)
plt.title('Box Plot with Outliers')
plt.xlabel('Values')
plt.show()

# Display the identified outliers
print("Identified Outliers:")
print(outliers)
