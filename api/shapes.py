import csv

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
