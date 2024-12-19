import requests, io, os
from zipfile import ZipFile
from routes import Routes
from shapes import Shapes
from stop_times import StopTimes
from trips import Trips
from services import Services

r = requests.get('https://contenu.sto.ca/GTFS/GTFS.zip')
faunaKey = ''
# print(faunaKey)

with ZipFile(io.BytesIO(r.content)) as z:
	wd = os.path.dirname(__file__)
	z.extractall(wd+'\\gtfs')
	z.close()

# routes = Routes('api/gtfs/routes.txt')
# routes.jsonDump()
# print('{} routes dumped to json'.format(len(routes.data.keys())))
# shapes = Shapes('api/gtfs/shapes.txt')
# shapes.jsonDump()
# print('{} shapes dumped to json'.format(len(shapes.data.keys())))
# stop_times = StopTimes('api/gtfs/stop_times.txt')
# stop_times.jsonDump()
# print('{} stop times dumped to json'.format(len(stop_times.data.keys())))
# trips = Trips('api/gtfs/trips.txt')
# trips.jsonDump()
# print('{} trips dumped to json'.format(len(trips.data.keys())))
services = Services('api/gtfs/calendar_dates.txt')
services.jsonDump()
print('{} services dumped to json'.format(len(services.data.keys())))

os.system("cd api/gtfs & fauna import --path . --secret {}:sto:admin".format(faunaKey))
