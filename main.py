# %% 
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SupperSecretKey'

TODOS = ["Ir al cerro", "Estudiar flask", "Hacer pagina sensor"]

@app.errorhandler(404)
def not_found(error):
	return render_template("404.html", error=error)

@app.route('/')
def index():
	use_ip = request.remote_addr
	response = make_response(redirect("/hello"))
	# response.set_cookie("user_ip", use_ip)
	session["user_ip"] = use_ip	

	return response

@app.route('/hello')
def hello():
	# user_ip = request.cookies.get("user_ip")
	user_ip = session.get("user_ip")

	context = {"user_ip":user_ip, 
				  "TODOS":TODOS}

	return render_template("hello.html", **context)