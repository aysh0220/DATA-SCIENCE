import pandas as pd

# Create a dictionary with index labels
data = {
    'Name': ['ALIYA', 'HAJRA', 'NAJMA', 'AYSH'],
    'Age': [25, 30, 35, 40],
    'City': ['PUNE', 'PIMPRI', 'HADAPSAR', 'PUNE']
}

index_labels = ['A', 'B', 'C', 'D']

# Create a DataFrame from the dictionary with index labels
df = pd.DataFrame(data, index=index_labels)

# Display the DataFrame
print(df)
