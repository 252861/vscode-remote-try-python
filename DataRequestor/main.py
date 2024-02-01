from time import sleep
from datetime import datetime
from paho.mqtt import client as mqtt_client
import json
import os
import requests
import time
from mqttsp import *

url = f"https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city={os.getenv('CITY')}&order_by=lastUpdated&dump_raw=false"
values={}

mqttsp = mqttsp(str(os.getenv('IP')), str("252861/"+str(os.getenv('CITY'))), str(os.getenv('USER')), str(os.getenv('PASS')))
mqttsp.connect_mqtt()
      
while (True):
    
    response = requests.get(url)
    x = response.text
    y = json.loads(x)
  
    country = y['results'][0]['country']
    city = y['results'][0]['city']
    time = str(y['results'][0]['parameters'][0]['lastUpdated'])

    location={"country":country, "city":city}

    for el in y["results"][0]["parameters"]:
        values[el["parameter"]]=el["lastValue"]

    weather={   "location":location["city"], "timestamp":time, "values":values}

    data_to_send=json.dumps(weather,ensure_ascii=False)
    print(data_to_send)

    mqttsp.publish(data_to_send)
    sleep(5)
