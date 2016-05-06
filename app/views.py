#returns string to be displayed on the client's browser
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
