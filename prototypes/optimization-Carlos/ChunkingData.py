import pandas as pd

#this code splits up the larger data files into smaller, readable sizes. 

#below reads the file only in chunksize 10,000
df = pd.read_csv(
r'/usr/src/app/barrios-data/iss-data/csv/inventory_mgmt_system/inventory_mgmt_system_consumables_20220101-20230905.csv',
chunksize = 10000)

#below is a for loop that gets the chunks above and creates its own csv to place in the selected folder
for i, f in enumerate(df):
    f.to_csv(rf'/usr/src/app/barrios-data/iss-data/csv/inventory_mgmt_system/inv_mgmt_{i}.csv')

