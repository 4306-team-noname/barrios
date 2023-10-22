import uuid, csv
import numpy as np
import pandas as pd

from app import app
from emmett import request, response
from emmett.helpers import stream_file
from emmett.helpers import flash
from utils.data_dictionary import get_dictionary
from utils.model_utils import insert_model

# models = [FlightPlanCrewEntry, FlightPlanEntry, GasEntry, IMSEntry, WaterEntry]

data = app.module(__name__, 'data', url_prefix='data', template_folder='pages/data')


@data.route('/')
async def index():
    response.meta.title = 'Data | ISS Consumables'
    return {}

@data.route('/upload', methods='post')
async def upload():
    response.meta.title = 'Upload | ISS Consumables'
    files = await request.files
    file = files.file
    id = str(uuid.uuid4())
    type = file.content_type.split('/',1)[0]
    ext = file.content_type.split('/',1)[1]

    if ext != 'csv':
        return flash('Data must be in CSV format!', 'error')

    # otherwise, upload to a temp folder
    temp_file_location = f"storage/{id}.{ext}"
    await file.save(temp_file_location)

    # now, read the saved temp file and store its columns as a list
    file_df = pd.read_csv(temp_file_location)
    columns = np.asarray(file_df.columns.to_numpy())
    
    # get the stored data dictionary
    data_dictionary = get_dictionary()
    model_name = None

    for key in data_dictionary.keys():
    # check the field names to determine what type of model
    # the data represents
        dictionary_entry = data_dictionary[key]
        entry_columns = dictionary_entry['columns']
        dictionary_columns_arr = np.asarray(entry_columns)
        matches = np.array_equal(columns, dictionary_columns_arr)
        if matches == True:
            model_name = dictionary_entry['model_name']
    
    if model_name is None:
        return flash("Error: CSV file doesn't match any known user data types", "error")
    # instantiate and persist the appropriate models.
        


    # return an HTML table (possibly paginated)

    # delete the temporary file
    return {'name': file.filename, 'ext': ext, 'type': type}
