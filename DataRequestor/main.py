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
    
    country = y['results'][0]['country']
    city = y['results'][0]['city']
    time = str(y['results'][0]['measurements'][0]['lastUpdated'])

    location={"country":country,
             "city":city}
    
    values={}
    for el in y["results"][0]["measurements"]:
        values[el["parameter"]]={
            "value":el["value"],
            "unit":el["unit"]
        }

    weather={   "location":location,
                "timestamp":time,
                "values":values}

    data_to_send=json.dumps(weather,ensure_ascii=False)
    print(data_to_send)

    sleep(5)



