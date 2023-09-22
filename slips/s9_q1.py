import pandas as pd

# Create a dictionary with sample data
data = {
    'Date': ['2023-09-01', '2023-09-01', '2023-09-02', '2023-09-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Create a pivot table using the Pandas pivot_table() function
pivot_table = pd.pivot_table(df, values='Value', index='Date', columns='Category', aggfunc='sum')

# Display the pivot table
print(pivot_table)
