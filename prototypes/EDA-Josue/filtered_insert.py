import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('../../prototypes\EDA-Josue\ims_filtered.csv')

# Filter rows where category_id is 5.0
filtered_df = df[df['categoryID'] == 5.0]

# Display the resulting DataFrame
print(filtered_df)
