import json
from pprint import pprint

import requests


# parse données statiques
def open_fichier_Json(fichier):
    with open(fichier) as data_file:
        data = json.load(data_file)


# pprint(data)

# parse API
def station_a_recharger():
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Toulouse&apiKey=adcf8bb9b76004df8324b59f7dc0a0a74e1658f0'

    resp = requests.get(url=url)
    liste_data = json.loads(resp.text)

    station_a_recharger = []

    for data in liste_data:
        if data["available_bike_stands"] < data["bike_stands"] / 2 and data["status"] == "OPEN":
            station_a_recharger.append(data)

    pprint(station_a_recharger)


station_a_recharger()
