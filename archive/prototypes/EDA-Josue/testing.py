import pandas
#dataframe = pandas.read_csv("../../iss-data\csv\ims_consumables_category_lookup.csv")
dataframe = pandas.read_csv("../../iss-data\csv\iss_flight_plan_20220101-20251231.csv")

nameOfColumn = 'event'

filtered_Dataframe = dataframe[dataframe[nameOfColumn].notna()]

pandas.set_option('display.max_rows', None)
print(filtered_Dataframe)

num_rows_printed = filtered_Dataframe.shape[0]
print(f"Number of rows printed: {num_rows_printed}")