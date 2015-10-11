
import paho.mqtt.client as mqtt
import json

with open('data.json') as data_file:
    data = json.load(data_file)

mqttc = mqtt.Client("python_pub")
mqttc.connect("10.0.1.5", 1883)
mqttc.publish("hello/world", json.dumps(data))
mqttc.loop(2) # timeout = 2s
