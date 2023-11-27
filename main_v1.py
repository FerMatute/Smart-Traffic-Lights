import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("esp32/alarm1",0), ("esp32/alarm2",1)])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "esp32/alarm1":
        msgs = [("esp32/green1","on"),("esp32/green2","on")]
        publish.multiple(msgs,hostname="192.168.1.6",port=1883,keepalive=60)
    elif msg.topic == "esp32/alarm2":
        msgs = [("esp32/green1","off"),("esp32/green2","off")]
        publish.multiple(msgs,hostname="192.168.1.6",port=1883,keepalive=60)
    
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.6", 1883, 60)


client.loop_start()
num = 0
while True:
    msg = [("esp32/green1","on"),("esp32/green2","off")]
    publish.multiple(msg,hostname="192.168.1.18",port=1883,keepalive=60)
    time.sleep(.5)
    msg = [("esp32/green1","off"),("esp32/green2","on")]
    publish.multiple(msg,hostname="192.168.1.18",port=1883,keepalive=60)
    time.sleep(.5)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

