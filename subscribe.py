from paho.mqtt import client as mqtt

def on_message(client, userdata, message):
    print("Received message:", str(message.payload.decode("shift-jis")))
    
client = mqtt.Client()
client.username_pw_set(username="lucas", password="rohlin")

# Set callback function
client.on_message = on_message

# Connect to broker
client.connect("192.168.3.11", 1883)

# Subscribe to topic
client.subscribe("test")

# Loop and handle incoming messages
client.loop_forever()