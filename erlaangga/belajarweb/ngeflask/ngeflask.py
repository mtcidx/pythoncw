from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
	#the_menu = ['Hmmmm', 'Iyayayaya']
	#return render_template('index.html', menu=the_menu)
	return '<h1 style="text-align: center;">"Hello wong!</h1>'

app.run(host='0.0.0.0', debug=True, threaded=True)
