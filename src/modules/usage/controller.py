from app import app, auth
from emmett import response, url
from emmett.pipeline import RequirePipe

usage = app.module(__name__, "usage", url_prefix="usage", template_folder="pages/usage")

usage.pipeline = [RequirePipe(auth.is_logged, url("auth/login"))]


@usage.route("/")
async def index():
    response.meta.title = "Usage | ISS Consumables"
    return {}
