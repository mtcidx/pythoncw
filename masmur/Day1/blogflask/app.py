# Jalanin flask
# flask run -h 0.0.0.0 -p 4000
# Buka di browser http://locallhost:4000
from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    list_menu =  requests.get('http://localhost:5555/api/v1/get_categories/').json()
    return render_template('index.html', menu = list_menu)
