from app import app
from emmett import response

@app.route('/')
async def index():
    response.meta.title = 'Dashboard | ISS Consumables'
    return {}