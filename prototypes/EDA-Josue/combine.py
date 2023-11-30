import pandas as pd
from datetime import datetime

# Read the CSV file
df = pd.read_csv('../../prototypes\EDA-Josue\ims_filtered.csv')

# Convert the 'datedim' column to datetime
df['datedim'] = pd.to_datetime(df['datedim'])

# Sort the DataFrame by 'datedim'
df = df.sort_values(by='datedim')

# Filter rows with category 'Water'
category_df = df[df['category_name'] == 'Filter Inserts']

# Initialize variables
usage_rates = []

# Iterate through unique IDs
unique_ids = category_df['id'].unique()
for unique_id in unique_ids:
    id_df = category_df[category_df['id'] == unique_id]
    
    # Initialize variables for each ID
    usage_start_date = None
    
    # Iterate through rows to calculate usage rates for each ID
    for index, row in id_df.iterrows():
        if usage_start_date is None:
            usage_start_date = row['datedim']
        else:
            usage_end_date = row['datedim']
            usage_duration = (usage_end_date - usage_start_date).days
            
            # Calculate usage rate for each entry
            usage_rate = 1 / (usage_duration + 1)  # Add 1 to include the single-day usage
            usage_rates.append(usage_rate)
            
            usage_start_date = usage_end_date

# Check if there are any usage rates before calculating the average
if len(usage_rates) > 0:
    average_usage_rate = sum(usage_rates) / len(usage_rates)
    print(f"The average usage rate for Category is: {average_usage_rate}")
else:
    print("No valid data to calculate the average usage rate.")