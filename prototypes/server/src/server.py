from sanic import Request, Sanic, Blueprint
from sanic_ext import Config, render

app = Sanic('barrios')

# set path for static files
app.static('/public/', 'src/public')

# Note: Default path for all templates is `templates`
# prepend '/src' so everything works as expected
app.extend(config=Config(templating_path_to_templates='src/templates'))


# Define middleware, if necessary

# Define blueprints (associated routing)

analyze_bp = Blueprint('analyze_blueprint')
forecast_bp = Blueprint('forecast_blueprint')

app.blueprint(analyze_bp)
app.blueprint(forecast_bp)


# Base route


@app.get('/')
async def home(request):
    return await render('home.html', context={}, status=200)
