from app import app
from emmett import response


flightplan = app.module(
        __name__,
        'flightplan', url_prefix='flightplan',
        template_folder='pages/flightplan'
        )


@flightplan.route('/')
async def index():
    response.meta.title = 'Flight Plan | ISS Consumables'
    return {}

