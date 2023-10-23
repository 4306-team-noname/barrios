import numpy as np
import pandas as pd
from typing import Final
from app import app, db

from emmett import request, response, session
from emmett.helpers import stream_file
from emmett.helpers import flash
from result import Result, Ok, Err
from utils.data_dictionary import get_dictionary
from utils.model_utils import insert_model
from services.UploadService import UploadService

data = app.module(__name__, 'data', url_prefix='data', template_folder='pages/data')


@data.route('/')
async def index():
    response.meta.title = 'Data | ISS Consumables'
    return {}

@data.route('/upload', methods='post')
async def upload():
# This route handles uploading a new file and persisting
# its data to a database
# TODO: Consider moving the upload & persistence logic
# into services (UploadService, UserDataService)
    response.meta.title = 'Upload | ISS Consumables'
    storage_path: Final = 'storage' # TODO: set as environment variable?
    upload_service = UploadService(db, storage_path, ['csv'])

    files = await request.files
    file = files.file
    ext = file.content_type.split('/',1)[1]

    upload_result = await upload_service.create_upload(file)
    print(upload_result)
    temp_file_location: str = None
    upload_id: int = None

    match upload_result['ok']:
        case True:
            temp_file_location = upload_result['value']['temp_file_location']
            upload_id = upload_result['value']['id']
        case False:
            # return flash("Could not upload the file", 'error')
            print("Error: Could not upload the file")
        
    # print(session)


    file_df = pd.read_csv(temp_file_location)
    columns = np.asarray(file_df.columns.to_numpy())

    # get the stored data dictionary
    data_dictionary = get_dictionary()

    # we'll figure out the model name according to
    # a matching dictionary entry
    model_name = None

    for key in data_dictionary.keys():
    # check the field names to determine what type of model
    # the data represents
        dictionary_entry = data_dictionary[key]
        entry_columns = dictionary_entry['columns']
        dictionary_columns_arr = np.asarray(entry_columns)
        # print(dictionary_columns_arr)
        print(columns)
        matches = np.array_equal(columns, dictionary_columns_arr)

        if matches == True:
            model_name = dictionary_entry['model_name']

    if model_name == None:
        print("Error: The uploaded file doesn't match any known user data types")
        return flash("The uploaded file doesn't match any known user data types", "error")
    # iterate over dataframe and use values in each row to
    # instantiate and persist the appropriate models.
    file_df = file_df.reset_index()
    file_df = file_df.replace({np.nan:None})

    # add 'upload' as a column value
    columns = np.append(columns, 'upload')

    for index, row in file_df.iterrows():
        np_row_arr = row.to_numpy()

        # drop the index from np_row_arr
        np_row_arr = np_row_arr[1:]

        # append upload id as field value
        np_row_arr = np.append(np_row_arr, upload_id)

        # TODO: Figure out what to show the user if a subset
        # of the rows conflicts with stored entries
        model_result = insert_model(model_name, columns, np_row_arr)
        print(f'model_result: {model_result}')

        if model_result['ok'] == False:
            error = model_result['error']
            key = model_result['error_field']
            print(f'{key}: {error}')
            # pass
            # return flash('The uploaded data conflicts with stored data', 'error')

    # delete the temporary file
    upload_service.delete_temp_file(temp_file_location)

    # return an HTML table (possibly paginated, in the case of thousands of rows)
    return {'name': file.filename, 'ext': ext, 'type': type, 'dataframe': file_df}
