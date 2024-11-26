from flask import Flask
import json

app = Flask(__name__)

@app.route("/api/")
def hello_world():
	return("<p>hello world</p>")

@app.route("/api/test")
def test():
	return {"information": "yes"}