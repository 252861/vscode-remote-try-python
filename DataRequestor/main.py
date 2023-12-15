from time import sleep
from datetime import datetime
#from snap7.server import mainloop
import json
import requests

url = "https://api.openaq.org/v2/latest/9342?limit=100&page=1&offset=0&sort=asc"

headers = {"accept": "application/json"}

while (True):
    response = requests.get(url, headers=headers)
    x = response.text
    y = json.loads(x)
    
    kraj = y['results'][0]['country']
    miasto = y['results'][0]['city']
    czas = str(y['results'][0]['measurements'][0]['lastUpdated'])

    location={"country":kraj,
             "city":miasto}
    
    values={}

    weather={   "location":location,
                "timestamp":czas,
                "values":[{<measurement-name>:<value>}]}

    data_to_send=json.dumps(weather)
    print(data_to_send)

    for el in y["results"][0]["measurements"]:
        print(f"{el['parameter']:<5} = {el['value']} {el['unit']}")

    sleep(5)



