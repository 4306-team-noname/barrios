import pandas as pd

# Replace 'your_file.csv' with the actual filename
input_file = '../../iss-data\csv\iss_flight_plan_crew_20220101-20251321.csv'
output_file = '../../iss-data\csv\eda\crew_filtered.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Filter rows where 'crew_count' is greater than 0
df_filtered = df[df['crew_count'] > 0]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
