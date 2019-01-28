#!python3
import Adafruit_DHT as DHT
import time
import datetime
import paho.mqtt.client as mqtt
import json
import configparser
import sys
# from multiprocessing import Pool

def OnLog(client, userdata, level, buf=0):
    print("[Info]   " + buf + "\n")

def OnConnect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection succeeded\n")
    else:
        print("Connection failure, returned code = " + str(rc) + "\n")

def OnDisconnect(client, userdata, flags, rc=0):
    print("Disconnected, result code was " + str(rc) + "\n")

def OnMessage(client, userdata, msg):
    print("Message received: " + str(msg.payload.decode("utf-8")) + "\n")

def isReadingValid(humidity, temperature):
    return humidity is not None and temperature is not None

# Read config file
config = configparser.ConfigParser()
config.read(["config.ini", "config.app.ini"])

# Initialize sensor parameters
if config["DEFAULT"]["Sensor"] == "AM2302":
    sensor = DHT.AM2302
elif config["DEFAULT"]["Sensor"] == "DHT22":
    sensor = DHT.DHT22
elif config["DEFAULT"]["Sensor"] == "DHT11":
    sensor = DHT.DHT11
else:
    sys.exit('Invalid sensor! Valid sensors are "DHT11", "DHT22" or "AM2302".')
    
pin = config["DEFAULT"]["Pin"]
sec = int(config["DEFAULT"]["TimeBetweenReadings"])

# Gateway configurations
broker = config["DEFAULT"]["GatewayURL"]
port = int(config["DEFAULT"]["GatewayPort"])
keepalive = int(config["DEFAULT"]["KeepAlive"])
topic = config["DEFAULT"]["TopicOfPublish"]

# Client configurations
client = mqtt.Client(config["DEFAULT"]["DeviceID"])
if config["DEFAULT"].getboolean("UseTls"):
    client.tls_set()
    client.username_pw_set(config["DEFAULT"]["Username"], config["DEFAULT"]["Password"])
client.on_log = OnLog
client.on_connect = OnConnect
client.on_disconnect = OnDisconnect
client.on_message = OnMessage

print ("Connecting to broker " + broker + "...\n")

client.connect(broker, port, keepalive)
client.loop_start()

while True:
    humidity, temperature = DHT.read(sensor, pin)
    if isReadingValid(humidity, temperature):
        payload = {
            "date": str(datetime.datetime.now()),
            "temperature": temperature,
            "humidity": humidity
            }
        print(payload)
        client.publish(topic, json.dumps(payload))
    time.sleep(sec)
    
time.sleep(4)
client.loop_stop()
client.disconnect()