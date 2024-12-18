import requests, io, os
from zipfile import ZipFile

r = requests.get('https://contenu.sto.ca/GTFS/GTFS.zip')

with ZipFile(io.BytesIO(r.content)) as z:
	wd = os.path.dirname(__file__)
	z.extractall(wd+'\\gtfs')
	z.close()