import pandas as pd

path = r'C:\Users\cicic\OneDrive\Desktop\Barrios_Project\barrios\iss-data\csv\inventory_mgmt_system\inv_mgmt_0.csv'

df = pd.read_csv(path)

for i, f in enumerate(df):
    f = pd.read_csv(path, usecols=[1, i])
    f.to_csv(rf'C:\Users\cicic\OneDrive\Desktop\Barrios_Project\barrios\iss-data\csv\inv-mgmt_cols\inv_mgmt_0_{i}.csv')



