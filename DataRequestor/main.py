from time import sleep
from datetime import datetime
#from snap7.server import mainloop
import json
import requests

url = "https://api.openaq.org/v2/latest/9342?limit=100&page=1&offset=0&sort=asc"

headers = {"accept": "application/json"}
#test

while (True):
    response = requests.get(url, headers=headers)
    x = response.text
    y = json.loads(x)
                       
     
    weatherRequest={"location":"<location-name>",
                    "timestamp":"<iso-current-time>",
                    "values":[{"<measurement-name>":"<value>"}]}
    
    dKraj = y['results'][0]['country']
    dMiasto = y['results'][0]['city']
    dCzas = str(y['results'][0]['measurements'][0]['lastUpdated'])
    dCzasF = dCzas.replace("T"," ")
    
    #print("Kraj: "      +  y['results'][0]['country'])
    #print("Miasto: "    +  y['results'][0]['city'])
    #print("Czas: "      +  str(y['results'][0]['measurements'][0]['lastUpdated']))

    print("Kraj: "      +  dKraj)
    print("Miasto: "    +  dMiasto)
    print("Czas: "      +  dCzasF)

    for el in y["results"][0]["measurements"]:
        print(f"{el['parameter']:<5} = {el['value']} {el['unit']}")

    sleep(5)



