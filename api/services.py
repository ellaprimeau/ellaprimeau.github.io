import csv, json

class Services:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.DictReader(f, delimiter=',')

			for row in reader:
				key = row['service_id']
				row.pop('service_id')
				if key in self.data.keys():
					self.data[key].append(row)

				else:
					self.data[key] = [row]

	def jsonDump(self):
		itemList = []
		for key in self.data.keys():
			# The | combines the two into 1 dict with
			# specific order of keys eg:
			# {these keys first} | {then these keys}
			# to ensure databaseKey is first
			newItem = {
				'service_id': key,
				'dates':self.data[key]
			}
			itemList.append(newItem)

		with open('api/gtfs/services.json', 'w+') as f:
			json.dump(itemList, f, indent=4)
			f.close()
		print('json dump complete')