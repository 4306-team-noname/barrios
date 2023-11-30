import pandas as pd

# Load the CSV file into a DataFrame
file_path = '../../prototypes\EDA-Josue\ims_with_headers.csv'
df = pd.read_csv(file_path)

# Assuming the CSV file has a column named 'id' and another column named 'calculated_volume'
# Adjust column names accordingly based on your actual CSV structure

# Sort the DataFrame based on the 'id' column
df.sort_values(by='id', inplace=True)

# Initialize variables to track historical usage rates
current_serial_number = None
historical_usage = []

# Iterate through the DataFrame to calculate historical usage rates
for index, row in df.iterrows():
    if current_serial_number is None or row['id'] != current_serial_number:
        # If a new serial number is encountered, save the historical usage rate
        if current_serial_number is not None:
            historical_usage.append({'id': current_serial_number, 'HistoricalUsage': usage_rate})
        current_serial_number = row['id']
        usage_rate = 0  # Reset usage rate for the new serial number

    # Accumulate the usage for the current serial number
    usage_rate += row['quantity']

# Save the last serial number's historical usage rate
historical_usage.append({'id': current_serial_number, 'HistoricalUsage': usage_rate})

# Create a new DataFrame from the historical usage data
historical_df = pd.DataFrame(historical_usage)

# Save the results to a new CSV file or perform further analysis as needed
historical_df.to_csv('../../prototypes\EDA-Josue\historical_usage.csv', index=False)
