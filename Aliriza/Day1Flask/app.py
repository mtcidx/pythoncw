from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    var_menu = ['Sport','Finance']
    return render_template ('index.html',menu = var_menu)