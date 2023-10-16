from emmett import App, response, url
from emmett.orm import Database
from models.User import User
from models.FlightPlanEntry import FlightPlanEntry

app = App(__name__)
app.config.url_default_namespace = "main"
app.config_from_yaml('db.yml', 'db')

db = Database(app)
# db.define(FlightPlanEntry)
url('static', 'static/')

# import controllers to expose routing functions
from controllers import data, flightplan, forecast, main, usage