from app import app
from emmett import response

data = app.module(__name__, 'data', url_prefix='data', template_folder='pages/data')

@data.route('/')
async def index():
    response.meta.title = 'Data | ISS Consumables'
    return {}

@data.route('/upload', methods='post')
async def upload():
    return {}