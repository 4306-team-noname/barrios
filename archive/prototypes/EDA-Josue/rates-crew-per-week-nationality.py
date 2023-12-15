import pandas as pd

# Assuming the provided data is in a file named 'your_crew_file.csv'
file_path_crew = '../../iss-data\csv\eda\sorted_nationalities.csv'

# Read the crew file
df_crew = pd.read_csv(file_path_crew)

# Convert the 'datedim' column to datetime with the correct format
df_crew['datedim'] = pd.to_datetime(df_crew['datedim'], format='%Y-%m-%d')

# Assuming the provided data is in a file named ''
file_path_category = '../../iss-data\csv\eda\ims-datedim.csv'

# Read the first CSV file
df_category = pd.read_csv(file_path_category)

# Convert the 'datedim' column to datetime with the correct format
df_category['datedim'] = pd.to_datetime(df_category['datedim'], format='%Y-%m-%d')

# Sort the DataFrame by 'datedim'
df_category = df_category.sort_values(by=['id', 'datedim'])

# Filter rows with category 'category'
category_df = df_category[df_category['category_name'] == 'KTO']

# Initialize variables
total_usos_rate = 0
total_ru_rate = 0
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

    # Group by week and take the last crew count for each week
    weekly_crew_counts = merged_df.groupby(merged_df['datedim'].dt.to_period("W")).last()['crew_count']

    # Get the crew count for the last week
    crew_members = weekly_crew_counts.iloc[-1] if not weekly_crew_counts.empty else 0

    # Separate crew members by nationality (USOS and RU)
    usos_crew = merged_df[merged_df['nationality_category'].isin(['CSA', 'ESA', 'JAXA', 'NASA', 'USOS', 'ASI', 'NASA, USOS', 'Commercial'])]
    ru_crew = merged_df[merged_df['nationality_category'].isin(['RSA', 'SFP','RU'])]

    # Calculate rates for USOS and RU separately
    usos_rate = weekly_usage_rate * usos_crew['crew_count'].iloc[-1] if not usos_crew.empty else 0
    ru_rate = weekly_usage_rate * ru_crew['crew_count'].iloc[-1] if not ru_crew.empty else 0

    # Add rates to the total
    total_usos_rate += usos_rate
    total_ru_rate += ru_rate
    total_duration += 1  # Since it's a single instance, use 1 week

# Calculate the difference in rates between USOS and RU
if total_duration > 0:
    # Print weekly rates for USOS and RU
    print(f"Average USOS rate per week: {total_usos_rate / total_duration:.2f}")
    print(f"Average RU rate per week: {total_ru_rate / total_duration:.2f}")
else:
    print("No valid data to calculate the rate difference.")