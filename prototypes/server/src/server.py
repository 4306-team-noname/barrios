from sanic import Request, Sanic, Blueprint
from sanic_ext import Config, render
from .controllers.HomeController import HomeController

app = Sanic('barrios')

# set path for static files
app.static('/public/', 'src/public')

# Note: Default path for all templates is `templates`
# prepend '/src' so everything works as expected
app.extend(config=Config(templating_path_to_templates='src/templates'))


# Define middleware, if necessary

# Define blueprints (associated routing)

home_bp = Blueprint('home_blueprint')
analyze_bp = Blueprint('analyze_blueprint')
forecast_bp = Blueprint('forecast_blueprint')

# Base route and controller


@home_bp.route('/')
async def home_handler(request):
    return await render('home.html', context={}, status=200)
# app.add_route(HomeController.as_view(), '/')


app.blueprint(home_bp)
app.blueprint(analyze_bp)
app.blueprint(forecast_bp)
