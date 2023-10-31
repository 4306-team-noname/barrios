from app import app, auth, url
from emmett import response
from emmett.pipeline import RequirePipe

dashboard = app.module(
    __name__, "dashboard", url_prefix="/dashboard", template_folder="pages/dashboard"
)

dashboard.pipeline = [RequirePipe(auth.is_logged, url("auth/login"))]


@dashboard.route("/")
async def index():
    response.meta.title = "Dashboard | ISS Consumables"
    return {}
