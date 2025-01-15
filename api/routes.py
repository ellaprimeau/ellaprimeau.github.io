import csv, json

class Routes:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.DictReader(f, delimiter=',')
			
			for row in reader:
				key = row['route_id']
				row.pop('route_id')
				for item in row.keys():
					row[item] = row[item].encode('cp1252').decode('utf-8')
				self.data[key] = row

	def list_routes(self):
		for route in self.data.keys():
			print(self.data[route]['route_short_name'],self.data[route]['route_long_name'])

	def jsonDump(self):
		itemList = []
		for key in self.data.keys():
			# The | combines the two into 1 dict with
			# specific order of keys eg:
			# {these keys first} | {then these keys}
			# to ensure databaseKey is first
			newItem = {'route_id': key} | self.data[key]
			itemList.append(newItem)

		with open('api/gtfs/routes.json', 'w+') as f:
			json.dump(itemList, f, indent=4)
			f.close()
		print('json dump complete')

if __name__ == "__main__":
	localRoutes = Routes('api/gtfs/routes.txt')
	print(len(localRoutes.data.keys()))
	localRoutes.jsonDump()