from flask import Flask, escape, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    menu = []

    menu = requests.get('http://127.0.0.1:8000/api/v1/get_categories/').json()
    # for categ in categories.json():
    #     menu.append(categ['title'])
    # import ipdb;ipdb.set_trace()
    # return 'Hello, ' + name
    return render_template('index.html', menu=menu)