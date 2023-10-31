from app import app, auth, url
from emmett import response
from emmett.pipeline import RequirePipe

flightplan = app.module(
    __name__, "flightplan", url_prefix="flightplan", template_folder="pages/flightplan"
)

flightplan.pipeline = [RequirePipe(auth.is_logged, url("auth/login"))]


@flightplan.route("/")
async def index():
    response.meta.title = "Flight Plan | ISS Consumables"
    return {}
