import pandas as pd

# Read the dataset
df = pd.read_csv("employee_data.csv")

# a. Get descriptive statistics
descriptive_stats = df.describe()

# b. Find the 7 most common job titles
common_job_titles = df['JobTitle'].value_counts().head(7)

# c. Find the email of the employee with cell number 919096777860
cell_number_to_find = 919096777860
employee_email = df.loc[df['CellPhone'] == cell_number_to_find, 'Email'].values[0]

# Display the results
print("a. Descriptive Statistics:")
print(descriptive_stats)

print("\nb. 7 Most Common Job Titles:")
print(common_job_titles)

print("\nc. Employee Email with Cell Number 919096777860:")
print(employee_email)
