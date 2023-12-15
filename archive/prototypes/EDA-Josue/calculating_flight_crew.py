import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('../../iss-data\csv\eda\sorted_crew_alpha.csv')

# Group by date and sum the crew_count
grouped_by_date = df.groupby(['datedim'])['crew_count'].sum().reset_index()

# Specify the path where you want to save the new CSV file
output_path = '../../iss-data\csv\eda\crew-by-week.csv'

# Write the grouped data to a new CSV file
grouped_by_date.to_csv(output_path, index=False)

print(f"Grouped data saved to {output_path}")
