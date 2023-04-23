from paho.mqtt import client as mqtt

def on_message(client, userdata, message):
    print("Received message:", str(message.payload.decode("shift-jis")))

broker = "localhost"    
port = 1883

client = mqtt.Client()
client.username_pw_set(username="", password="")

# Set callback function
client.on_message = on_message

# Connect to broker
client.connect(broker, port)

# Subscribe to topic
client.subscribe("topic")

# Loop and handle incoming messages
client.loop_forever()
