from flask import render_template, Flask
from . import db


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def map_view():
    return render_template('map.html')

db.init_app(app)