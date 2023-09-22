import pandas as pd

# Create a sample dataset
data = {
    'Student_Name': ['Aysh', 'Aliya', 'Najma', 'Mansi', 'summaiya'],
    'Marks': [50, 28, 33, 40, 30],
    'Exam_Attempts': [1, 1, 4, 1, 2]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# a. Select the rows where the marks are between 30 and 35.
marks_between_30_and_35 = df[(df['Marks'] >= 30) & (df['Marks'] <= 35)]
print("Rows where marks are between 30 and 35:")
print(marks_between_30_and_35)

# b. Select the rows where the number of attempts is less than 2 and marks greater than 30.
attempts_less_than_2_and_marks_greater_than_30 = df[(df['Exam_Attempts'] < 2) & (df['Marks'] > 30)]
print("\nRows with attempts less than 2 and marks greater than 30:")
print(attempts_less_than_2_and_marks_greater_than_30)

# c. Calculate the sum of examination attempts by the students.
total_attempts = df['Exam_Attempts'].sum()
print("\nTotal examination attempts by students:", total_attempts)
