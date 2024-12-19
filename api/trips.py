import csv, json

class Trips:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r',encoding='utf-8') as f:
			reader = csv.DictReader(f, fieldnames=[
				'route_id',
				'service_id',
				'trip_id',
				'trip_headsign',
				'shape_id',
				'block_id'], delimiter=',')

			# Since fieldnames were specified,
			# reader starts on header line. This line
			# skips it and moves to the data 
			next(reader)
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
		itemList = []
		for key in self.data.keys():
			# The | combines the two into 1 dict with
			# specific order of keys eg:
			# {these keys first} | {then these keys}
			# to ensure databaseKey is first
			newItem = {'trip_id': key} | self.data[key]
			itemList.append(newItem)

		with open('api/gtfs/trips.json', 'w+') as f:
			json.dump(itemList, f, indent=4)
			f.close()
		print('json dump complete')

if __name__ == "__main__":
	localTrips = Trips('api/gtfs/trips.txt')
	print(len(localTrips.data.keys()))
	localTrips.jsonDump()