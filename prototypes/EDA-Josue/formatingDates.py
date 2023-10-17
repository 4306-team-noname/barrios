import pandas as pd

#read the file
df = pd.read_csv(r'C:\Users\xbox1\OneDrive - Angelo State University\Documents\CS4306\barrios-1\iss-data\csv\s_us_rs_weekly_consumable_gas_summary_20220102-20230903.csv')

# Convert the date column to a datetime dtype
df['Date'] = pd.to_datetime(df['Date'])

# Save the DataFrame to a CSV file with the new date format (YYYY-MM-DD)
df.to_csv(r'C:\Users\xbox1\OneDrive - Angelo State University\Documents\CS4306\barrios-1\iss-data\csv\test\us_rs_weekly_consumbale_gas_summary_1.csv',
          date_format= '%Y-%m-%d')