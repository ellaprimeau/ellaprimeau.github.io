import requests, io
from zipfile import ZipFile

r = requests.get('https://oct-gtfs-emasagcnfmcgeham.z01.azurefd.net/public-access/GTFSExport.zip')
z = ZipFile(io.BytesIO(r.content))
z.extractall('./GTFS/')