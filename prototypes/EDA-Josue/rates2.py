import pandas as pd

# Read the CSV file
df = pd.read_csv('../../iss-data\csv\s_us_rs_weekly_consumable_gas_summary_20220102-20230903.csv')

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Calculate weekly consumption for each consumable
consumables = ['USOS O2 (kg)', 'RS O2 (kg)', 'US N2 (kg)', 'RS N2 (kg)', 'Adjusted O2 (kg)', 'Adjusted N2 (kg)', 'Resupply O2 (kg)', 'Resupply N2 (kg)', 'Resupply Air (kg)']

# Create a new DataFrame to store weekly consumption
weekly_consumption = pd.DataFrame(index=df.index)

for consumable in consumables:
    # Calculate the weekly difference and fill NaN values with 0
    weekly_consumption[consumable + '_Weekly'] = df[consumable].diff(7).fillna(0)

# Print the resulting DataFrame
print(weekly_consumption)
