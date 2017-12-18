import json, requests

from pprint import pprint

with open('../Toulouse.json') as data_file:    
    data = json.load(data_file)
pprint(data)
