from flask import Flask
import json, random
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

@app.route("/api/shapes/<route_id>")
def getShapesByRouteId(route_id):
	shapesQuery = fauna.paginate(fql('trips.route_id("{}") {{ shape_id, trip_headsign }}'.format(route_id)))
	shapes = []
	shapeIds = []
	colors = ['#F25DC5','#F2D45D','#5DF28A','#5D7AF2']
	i=0
	for page in shapesQuery:
		for doc in page:
			if doc['shape_id'] not in shapeIds:
				shapes.append({
					'shape_id': doc['shape_id'],
					'color': colors[i%len(colors)],
					'shape_headsign': doc['trip_headsign']
				})
				shapeIds.append(doc['shape_id'])
				i+=1
	return shapes
	# return sorted(shapes, key=lambda i: i['shape_id'])

@app.route("/api/getRoutes")
def getRoutes():
	routesQuery = fauna.paginate(fql('routes.all() { route_id, route_long_name}'))
	routes = []
	for page in routesQuery:
		for doc in page:
			routes.append({
				'route_id': int(doc['route_id']),
				'route_long_name': doc['route_long_name'],
				'str': '{} {}'.format(doc['route_id'], doc['route_long_name'])
				})
	return sorted(routes, key=lambda i: i['route_id'])

@app.route("/api/stop_times/byShape/<shape_id>")
def getStopTimesByShape(shape_id):
	stopTimesQuery = fauna.paginate(fql("""
		let tripList = trips.shape_id('{}').toSet() {{ trip_id, route_id, trip_headsign, service_id }}

		tripList.map(item => {{
		  'route_id': item.route_id,
		  'trip_headsign': item.trip_headsign,
		  'service_id': item.service_id,
		  'stop_times': stop_times.trip_id(item.trip_id).first()}})
	""".format(shape_id)))
	stopTimes = []
	services = {
		'H01S924S-Semaine-4-_24AUT-1111100-':'Weekday',
		'H01S024A-Dimanche-4-_24AUT-0000001-':'Saturday',
		'H01S024I-Dimanche-4-_24AUT-0000001-':'Sunday'
	}
	for page in stopTimesQuery:
		for doc in page:
			if doc['service_id'] in services:
				stopTimes.append([services[doc['service_id']],doc['route_id'],doc['trip_headsign'],doc['stop_times']['stopTimes'][0]['departure_time']])

	return sorted(stopTimes, key=lambda i: int(i[-1][:2]))


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