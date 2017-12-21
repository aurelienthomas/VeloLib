import json
import math


class Station():
    def __init__(self, numero, longitude, name, adress, latitude):
        self.numero = numero
        self.longitude = longitude
        self.latitude = latitude
        self.name = name
        self.adress = adress


def __init__(self, j):
    self.__dict__ = json.loads(j)


def chargerJson(fichier):
    resultat = {}
    with open(fichier, "r") as f:
        json_dict = json.load(f)
    return json_dict


def graph(liste_donnees):
    import matplotlib.pyplot as plt
    axe_x = []
    axe_y = []
    for donnee in liste_donnees:
        axe_x.append(donnee["longitude"])
        axe_y.append(donnee["latitude"])
    plt.plot(axe_x, axe_y, "ro")
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.show()


liste_station = chargerJson("Toulouse.json")
liste_station_visitable = chargerJson("Toulouse.json")
for station in liste_station:
    premier = True
    distance_min = 0
    liste_station_visitable.remove(station)
    for station_proche in liste_station_visitable:
        if station['name'] != station_proche["name"]:
            distance = math.sqrt((station["longitude"] - station_proche["longitude"]) * (
                station["longitude"] - station_proche["longitude"])
                                 + (station["latitude"] - station_proche["latitude"]) * (
                                     station["latitude"] - station_proche["latitude"]))
            if distance < distance_min or premier == True:
                station_la_plus_proche = station_proche['name']
                premier = False
    station["station_proche"] = station_la_plus_proche

# graph(liste_station)
for station in liste_station:
    print(station["name"] + " : " + station["station_proche"])
