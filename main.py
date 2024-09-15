# %% 
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

TODOS = ["Ir al cerro", "Estudiar flask", "Hacer pagina sensor"]

@app.route('/')
def index():
	use_ip = request.remote_addr
	response = make_response(redirect("/hello"))
	response.set_cookie("user_ip", use_ip)

	return response

@app.route('/hello')
def hello():
	user_ip = request.cookies.get("user_ip")

	context = {"user_ip":user_ip, 
				  "TODOS":TODOS}

	return render_template("hello.html", **context)