from emmett import App, Field, Form, request, session, url
from emmett.sessions import SessionManager
from controllers.dashboard_controller import DashboardController
app = App(__name__)


dash_controller = DashboardController()

static = url('static/')  # defining a static route is so very simple

app.pipeline = [SessionManager.cookies('secretkey')]


@app.route('/')
async def home():
    session.counter = (session.counter or 0) + 1
    return {'count': session.counter}


@app.route('/dashboard')
async def dashboard():  # okay, so the method matches the template name, fun
    return {'name': 'Pie Hole'}


@app.route('/form')
async def form():
    simple_form = await Form({
        'name': Field()
    })
    if simple_form.accepted:
        print('Okay')
    return dict(form=simple_form)


@app.route('/static-form')
async def static_form():
    params = await request.body_params
    input_name = params.name or 'Nobody!'
    return {'name': input_name}
