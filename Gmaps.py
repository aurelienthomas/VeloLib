import googlemaps
from datetime import datetime
import json
from pprint import pprint
import requests

"""gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
"""
# parse API
def station_a_recharger():
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Toulouse&apiKey=adcf8bb9b76004df8324b59f7dc0a0a74e1658f0'

    resp = requests.get(url=url)
    liste_data = json.loads(resp.text)

    station_a_recharger = []

    for data in liste_data:
        if data["available_bike_stands"] < data["bike_stands"]/2 and data["status"] == "OPEN":
            station_a_recharger.append(data)

    return station_a_recharger

def gmaps():
    station = station_a_recharger()
    gmaps = googlemaps.Client(key='AIzaSyAqq2AUug4t3ovjFt_AP4KiCqNhVdIuedM')
    reverse_geocode_result = gmaps.reverse_geocode((station[0].position.lat, station[0].position.lng))
