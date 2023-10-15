from emmett import App, response, url
from emmett.orm import Database
from controllers import AnalysisController, UserController, UserDataController
from services import AnalysisService, UserService, UserdataService
from repositories import AnalysisRepository, UserRepository, UserdataRepository

app = App(__name__)
app.config_from_yaml('db.yml', 'db')
db = Database(app)

url('static', 'static/')


@app.route('/')
async def home():
    response.meta.title = 'Barrios Consumables Dashboard'
    return {}


@app.route('/upload')
# https://this_app.com/upload
async def upload():
    response.meta.title = 'Upload Data'
    pass
