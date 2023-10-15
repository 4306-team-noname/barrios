from app import app
from emmett import response

usage = app.module(__name__, 'usage', url_prefix='usage', template_folder='pages/usage')

@usage.route('/')
async def index():
    response.meta.title = 'Usage | ISS Consumables'
    return {}