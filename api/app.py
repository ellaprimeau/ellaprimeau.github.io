from flask import Flask
import json
from shapes import Shapes
import requests

app = Flask(__name__)

localShapes = {}

@app.route("/api/")
def hello_world():
	return("<p>hello world</p>")

@app.route("/api/test")
def test():
	return {"information": "yes"}

@app.route("/api/getShapes")
def getShapes():
	if localShapes == {}:
		s = requests.get('https://media.githubusercontent.com/media/ellaprimeau/GTFS/refs/heads/main/shapes.txt', stream=True).text
		with open('./gtfs/shapes.txt', 'w+') as f:
			f.write(s)
		# localShapes = Shapes('./gtfs/shapes.txt')
		# return localShapes.get('shp-10-03')
	else:
		return