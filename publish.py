from paho.mqtt import client as mqtt
from random import randint

port = 1883
broker = "localhost"

player = "player-name"
score = randint(1,100)

client = mqtt.Client()
client.username_pw_set(username="", password="")
client.connect(broker, port)

client.publish("topic", "{}: {}".format(player, score))

client.disconnect()
