import uuid, csv
from app import app
from emmett import request, response
from emmett.helpers import stream_file
from models import FlightPlanCrewEntry, FlightPlanEntry, GasEntry, IMSEntry, WaterEntry

models = [FlightPlanCrewEntry, FlightPlanEntry, GasEntry, IMSEntry, WaterEntry]

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
    # return an error if not csv
    # otherwise, upload to a temp folder
    temp_file_location = f"storage/{id}.{ext}"
    await file.save(temp_file_location)
    # read the file from disk
    # Note: encoding='utf-8-sig' is important here
    #       it removes `\ufeff` from fields
    fields = []
    with open(temp_file_location, encoding='utf-8-sig', newline='') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
        fields = data[0].keys()
        print(fields)
    # check the field names to determine what type of model
    # the data represents

    # instantiate and persist the appropriate models.

    # return an HTML table (possibly paginated)

    # delete the temporary file
    return {'name': file.filename, 'ext': ext, 'type': type}
