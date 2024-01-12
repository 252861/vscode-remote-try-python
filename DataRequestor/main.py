from time import sleep
from datetime import datetime
#from snap7.server import mainloop
import json
import os
import requests


env_city = os.getenv('CITY')

#url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city=E%C5%82k&order_by=lastUpdated&dump_raw=false"
url = f"https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city={env_city}&order_by=lastUpdated&dump_raw=false"
headers = {"accept": "application/json"}


while (True):
    
    response = requests.get(url, headers=headers)
    x = response.text
    y = json.loads(x)
  

    country = y['results'][0]['country']
    city = y['results'][0]['city']
    time = str(y['results'][0]['parameters'][0]['lastUpdated'])

    location={"country":country,
            "city":city}
    
    values={}
    for el in y["results"][0]["parameters"]:
        values[el["parameter"]]={
            "value":el["lastValue"],
            "unit":el["unit"]
        }

    weather={   "location":location,
                "timestamp":time,
                "values":values}

    data_to_send=json.dumps(weather,ensure_ascii=False)
    print(data_to_send)

    sleep(5)




