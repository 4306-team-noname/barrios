from emmett import App

app = App(__name__)


@app.route('/')
async def hello():
    return "Hello world"


@app.route('/<str:msg>')
async def echo(msg):
    return dict(message=msg)
