from app import app, auth
from emmett import response, url
from emmett.pipeline import RequirePipe


forecast = app.module(
    __name__, "forecast", url_prefix="forecast", template_folder="pages/forecast"
)

forecast.pipeline = [RequirePipe(auth.is_logged, url("auth/login"))]


@forecast.route("/")
async def index():
    response.meta.title = "Forecast | ISS Consumables"
    return {}
