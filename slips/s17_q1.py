import pandas as pd

# Create a sample society's dataset
data = {
    'Location': ['Pune', 'Pune', 'Pune', 'Kondhwa', 'Kondhwa'],
    'Property_Type': ['Rental', 'Rental', 'Rental', 'Apartment', 'Apartment'],
    'Bedroom_Count': [0, 1, 2, 2, 3],
}

# Create a DataFrame from the sample data
society_df = pd.DataFrame(data)

# a. How many houses in Pune rental list do not have a bedroom
pune_rental_no_bedroom = society_df[(society_df['Location'] == 'Pune') & (society_df['Property_Type'] == 'Rental') & (society_df['Bedroom_Count'] == 0)]
num_houses_without_bedroom = len(pune_rental_no_bedroom)

# b. How many 2BHK apartments are there in Kondhwa
kondhwa_2bhk_apartments = society_df[(society_df['Location'] == 'Kondhwa') & (society_df['Property_Type'] == 'Apartment') & (society_df['Bedroom_Count'] == 2)]
num_2bhk_apartments_in_kondhwa = len(kondhwa_2bhk_apartments)

print(f"The number of houses in Pune rental list without a bedroom: {num_houses_without_bedroom}")
print(f"The number of 2BHK apartments in Kondhwa: {num_2bhk_apartments_in_kondhwa}")
