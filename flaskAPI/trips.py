import csv

class Trips:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.DictReader(f, delimiter=',')
			for row in reader:
				key = row['trip_id']
				row.pop('trip_id')
				self.data[key] = row

	def list_trips(self):
		for trip in self.data.keys():
			print(self.data[trip])

	def list_trips_by_route(self, route):
		returnList = []
		for trip in self.data.keys():
			if self.data[trip]['route_id'] == route:
				returnList.append(self.data[trip])
		return returnList