from flask import Flask

app = Flask(__name__)

@app.route("/api/")
def hello_world():
	return("<p>hello world</p>")

@app.route("/api/test")
def test():
	return("test")