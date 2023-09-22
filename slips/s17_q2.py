import pandas as pd

# Create a sample dataset
data = {
    'Flight_Number': [101, 102, 103, 104, 105],
    'Airline': ['Delta', 'United', 'American', 'Delta', 'Southwest'],
    'Departure_Airport': ['JFK', 'LAX', 'DFW', 'JFK', 'ATL'],
    'Arrival_Airport': ['LAX', 'DFW', 'ORD', 'LAX', 'MCO'],
    'Departure_Time': ['2023-09-22 08:00', '2023-09-22 09:30', '2023-09-22 11:15', '2023-09-22 13:45', '2023-09-22 15:20']
}

# Create a DataFrame from the sample data
flights_df = pd.DataFrame(data)

# 1. Find the size of the dataset
dataset_size = flights_df.shape
print(f"Size of the dataset: {dataset_size[0]} rows x {dataset_size[1]} columns")

# 2. Give a count of all available airlines
airline_counts = flights_df['Airline'].value_counts()
print("Count of all available airlines:")
print(airline_counts)

# 3. Which airline is the most common
most_common_airline = airline_counts.idxmax()
print(f"The most common airline is: {most_common_airline}")

# 4. Which airport has the maximum departures
max_departures_airport = flights_df['Departure_Airport'].value_counts().idxmax()
print(f"The airport with the maximum departures is: {max_departures_airport}")
