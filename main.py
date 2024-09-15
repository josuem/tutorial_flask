# %% 
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
	IP_USER = request.remote_addr
	return f"Hello World test. Tu IP es: {IP_USER}"