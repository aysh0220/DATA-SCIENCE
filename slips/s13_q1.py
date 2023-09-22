import pandas as pd

# Create a dictionary with student details
student_data = {
    'Rollno': [1, 2, 3, 4, 5],
    'Studname': ['Aysh', 'Robot', 'Najma', 'Aliya', 'Eda'],
    'Address': ['123 Main St', '456 Elm St', '789 Oak St', '101 Pine St', '202 Birch St'],
    'Marks': [85, 92, 78, 95, 88],
    'Contact': ['123-456-7890', '987-654-3210', '555-555-5555', '111-222-3333', '999-888-7777']
}

# Create a DataFrame from the dictionary
student_df = pd.DataFrame(student_data)

# Display the details of the students
print("Details of 5 Students:")
print(student_df)

# Alter the "Contact" column (e.g., add the country code)
student_df['Contact'] = '+1-' + student_df['Contact']

# Display the DataFrame with the altered "Contact" column
print("\nDetails of 5 Students with Altered Contact:")
print(student_df)
