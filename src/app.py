from emmett import App
from controllers import AnalysisController, UserController, UserDataController
from services import AnalysisService, UserService, UserdataService
from repositories import AnalysisRepository, UserRepository, UserdataRepository

app = App(__name__)

@app.route('/')
async def home():
  return 'This is the beginning of the implementation'