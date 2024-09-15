# %% 
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
	use_ip = request.remote_addr
	response = make_response(redirect("/hello"))
	response.set_cookie("user_ip", use_ip)

	return response

@app.route('/hello')
def hello():
	user_ip = request.cookies.get("user_ip")
	return f"Hello World test. Tu IP es: {user_ip}"