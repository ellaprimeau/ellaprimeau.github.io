import csv
from routes import Routes
from trips import Trips
from shapes import Shapes
from pprint import pprint
import json

calendar = {}
calendar_dates = {}
stops = {}

routes = Routes('GTFS/routes.txt')
# routes.list_routes()

trips = Trips('GTFS/trips.txt')
# for trip in trips.list_trips_by_route('99'): print(trip['shape_id'],trip['trip_headsign'])

shapes = Shapes('GTFS/shapes.txt')
coords = []
for item in shapes.get('shp-110-04'):
	coords.append([float(item['shape_pt_lon']),float(item['shape_pt_lat'])])


with open('./coords.json', 'w+') as f:f.write(json.dumps(coords))


# with open('GTFS/trips.txt', 'r') as f:
# 	reader = csv.DictReader(f, delimiter=',')
# 	for row in reader:
# 		key = row['trip_id']
# 		row.pop('trip_id')
# 		trips[key] = row

# with open('GTFS/calendar.txt', 'r') as f:
# 	reader = csv.DictReader(f, delimiter=',')
# 	for row in reader:
# 		key = row['service_id']
# 		row.pop('service_id')
# 		calendar[key] = row

# with open('GTFS/calendar_dates.txt', 'r') as f:
# 	reader = csv.DictReader(f, delimiter=',')
# 	for row in reader:
# 		key = row['service_id']
# 		row.pop('service_id')
# 		calendar_dates[key] = row		

# with open('GTFS/stops.txt', 'r') as f:
# 	reader = csv.DictReader(f, delimiter=',')
# 	for row in reader:
# 		key = row['stop_id']
# 		row.pop('stop_id')
# 		stops[key] = row