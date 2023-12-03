import pandas as pd

# Read the CSV file
df = pd.read_csv('../../iss-data\csv\eda\sorted_crew_alpha.csv')

# Define a function to map nationalities
def map_nationality(nationality):
    usos_nationalities = {'CSA', 'ESA', 'JAXA', 'NASA', 'USOS', 'ASI', 'NASA, USOS','Commercial'}
    ru_nationalities = {'RSA', 'SFP'}
    
    if nationality in usos_nationalities:
        return 'USOS'
    elif nationality in ru_nationalities:
        return 'RU'
    else:
        return None  # Ignore other nationalities

# Apply the mapping function to the 'nationality_category' column
df['nationality_category'] = df['nationality_category'].apply(map_nationality)

# Group by 'datedim' and 'nationality_category' and sum the 'crew_count'
result_df = df.groupby(['datedim', 'nationality_category']).sum().reset_index()

# Save the modified DataFrame to a new CSV file
result_df.to_csv('../../iss-data\csv\eda\sorted_nationalities.csv', index=False)

