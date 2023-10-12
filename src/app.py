from emmett import App
from controllers import AnalysisController, UserController, UserDataController
from services import AnalysisService, UserService, UserdataService
from repositories import AnalysisRepository, UserRepository, UserdataRepository

app = App(__name__)

# https://barrios.com/upload

@app.route('/')
async def home():
  return 'This is the beginning of the implementation'

@app.route('/upload')
async def upload():
  pass