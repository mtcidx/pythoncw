import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # http://localhost:5000/api/v1/get_categories
    categories = requests.get('http://localhost:5000/api/v1/get_categories')
    categories = categories.json()

    return render_template('index.html', menu=categories)
