import pandas as pd

# Create a Series
data_series = pd.Series([1, 2, 3, 4, 5])

# Create a DataFrame
data_dict = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
data_df = pd.DataFrame(data_dict)

# Function to square a number
def square(x):
    return x ** 2

# Function to add 10 to a number
def add_10(x):
    return x + 10

# Apply the square function to the Series
result_series_apply = data_series.apply(square)

# Apply the add_10 function to the DataFrame using applymap()
result_df_applymap = data_df.applymap(add_10)

# Create a mapping dictionary
mapping_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# Map the Series using the mapping dictionary
result_series_map = data_series.map(mapping_dict)

# Display the results
print("Original Series:")
print(data_series)

print("\nResult of Series.apply(square):")
print(result_series_apply)

print("\nOriginal DataFrame:")
print(data_df)

print("\nResult of DataFrame.applymap(add_10):")
print(result_df_applymap)

print("\nResult of Series.map(mapping_dict):")
print(result_series_map)
