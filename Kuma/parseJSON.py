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
data = json.loads(resp.text)
