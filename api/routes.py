import csv

class Routes:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.DictReader(f, delimiter=',')
			for row in reader:
				key = row['route_id']
				row.pop('route_id')
				self.data[key] = row

	def list_routes(self):
		for route in self.data.keys():
			print(self.data[route]['route_short_name'],self.data[route]['route_long_name'])
