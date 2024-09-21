import csv

trips = {}
calendar = {}
calendar_dates = {}
stops = {}

with open('GTFS/trips.txt', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		key = row['trip_id']
		row.pop('trip_id')
		trips[key] = row

with open('GTFS/calendar.txt', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		key = row['service_id']
		row.pop('service_id')
		calendar[key] = row

with open('GTFS/calendar_dates.txt', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		key = row['service_id']
		row.pop('service_id')
		calendar_dates[key] = row		

with open('GTFS/stops.txt', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		key = row['stop_id']
		row.pop('stop_id')
		stops[key] = row

# print(stops[list(stops.keys())[0]])

# print(stops['436'])

for stop in stops:
	if 'HURDMAN' in stops[stop]['stop_name']:
		print(stop, stops[stop])