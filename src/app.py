from emmett import App, response, url
from emmett.orm import Database


app = App(__name__)
app.config.url_default_namespace = "main"
app.config_from_yaml('db.yml', 'db')
db = Database(app)

url('static', 'static/')

# import controllers to expose routing functions
from controllers import data, flightplan, forecast, main, usage