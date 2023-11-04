import pandas as pd

#read the file
df = pd.read_csv(r'C:\Users\cicic\OneDrive\Desktop\Barrios_Project\barrios\iss-data\csv\us_weekly_consumable_water_summary_20220102-20230903.csv')

# Convert the date column to a datetime dtype
df['Date'] = pd.to_datetime(df['Date'])

# Save the DataFrame to a CSV file with the new date format (YYYY-MM-DD)
df.to_csv(r'C:\Users\cicic\OneDrive\Desktop\Barrios_Project\barrios\iss-data\csv\formatted_dates\us_weekly_consumable_water_summary_20220102-20230903_d.csv',
          date_format= '%Y-%m-%d')
