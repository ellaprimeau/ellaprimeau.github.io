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
		for key in self.data.keys():
			with open('api/gtfs/{}.json'.format(key), 'w+') as f:
				json.dump({'shape_id': key, 'shape': self.data[key]}, f)
				f.close()
		print('json dump complete')


if __name__ == "__main__":
	localShapes = Shapes('api/gtfs/shapes.txt')
	localShapes.jsonDump()