import pandas as pd

# Assuming the provided data is in a file named 'your_file.csv'
file_path = '../../iss-data\csv\eda\ims_filtered_stored.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Convert the 'datedim' column to datetime with the correct format
df['datedim'] = pd.to_datetime(df['datedim'], format='%m/%d/%Y %H:%M')

# Sort the DataFrame by 'datedim'
df = df.sort_values(by=['id', 'datedim'])

# Filter rows with category 'Water'
water_df = df[df['category_name'] == 'ACY Inserts']

# Initialize variables
total_usage = 0
total_duration = 0

# Iterate through unique IDs
unique_ids = water_df['id'].unique()
for unique_id in unique_ids:
    id_df = water_df[water_df['id'] == unique_id]

    # Get the first and last date for each ID
    first_date = id_df['datedim'].min()
    last_date = id_df['datedim'].max()

    # Calculate the duration between the first and last date for each ID in weeks
    duration_weeks = (last_date - first_date).days // 7

    # Calculate weekly usage rate for each ID
    weekly_usage_rate = 1 / (duration_weeks + 1)  # Add 1 to include the single-week usage

    # Add the total for the current ID to the overall total
    total_usage += weekly_usage_rate
    total_duration += 1  # Since it's a single instance, use 1 week

# Calculate the average usage rate per week
if total_duration > 0:
    average_weekly_usage_rate = total_usage / total_duration
    print(f"The average usage rate for Water is: {average_weekly_usage_rate:.2f} per week")
else:
    print("No valid data to calculate the average usage rate.")
