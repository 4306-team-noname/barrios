import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = '../../iss-data\csv\eda\stored-datedim.csv'
#iss-data\csv\eda\Mockup - Sheet1.csv
#iss-data\csv\eda\ims-datedim.csv
#iss-data\csv\eda\stored-datedim.csv
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

#'%Y-%m-%d' '%m-%d-%Y'
# Convert 'datedim' to datetime if it's in string format
# Convert 'datedim' to datetime if it's in string format
# Convert 'datedim' to datetime if it's in string format
df['datedim'] = pd.to_datetime(df['datedim'], format='%Y-%m-%d')

# Filter rows where 'category_name' is "Water"
water_df = df[df['category_name'] == 'KTO']

# Group by 'datedim' and count unique IDs
water_counts_per_day = water_df.groupby('datedim')['id'].nunique().reset_index(name='count')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(water_counts_per_day['datedim'], water_counts_per_day['count'], marker='o')
plt.title('Total Count of Unique IDs for Water per Day')
plt.xlabel('Date')
plt.ylabel('Count')
plt.grid(True)
plt.show()