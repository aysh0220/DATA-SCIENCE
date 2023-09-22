import pandas as pd
import numpy as np

# Create random data
np.random.seed(0)  # Setting a seed for reproducibility
data = {
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value1': np.random.randint(1, 100, size=100),
    'Value2': np.random.randint(50, 150, size=100),
}

# Create a DataFrame from the random data
df = pd.DataFrame(data)

# Create a pivot table
pivot_table = pd.pivot_table(df, values=['Value1', 'Value2'], index='Category', aggfunc=np.mean)

# Display the pivot table
print("Pivot Table:")
print(pivot_table)
