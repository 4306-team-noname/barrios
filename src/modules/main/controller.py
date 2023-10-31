from app import app
from emmett import response


@app.route("/")
async def index():
    response.meta.title = "ISS Consumables Analytics"
    return {}
