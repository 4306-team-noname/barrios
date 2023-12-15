import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = '../../iss-data\csv\iss_flight_plan_20220101-20251231.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Filter rows where the 'event' column is 'Dock'
filtered_df = df[df['event'] == 'Dock']

# Display the result
print(filtered_df)