import csv, json

class CalendarDates:
	def __init__(self, filepath):
		self.data = {}
		with open(filepath, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			for row in reader:
				key = row[]