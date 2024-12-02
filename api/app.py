from flask import Flask
import json
# from shapes import Shapes
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

@app.route("/api/shapeNames")
def getShapeNames():
	shapesQuery = fauna.paginate(fql('shapes.all() { shape_id }'))
	shapes = []
	for page in shapesQuery:
		for doc in page:
			shapes.append(doc['shape_id'])
	shapes.sort()
	return shapes

@app.route("/api/trip/<shape_id>")
def getTrips(shape_id):
	tripsQuery = fauna.paginate(fql('trips.shape_id("{}")'.format(shape_id)))
	# tripsQuery = fauna.paginate(fql('trips.route_id("400")'))
	trips = []
	services = {
		'H01S924S-Semaine-4-_24AUT-1111100-':'Weekday',
		'H01S024A-Dimanche-4-_24AUT-0000001-':'Saturday',
		'H01S024I-Dimanche-4-_24AUT-0000001-':'Sunday'
	}
	for page in tripsQuery:
		for doc in page:
			stopTimes = getStopTimes(doc['trip_id'])
			if(doc['service_id'] in services.keys()):
				trips.append([services[doc['service_id']],doc['route_id'],doc['trip_headsign'],stopTimes[0][0]['departure_time']])
	return trips

@app.route("/api/stop_times/<trip_id>")
def getStopTimes(trip_id):
	stopTimesQuery = fauna.paginate(fql('stop_times.trip_id("{}")'.format(trip_id)))
	stopTimes = []
	for page in stopTimesQuery:
		for doc in page:
			stopTimes.append(doc['stopTimes'])
	return stopTimes

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