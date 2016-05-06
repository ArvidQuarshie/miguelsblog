#returns string to be displayed on the client's browser
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Arvid'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
