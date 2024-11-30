from flask import Flask
import json
from shapes import Shapes
import requests
import os
from fauna import fql
from fauna.client import Client

app = Flask(__name__)
faunaDomain = os.environ.get('FAUNA_DB_DOMAIN')
faunaKey = os.environ.get('FAUNA_ADMIN_KEY')

localShapes = {}
fauna = Client(secret=faunaKey)

@app.route("/api/")
def hello_world():
	return("<p>hello world</p>")

@app.route("/api/shape/<shape_id>")
def getShape(shape_id):
	shape = fauna.query(fql('shapes.shape_id("{}")'.format(shape_id))).data.data[0].get('shape')
	returnShapes = []
	for seg in shape:
		returnShapes.append([seg['shape_pt_lon'],seg['shape_pt_lat']])
	return returnShapes


# @app.route("/api/getShapes")
# def getShapes():
	# if localShapes == {}:
		# s = requests.get('https://media.githubusercontent.com/media/ellaprimeau/GTFS/refs/heads/main/shapes.txt', stream=True).text
		# with open('./gtfs/shapes.txt', 'w+') as f:
			# f.write(s)
		# localShapes = Shapes('./gtfs/shapes.txt')
		# return localShapes.get('shp-10-03')
	# else:
		# return