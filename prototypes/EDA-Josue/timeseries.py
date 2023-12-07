import pandas as pd
import numpy as np

def derive_ims_df_from_csv(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Drop columns that have a status that is not useful
    df = df[df["status"] != "Discard"]
    df = df[df["status"] != "Return"]
    df = df[df["status"] != np.nan]

    # Convert datetimes to plain date so multiple
    # values that fall on a single day can be grouped
    # or discarded.
    df["datedim"] = pd.to_datetime(df["datedim"]).dt.date

    # Get rid of any remaining duplicates. If they have the same
    # id, datedim and status, they're the same thing and shouldn't
    # be counted twice.
    unique = df.drop_duplicates(
        subset=["id", "datedim", "status", "category_name"]
    )

    # First grouping. Group by datedim first, but make sure to
    # bring along the other relevant columns. Reindex to rename
    # the group count column to `actual_value` for use in plotting.
    group_one = (
        unique.groupby(["datedim", "id", "category_name"])
        .size()
        .reset_index(name="actual_value")
    )

    # Group again on datedim and category name. (Is this right?)
    grouped_df = (
        group_one.groupby(["datedim", "category_name"])
        .agg({"actual_value": "sum"})
        .reset_index()
    )

    # We don't have a predicted value in this dataset. We'll be using
    # something else for a value we attempt to forecast ourselves.
    grouped_df["predicted_value"] = None

    # Rename datedim to date so our plotting method doesn't have to do it
    grouped_df = grouped_df.rename(columns={"datedim": "date"})

    # Done
    return grouped_df

# Example usage
csv_file_path = "../../iss-data\csv\eda\stored-datedim.csv"
result_df = derive_ims_df_from_csv(csv_file_path)
print(result_df)