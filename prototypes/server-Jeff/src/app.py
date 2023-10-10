from emmett import App, Field, Form, request, session, url
from emmett.sessions import SessionManager
from controllers.dashboard_controller import DashboardController
import pytest


app = App(import_name='Barrios')


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
# The Emmett Form is a nice utility that can
# hook directly into the database. I'm not sure it
# matches up with out use case, though.
async def form():
    simple_form = await Form({
        'name': Field()
    })
    if simple_form.accepted:
        print('Okay')
    return dict(form=simple_form)


@app.route('/static-form')
# Just a static form!
async def static_form():
    params = await request.body_params
    input_name = params.name or 'Nobody!'
    return {'name': input_name}


@app.route('/htmx')
# Testing an HTMX interaction
async def htmxsource():
    return {}


@app.route('/count', methods='post')
async def count():
    params = await request.body_params
    click_count = (int(params.click_count) or 0) + 1
    return {'count': click_count}


@app.route('/decrement', methods='post')
async def decrement():
    params = await request.body_params
    click_count = (int(params.click_count) or 0) - 1
    return {'count': click_count}
