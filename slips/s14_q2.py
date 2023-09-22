import pandas as pd

# Read the dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('/content/student-por.csv')
# Describe student details
student_details_description = df.describe()
print("Student Details Summary:")
print(student_details_description)
# Find missing values in the dataset
missing_values = df.isnull().sum()

# Fill missing data with appropriate values (replace 'column_name' and 'fill_value')
df['age'].fillna('fill_value', inplace=True)

# Alternatively, you can drop rows with missing values
# df.dropna(inplace=True)

print("Missing Values:")
print(missing_values)
# Drop irrelevant columns (replace 'column_name' with the actual column name)
df.drop(columns=['age'], inplace=True)

print("DataFrame after dropping irrelevant columns:")
print(df)
