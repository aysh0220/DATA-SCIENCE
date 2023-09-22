import pandas as pd

# Create a dictionary with student details
student_data = {
    'Rollno': [1, 2, 3, 4, 5],
    'Studname': ['Ayesha', 'Najma', 'Aliya', 'Alina', 'Robot'],
    'Address': ['123 Main St', '456 Elm St', '789 Oak St', '101 Pine St', '202 Birch St'],
    'Marks': [85, 92, 78, 95, 88]
}

# Create a DataFrame from the dictionary
student_df = pd.DataFrame(student_data)

# Display the details of the students
print(student_df)
