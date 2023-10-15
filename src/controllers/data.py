import uuid
from app import app
from emmett import request, response
from emmett.helpers import stream_file

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
    await file.save(f"storage/{id}.{ext}")
    return {'name': file.filename, 'ext': ext, 'type': type}