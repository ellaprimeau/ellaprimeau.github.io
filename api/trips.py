import csv, json

class Trips:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r',encoding='utf-8') as f:
			reader = csv.DictReader(f, delimiter=',')
			for row in reader:
				key = row['trip_id']
				row.pop('trip_id')
				self.data[key] = row

	def list_trips(self):
		returnList = []
		for trip in self.data.keys():
			returnList.append(self.data[trip])
		return returnList

	def list_trips_by_route(self, route):
		returnList = []
		for trip in self.data.keys():
			if self.data[trip]['route_id'] == route:
				returnList.append(self.data[trip])
		return returnList

	def list_trips_by_shape(self, shape):
		returnList = []
		for trip in self.data.keys():
			if self.data[trip]['shape_id'] == shape:
				returnList.append(self.data[trip])
		return returnList

	def jsonDump(self):
		with open('api/gtfs/tripsDump.json', 'w+') as f:
			json.dump(self.data, f)
			f.close()
		print('json dump complete')

if __name__ == "__main__":
	localTrips = Trips('api/gtfs/trips.txt')
	print(len(localTrips.data.keys()))
	# localTrips.jsonDump()