from emmett import App

app = App(__name__)

@app.route('/')
async def home():
  return 'This is the beginning of the implementation'