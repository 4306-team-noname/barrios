import pandas as pd

# Define the headers
headers = [
    "datedim", "id", "id_parent", "id_path", "tree_depth", "tree", 
    "part_number", "serial_number", "location_name", "original_ip_owner", 
    "current_ip_owner", "operational_nomenclature", "russian_name", 
    "english_name", "barcode", "quantity", "width", "height", "length", 
    "diameter", "calculated_volume", "stwg_ovrrd_vol", "children_volume", 
    "stwg_ovrrd_chldren_vol", "ovrrd_notes", "volume_notes", "expire_date", 
    "launch", "type", "hazard", "state", "status", "is_container", 
    "is_moveable", "system", "subsystem", "action_date", "move_date", 
    "fill_status", "categoryID", "category_name"
]

# Load the CSV file without headers
file_path = '../../iss-data\csv\eda\inventory_mgmt_system_consumables_20220101-20230905.csv'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv(file_path, header=None)

# Add headers to the DataFrame
df.columns = headers

# Save the DataFrame back to a new CSV file
output_file_path = '../../iss-data\csv\eda\ims_with_headers.csv'  # Replace with your desired output file path
df.to_csv(output_file_path, index=False)

print("Headers added successfully.")
