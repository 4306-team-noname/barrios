import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('../../iss-data\csv\eda\crew_filtered.csv')

# Sort the DataFrame by the 'datedim' column
df['datedim'] = pd.to_datetime(df['datedim'])

# Sort the DataFrame by the 'datedim' column in ascending order (oldest to latest)
df = df.sort_values(by='datedim')

# Save the sorted DataFrame back to a CSV file
df.to_csv('../../iss-data\csv\eda\sorted_crew.csv', index=False)
