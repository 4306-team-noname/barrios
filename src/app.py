from emmett import App, response, url
from emmett.orm import Database
from emmett.tools import Auth
from models.User import User
from utils.model_utils import define_models
from utils.data_dictionary import get_dictionary

app = App(__name__)
app.config.url_default_namespace = "main"
app.config.auth.single_template = True
app.config.auth.registration_verification = False
app.config.auth.hmac_key = 'SpaceMadness1969!'

app.config_from_yaml('db.yml', 'db')
db = Database(app)

auth = Auth(app, db, user_model=User)

db = define_models(db)
app.pipeline = [db.pipe]

# Set static directory for serving
# scripts, css files, images, etc.
url('static', 'static/')

# import controllers to expose routing functions
from controllers import data, flightplan, forecast, main, usage