import csv, json

class StopTimes:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.DictReader(f, delimiter=',')

			for row in reader:
				key = row['trip_id']
				row.pop('trip_id')
				if key in self.data.keys():
					self.data[key].append(row)

				else:
					self.data[key] = [row]

	def get(self, trip_id):
		return self.data[trip_id]

	def jsonDump(self):
		itemList = []
		for key in self.data.keys():
			newItem = {
				'trip_id':key,
				'stopTimes':self.data[key]
			}
			itemList.append(newItem)
		with open('api/gtfs/stop_times.json', 'w+') as f:
			json.dump(itemList, f, indent=4)
			f.close()

if __name__ == "__main__":
	localStopTimes = StopTimes('api/gtfs/stop_times.txt')
	localStopTimes.jsonDump()
	print('done')