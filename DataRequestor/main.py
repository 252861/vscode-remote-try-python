from time import sleep
from datetime import datetime
from paho.mqtt import client as mqtt_client
#from snap7.server import mainloop
import json
import os
import requests
import time
import mqttpub



env_city = os.getenv('CITY')
broker = os.getenv('IP')
port = 1883
topic = f"252861/{os.getenv('CITY')}"
client_id = "252861"
username = os.getenv('USER')
password = os.getenv('PASS')

url = f"https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city={env_city}&order_by=lastUpdated&dump_raw=false"
headers = {"accept": "application/json"}

class MqttPub:

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(client_id)
        # client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client


    def publish(self,client):
        msg_count = 1
        while True:
            time.sleep(1)
            msg = f"messages: {msg_count}"
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1
            if msg_count > 5:
                break


    def run(self):
        client = connect_mqtt()
        client.loop_start()
        publish(client)
        client.loop_stop()


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

    MqttPub.run()
    sleep(5)




