import pandas as pd

# Assuming the provided data is in a file named 'your_crew_file.csv'
file_path_crew = '../../iss-data\csv\eda\crew-by-week.csv'

# Read the crew file
df_crew = pd.read_csv(file_path_crew)

# Convert the 'datedim' column to datetime with the correct format
df_crew['datedim'] = pd.to_datetime(df_crew['datedim'], format='%Y-%m-%d')

# Assuming the provided data is in a file named 'ims_filtered.csv'
file_path_category = '../../iss-data\csv\eda\ims-datedim.csv'

# Read the first CSV file
df_category = pd.read_csv(file_path_category)

# Convert the 'datedim' column to datetime with the correct format
df_category['datedim'] = pd.to_datetime(df_category['datedim'], format='%Y-%m-%d %H:%M:%S.%f')

# Sort the DataFrame by 'datedim'
df_category = df_category.sort_values(by=['id', 'datedim'])

# Filter rows with category 'Food'
category_df = df_category[df_category['category_name'] == 'Food']

# Initialize variables
total_usage = 0
total_duration = 0

# Iterate through unique IDs
unique_ids = category_df['id'].unique()
for unique_id in unique_ids:
    id_df = category_df[category_df['id'] == unique_id]

    # Get the first and last date for each ID
    first_date = id_df['datedim'].min()
    last_date = id_df['datedim'].max()

    # Calculate the duration between the first and last date for each ID in weeks
    duration_weeks = (last_date - first_date).days // 7

    # Calculate weekly usage rate for each ID
    weekly_usage_rate = 1 / (duration_weeks + 1)  # Add 1 to include the single-week usage

    # Merge crew information based on 'datedim'
    merged_df = pd.merge(id_df, df_crew, on='datedim', how='left')

    # Check for NaN values in the 'crew_count' column and fill with 0
    merged_df['crew_count'] = merged_df['crew_count'].fillna(0)

    print(f"Merged DataFrame for ID {unique_id}:\n{merged_df}")

    # Get the sum of crew members for the current week
    crew_members = merged_df['crew_count'].sum()

    print(f"For ID {unique_id}, Weekly Usage Rate: {weekly_usage_rate}, Crew Members: {crew_members}")

    # Multiply the weekly usage rate by the number of crew members
    total_usage += weekly_usage_rate * crew_members
    total_duration += 1  # Since it's a single instance, use 1 week

# Calculate the average usage rate per week
if total_duration > 0:
    average_weekly_usage_rate = total_usage / total_duration
    print(f"The average usage rate for Category is: {average_weekly_usage_rate:.2f} per week")
else:
    print("No valid data to calculate the average usage rate.")