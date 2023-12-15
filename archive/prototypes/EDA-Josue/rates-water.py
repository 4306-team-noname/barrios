import pandas as pd
from datetime import datetime, timedelta

# Read the CSV file
df = pd.read_csv('../../iss-data\csv\sus_weekly_consumable_water_summary_20220102-20230903.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Sort the DataFrame by date
df = df.sort_values(by='Date')

# Calculate the weekly consumption rate for 'Corrected Total'
df['Weekly Consumption Rate'] = df['Corrected Total (L)'].diff() / 7

# Calculate the average rate per week
average_rate = df['Weekly Consumption Rate'].mean()

# Display the result
print(f"Average Rate per Week: {average_rate:.2f} L/week")