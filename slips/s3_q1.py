import pandas as pd

# Accept input values into a dictionary
data = {}
num_entries = int(input("Enter the number of entries: "))

for i in range(num_entries):
    key = input(f"Enter key for entry {i + 1}: ")
    value = input(f"Enter value for entry {i + 1}: ")
    data[key] = value

# Create a DataFrame from the dictionary
df = pd.DataFrame(list(data.items()), columns=['Key', 'Value'])

# Display the DataFrame
print("\nDataFrame:")
print(df)
