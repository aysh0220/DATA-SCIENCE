import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Ayesha', 'Najma', 'Aliya', 'Hajra'],
    'Age': [19, 19, 10, 4],
    'City': ['Pune', 'Hadapsr', 'P-Town!', 'Pimpri']
}

df = pd.DataFrame(data)

# Accessing columns
print("Column 'Name':")
print(df['Name'])

# Accessing rows by index
print("\nRow 0:")
print(df.loc[0])

# Accessing specific cell
print("\nValue at row 1, column 'Age':")
print(df.at[1, 'Age'])



# output:------------------>
# Column 'Name':
# 0    Ayesha
# 1     Najma
# 2     Aliya
# 3     Hajra
# Name: Name, dtype: object

# Row 0:
# Name    Ayesha
# Age         19
# City      Pune
# Name: 0, dtype: object

# Value at row 1, column 'Age':
# 19