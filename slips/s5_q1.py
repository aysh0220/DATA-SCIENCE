import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset (replace with your dataset)
df = pd.read_csv("/content/Netflix Userbase.csv")

# Choose an appropriate column for the pie chart (e.g., 'Category' column)
Country = 'Country'  # Replace with the actual column name from your dataset

# Count the values in the selected column
value_counts = df[Country].value_counts()

# Plot a pie chart
plt.figure(figsize=(8, 8))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Pie Chart for {Country}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()
