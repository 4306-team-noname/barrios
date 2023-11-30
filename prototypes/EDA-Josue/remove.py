import pandas as pd

# Load the CSV file with headers
file_path = '../../prototypes/EDA-Josue/ims_with_headers.csv'
df = pd.read_csv(file_path)

# Define the columns to keep
columns_to_keep = [
    'datedim', 'id', 'part_number', 'serial_number', 'current_ip_owner', 
    'english_name', 'launch', 'state', 'status', 'action_date', 
    'move_date', 'fill_status', 'categoryID', 'category_name'
]

# Select only the columns to keep
df_filtered = df[columns_to_keep]

# Save the filtered DataFrame to a new CSV file
output_file_path = '../../prototypes/EDA-Josue/ims_filtered.csv'
df_filtered.to_csv(output_file_path, index=False)

print("Columns filtered successfully.")
