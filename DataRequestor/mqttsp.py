
import time
import os
from paho.mqtt import client as mqtt_client

class mqttsp:
    def __init__(self, ip, city, user, passwd):
        self.ip = ip
        self.city = city
        self.user = user
        self.passwd = passwd
        self.client_id = "252861"
        self.port = 1883
        self.topic = self.client_id + "/" + self.city

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.subscribe()
                print("Connected to MQTT Broker!")
                
            else:
                print(f"Failed to connect, return code {rc}\n")

        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(self.user, self.passwd)
        self.client.loop_start()
        self.client.on_connect = on_connect
        self.client.connect(self.ip, self.port)
        return self.client

    def publish(self,data_to_send):

        result = self.client.publish(self.topic, data_to_send)
        status = result[0]
        if status == 0:
            print(f"Send `{data_to_send}` to topic `{self.topic}`")
        else:
            print(f"Failed to send message to topic {self.topic}")
    
    def subscribe(self):
        def on_message(client, userdata, msg):
            print(msg.payload.decode())
            name = str(msg.topic).replace("/","-")
            path = os.path.join("files", name)                
            with open(path, 'w') as file: 
                file.write(msg.payload.decode())
                  
        self.client.subscribe(topic='#') # topic='#'   # self.topic
        self.client.on_message = on_message