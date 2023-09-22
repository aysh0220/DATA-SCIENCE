#Download (https://www.kaggle.com/spscientist/students-performance-inexams?select=StudentsPerformance.csv)
import pandas as pd

# Read the CSV file into a DataFrame
file_path = "StudentsPerformance.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

# Display the shape of the dataset (number of rows and columns)
print("Shape of the dataset:", df.shape)

# Display the top rows of the dataset with their columns
print("\nTop rows of the dataset:")
print(df.head())
