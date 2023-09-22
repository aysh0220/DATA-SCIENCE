import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame (replace with your own dataset)
data = {
    'Column1': [10, 15, 20, 25, 30, 35, 40, 45, 200],
    'Column2': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Column3': [100, 110, 120, 130, 140, 150, 160, 170, 1000]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a function to identify and visualize outliers
def identify_outliers(column_data, column_name):
    Q1 = column_data.quantile(0.25)
    Q3 = column_data.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = column_data[(column_data < lower_bound) | (column_data > upper_bound)]
    
    plt.figure(figsize=(6, 4))
    plt.scatter(range(1, len(column_data) + 1), column_data, label='Data')
    plt.scatter(outliers.index, outliers, color='red', label='Outliers')
    plt.xlabel('Index')
    plt.ylabel(column_name)
    plt.title(f'Outliers in {column_name}')
    plt.legend()
    plt.show()

# Identify and visualize outliers for each column
for column in df.columns:
    identify_outliers(df[column], column)

