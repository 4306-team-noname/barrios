import pandas as pd

# Read the CSV file
df = pd.read_csv('../../iss-data\csv\eda\ims_filtered.csv')

# Parse 'datedim' column as datetime
df['datedim'] = pd.to_datetime(df['datedim'])

# Format 'datedim' column to the desired format
df['datedim'] = df['datedim'].dt.strftime('%Y-%m-%d')

# Save the modified DataFrame back to a new CSV file
df.to_csv('../../iss-data\csv\eda\ims-datedim.csv', index=False)
