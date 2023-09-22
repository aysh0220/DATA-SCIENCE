# 1.Write a program accepting random values in the dictionary and make a pivot table 
import pandas as pd
import random

# Accept random values into a dictionary
data = {
    'Category': [random.choice(['A', 'B', 'C']) for _ in range(100)],
    'Value1': [random.randint(1, 100) for _ in range(100)],
    'Value2': [random.randint(50, 150) for _ in range(100)],
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Create a pivot table
pivot_table = pd.pivot_table(df, values=['Value1', 'Value2'], index='Category', aggfunc='mean')

# Display the pivot table
print("Pivot Table:")
print(pivot_table)
