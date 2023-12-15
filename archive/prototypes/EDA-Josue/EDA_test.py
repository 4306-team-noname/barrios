import pandas
import matplotlib.pyplot as plt
import seaborn as sns
dataframe = pandas.read_csv("../../iss-data\csv\ims_consumables_category_lookup.csv")
#dataframe = pandas.read_csv("../../iss-data\csv\iss_flight_plan_20220101-20251231.csv")
#dataframe = pandas.read_csv("../../iss-data\csv\inventory_mgmt_system\inv_mgmt_0.csv")
#dataframe = pandas.read_csv("../../iss-data\csv\stored_items_only\stored_itm_only_0.csv")
#dataframe = pandas.read_csv("../../iss-data\csv\sthresholds_limits_definition.csv")
#dataframe = pandas.read_csv("../../iss-data\csv\s_us_rs_weekly_consumable_gas_summary_20220102-20230903.csv")

# Define the threshold for filtering null values
threshold = 0.4
max_null_values = dataframe.shape[1] * threshold

# Filter the dataframe rows based on null value threshold
filtered_out_rows = dataframe[dataframe.isnull().sum(axis=1) < max_null_values]

# Identify columns filtered out
columns_with_few_nulls = dataframe.columns[dataframe.isnull().mean() < threshold]

# Main loop for user interaction
while True:
    print("\nOptions:")
    print("1. Show filtered rows")
    print("2. Show unfiltered rows")
    print("3. Show filtered out columns")
    print("4. Describe statistics")
    print("5. Data Visualization")
    print("6. Dates")
    print("7. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        print(filtered_out_rows)
        num_rows_printed = filtered_out_rows.shape[0]
        print(f"Number of rows printed: {num_rows_printed}")
    elif choice == '2':
        print(dataframe)
        num_rows_printed = dataframe.shape[0]
        print(f"Number of rows printed: {num_rows_printed}")
    elif choice == '3':
        print("Columns with less than 40% null values:")
        for column in columns_with_few_nulls:
            print(column)
    elif choice == '4':
        print(dataframe.describe())
    
    elif choice == '5':
        print("\nData Visualization Options:")
        print("1. Histogram of a numeric column")
        print("2. Box plot of a numeric column")
        print("3. Correlation heatmap")
        vis_choice = input("Enter your data visualization choice (1/2/3): ")
        if vis_choice == '1':
            # Data Visualization: Histogram of a numeric column
            column_name = input("Enter the name of the numeric column: ")
            if column_name in dataframe.columns and pandas.api.types.is_numeric_dtype(dataframe[column_name]):
                dataframe[column_name].hist()
                plt.xlabel(column_name)
                plt.ylabel("Frequency")
                plt.title(f"Histogram of {column_name}")
                plt.show()
            else:
                print("Invalid column name or non-numeric column.")
        elif vis_choice == '2':
            # Data Visualization: Box plot of a numeric column
            column_name = input("Enter the name of the numeric column: ")
            if column_name in dataframe.columns and pandas.api.types.is_numeric_dtype(dataframe[column_name]):
                sns.boxplot(x=dataframe[column_name])
                plt.xlabel(column_name)
                plt.title(f"Box Plot of {column_name}")
                plt.show()
            else:
                print("Invalid column name or non-numeric column.")
        elif vis_choice == '3':
            # Data Visualization: Correlation heatmap
            numeric_columns = dataframe.select_dtypes(include=['float64', 'int64'])
            corr_matrix = numeric_columns.corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            plt.show()
        else:
            print("Invalid data visualization choice.")

    elif choice == '6':
        column_name = input("Enter the name of the date column: ")
        if column_name in filtered_out_rows.columns:
            dates_present = filtered_out_rows[column_name]
            dates_present = pandas.to_datetime(dates_present)
            date_counts = dates_present.value_counts().sort_index()
            
            plt.figure(figsize=(12, 6))
            plt.plot(date_counts.index, date_counts.values, marker='o', linestyle='-', color='b')
            plt.title('Timeline of Dates Present')
            plt.xlabel('Date')
            plt.ylabel('Frequency')
            plt.xticks(rotation=45)
            plt.show()

    elif choice == '7':
        print("Ending Test.")
        break
    else:
        print("Invalid choice")