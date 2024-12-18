import csv, json, os

class Shapes:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.DictReader(f, delimiter=',')
			for row in reader:
				key = row['shape_id']
				row.pop('shape_id')
				if key in self.data.keys():
					self.data[key].append(row)

				else:
					self.data[key] = [row]

	def get(self, id):
		return self.data[id]

	def jsonDump(self):
		itemList = []
		for key in self.data.keys():
			newItem = {
				'shape_id': key,
				'shape': self.data[key]
			}
			itemList.append(newItem)
		with open('api/gtfs/shapes.json', 'w+') as f:
			json.dump(itemList, f, indent=4)
			f.close()
		print('json dump complete')


if __name__ == "__main__":
	localShapes = Shapes('api/gtfs/shapes.txt')
	localShapes.jsonDump()