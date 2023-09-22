import pandas as pd
import matplotlib.pyplot as plt
import random

# Create a sample seller dataset
data = {
    'Seller_ID': range(1, 101),
    'Seller_Name': [f'Seller_{i}' for i in range(1, 101)],
    'Seller_Type': [random.choice(['Type_A', 'Type_B', 'Type_C']) for _ in range(100)],
    'Layout_Type': [random.choice(['Layout_1', 'Layout_2', 'Layout_3']) for _ in range(100)]
}

# Create a DataFrame from the sample data
seller_df = pd.DataFrame(data)

# a. How many different seller types are there? Show using appropriate graphs.
seller_type_counts = seller_df['Seller_Type'].value_counts()
plt.figure(figsize=(6, 4))
seller_type_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Different Seller Types')
plt.xlabel('Seller Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# b. Which seller has minimum records in the dataset?
min_records_seller = seller_type_counts.idxmin()
print(f"The seller with the minimum records is: {min_records_seller}")

# c. Using appropriate graphs, show the count of different layout types in the dataset.
layout_type_counts = seller_df['Layout_Type'].value_counts()
plt.figure(figsize=(6, 4))
layout_type_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightgreen'])
plt.title('Count of Different Layout Types')
plt.ylabel('')
plt.show()

