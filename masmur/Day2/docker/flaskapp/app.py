# Jalanin flask
# flask run -h 0.0.0.0 -p 4000
# Buka di browser http://locallhost:4000
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
