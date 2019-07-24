import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    categories = requests.get('http://localhost:5000/api/v1/get_categories')
    categories = categories.json()
    print(categories)
    return  render_template('index.html', menu=categories)

if __name__ == ' main ':
    app.run(debug=True)