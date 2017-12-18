import json

def __init__(self, j):
         self.__dict__ = json.loads(j)


def chargerJson(fichier):
    resultat = {}
    with open(fichier, "r") as f:
        json_dict = json.load(f)
    return json_dict

def test():
    liste_station = chargerJson("Toulouse.json")
    print(liste_station)

test()