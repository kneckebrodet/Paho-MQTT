from paho.mqtt import client as mqtt
from random import randint

port = 1883
broker = "192.168.3.11"

player = "player-name"
score = randint(1,100)

client = mqtt.Client("Lucas")
client.username_pw_set(username="lucas", password="rohlin")
client.connect(broker, port)

client.publish("test", "{}: {}".format(player, score))

client.disconnect()