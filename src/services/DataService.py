from cases import to_snake
from emmett.orm import Database
import numpy as np
import pandas as pd
from typing import Dict

from utils.model_utils import insert_model
from utils.Result import Result
from utils.data_dictionary import get_dictionary

class DataService():
    db: Database
    dictionary: Dict
    def __init__(self, db) -> None:
        self.db = db
        self.dictionary = get_dictionary()
        pass
    
    def save_file_data(self, file_location):
        file_df = pd.read_csv(file_location)
        columns = np.asarray(file_df.columns.to_numpy())

        # figure out the model name according to
        # a matching dictionary entry
        model_name = None

        for key in self.dictionary.keys():
        # check the field names to determine what type of model
        # the data represents
            dictionary_entry = self.dictionary[key]
            entry_columns = dictionary_entry['columns']
            dictionary_columns_arr = np.asarray(entry_columns)
            matches = np.array_equal(columns, dictionary_columns_arr)

            if matches == True:
                model_name = dictionary_entry['model_name']

        if model_name == None:
            return {'ok': False, 'value': None, 'error': "The uploaded file doesn't match any known user data types"}

        # iterate over dataframe and use values in each row to
        # instantiate and persist the appropriate models.
        file_df = file_df.reset_index()
        file_df = file_df.replace({np.nan:None})

        # add 'upload' as a column value
        # columns = np.append(columns, 'upload')

        for index, row in file_df.iterrows():
            np_row_arr = row.to_numpy()

            # drop the index from np_row_arr
            np_row_arr = np_row_arr[1:]

            # TODO: Figure out what to show the user if a subset
            # of the rows conflicts with stored entries
            model_result = insert_model(model_name, columns, np_row_arr)
            # print(f'model_result: {model_result}')

            if model_result['ok'] == False:
                error = model_result['error']
                key = model_result['error_field']
                return {'ok': False, 'value': None, 'error': f"{key}: {error}"}

        file_df = file_df.reset_index(drop=True)
        file_np = file_df.to_numpy()
        file_list = file_np.tolist()
        table_cols = []
        for col in columns:
            snake = to_snake(col)
            no_under = snake.replace('_', ' ')
            table_cols.append(no_under)

        return {
            'ok': True,
            'value':{
                'table_cols': table_cols,
                'dataframe': file_df,
                'table_list': file_list
                },
            'error': None
            }