from utils.module_factory import import_app_modules
from emmett import App, url
from emmett.orm import Database
from emmett.tools import Auth
from emmett.sessions import SessionManager
from models.User import User
from utils.model_utils import define_models
from utils.setup_app_commands import setup_app_commands

app = App(__name__)
app.config.url_default_namespace = "main"

app.config_from_yaml("auth.yml", "auth")
app.config_from_yaml("db.yml", "db")

if app.config.auth:
    app.config.auth.routes_paths = {
        "login": "/login",
        "logout": "/logout",
        "registration": "/signup",
    }

db = Database(app)
auth = Auth(app, db, user_model=User)
db = define_models(db)
app.pipeline = [SessionManager.cookies("TeamNonameBarrios"), db.pipe, auth.pipe]
auth_routes = auth.module(__name__)


# Set static directory for serving
# scripts, css files, images, etc.
url("static", "static/")
setup_app_commands(app, db, auth)
# import controllers to expose routing functions
app_modules = import_app_modules()
