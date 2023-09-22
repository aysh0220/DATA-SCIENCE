import pandas as pd

# Step 1: Read the dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('/content/diabetes.csv')

# Step 2: Calculate the Average Age of People Having Diabetes (Question a)
average_age_with_diabetes = df[df['DiabetesPedigreeFunction'] == 1]['Age'].mean()
print(f"a. The average age of people having diabetes is {average_age_with_diabetes:.2f} years.")

# Step 3: Count People Below Average Age with Diabetes (Question b)
people_below_avg_age_with_diabetes = df[(df['Age'] < average_age_with_diabetes) & (df['DiabetesPedigreeFunction'] == 1)].shape[0]
print(f"b. {people_below_avg_age_with_diabetes} people in the dataset are below the average age and have diabetes.")

# Step 4: Check the Relationship Between Blood Pressure and Weight (Question c)
import matplotlib.pyplot as plt

plt.scatter(df['BloodPressure'], df['Insulin'], alpha=0.5)
plt.xlabel('BloodPressure')
plt.ylabel('Insulin')
#using Blood pressure instead of weight bcoz of csv file...
plt.title('c. Relationship Between Blood Pressure and Weight')
plt.show()
