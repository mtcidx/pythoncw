import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    categories = requests.get('http://localhost:5555/api/v1/get_categories')
    categories = categories.json()
    print(categories)
    return render_template('index.html', menu=categories)
