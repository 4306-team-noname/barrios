import pandas as pd
import numpy as np
from dask import dataframe as dd
from prophet import Prophet
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
print("Running FB Prophet test:")
print(df.head())

column_names_df = pd.read_excel('iss-data/Data Dictionary.xlsx', sheet_name = "IMS Data Dictionary", usecols = [0])

column_names = column_names_df['Field'].to_numpy()

dask_df = dd.read_csv(
  'iss-data/csv/inventory_mgmt_system_consumables_20220101-20230905.csv',
  names = column_names,
  header = None,
  dtype={'fill_status': 'object', 'serial_number': 'object'},
  blocksize="100MB"
  )

print(dask_df.tail(20))
