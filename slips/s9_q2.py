import pandas as pd
#using name instead of mobole no 
# Read the dataset
df = pd.read_csv('/content/employee_data.csv')
# Find missing values and replace with "irrelevant"
df.fillna("irrelevant", inplace=True)
# Find the 7 most common job titles
common_job_titles = df['JobFunctionDescription'].value_counts().head(7)
print("7 Most Common Job Titles:")
print(common_job_titles)
# Find the email of an employee with cell number '919096777860'

FirstName = 'Zoie'
employee_email = df[df['FirstName'] == FirstName]['ADEmail']
print(f"Email of Employee with Cell Number {FirstName}: {employee_email.values[0]}")
