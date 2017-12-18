import json
import requests

from pprint import pprint

#parse données statiques
with open('../Toulouse.json') as data_file:    
    data = json.load(data_file)
pprint(data)

#parse API
url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Toulouse&apiKey=adcf8bb9b76004df8324b59f7dc0a0a74e1658f0'

resp = requests.get(url=url)
liste_data = json.loads(resp.text)

station_a_recharger = []

for data in liste_data:
    if data["available_bike_stands"] != data["bike_stands"] && data["status"]=="OPEN":
        station_a_recharger.append(data)

pprint(station_a_recharger)
