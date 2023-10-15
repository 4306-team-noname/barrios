from app import app
from emmett import response

forecast = app.module(__name__, 'forecast', url_prefix='forecast', template_folder='pages/forecast')

@forecast.route('/')
async def index():
  response.meta.title = 'Forecast | ISS Consumables'
  return {}