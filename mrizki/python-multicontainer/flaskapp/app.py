from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    return ("Hello World")

if __name__ == ' app ':
    app.run(debug=True)