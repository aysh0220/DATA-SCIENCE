import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Column1': [1, 2, np.nan, 4, 5],
    'Column2': [np.nan, 'A', 'B', np.nan, 'C'],
    'Column3': ['X', 'Y', 'Z', 'X', 'Y']
}

df = pd.DataFrame(data)

# Define a placeholder value for missing data
placeholder_value = 'Missing'

# Replace missing values in the DataFrame with the placeholder value
df.fillna(placeholder_value, inplace=True)

# Display the DataFrame with missing values replaced
print("DataFrame with Missing Values Replaced:")
print(df)
