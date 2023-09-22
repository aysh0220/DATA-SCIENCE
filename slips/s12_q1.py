# Write a program accept csv file and draw the pivot tab easy code


import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv('/content/Netflix Userbase.csv')

# Create a pivot table
pivot_table = df.pivot_table(index='User ID', columns='Subscription Type')

# Draw the pivot table
fig = px.imshow(pivot_table)
fig.show()


# have uploaded the csv file link in  csv dataset file