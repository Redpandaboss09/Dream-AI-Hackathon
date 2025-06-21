from flask import render_template, Flask

app = Flask(__name__)

"""
@app.route('/')
def index():
    return render_template('index.html')
"""

@app.route('/')
def map_view():
    return render_template('map.html')