import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

flag = False

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("esp32/alarm1",0), ("esp32/alarm2",1),("esp32/alarm3",2),("esp32/alarm4",2)])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global flag

    if msg.topic == "esp32/alarm1":
        print(str(msg.payload) + "/")
        if str(msg.payload) == "b'on'":
            print(flag)
            flag = True
            msgs = [("esp32/green1","on"),("esp32/green2","off"),("esp32/green3","off"),("esp32/green4","off")]
            publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
        elif str(msg.payload) == "b'off'":
            flag = False

    elif msg.topic == "esp32/alarm2":
        if str(msg.payload) == "b'on'":
            msgs = [("esp32/green1","off"),("esp32/green2","on"),("esp32/green3","off"),("esp32/green4","off")]
            publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
            flag = True    
        elif str(msg.payload) == "b'off'":
            flag = False

    elif msg.topic == "esp32/alarm3":
        if str(msg.payload) == "b'on'":
            msgs = [("esp32/green1","off"),("esp32/green2","off"),("esp32/green3","on"),("esp32/green4","off")]
            publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
            flag = True    
        elif str(msg.payload) == "b'off'":
            flag = False

    elif msg.topic == "esp32/alarm4":
        if str(msg.payload) == "b'on'":
            msgs = [("esp32/green1","off"),("esp32/green2","off"),("esp32/green3","off"),("esp32/green4","on")]
            publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
            flag = True    
        elif str(msg.payload) == "b'off'":
            flag = False
    
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.68", 1883, 60)


client.loop_start()
num = 0
while True:
    #print(flag)
    while flag == False:
        msg = [("esp32/green1","on"),("esp32/green2","off"),("esp32/green3","off"),("esp32/green4","off")]
        publish.multiple(msg,hostname="192.168.1.68",port=1883,keepalive=60)
        time.sleep(.5)

        if flag != False:
            break

        msg = [("esp32/green1","off"),("esp32/green2","on"),("esp32/green3","off"),("esp32/green4","off")]
        publish.multiple(msg,hostname="192.168.1.68",port=1883,keepalive=60)
        time.sleep(.5)
        
        if flag != False:
            break

        msg = [("esp32/green1","off"),("esp32/green2","off"),("esp32/green3","on"),("esp32/green4","off")]
        publish.multiple(msg,hostname="192.168.1.68",port=1883,keepalive=60)
        time.sleep(.5)
        
        if flag != False:
            break

        msg = [("esp32/green1","off"),("esp32/green2","off"),("esp32/green3","off"),("esp32/green4","on")]
        publish.multiple(msg,hostname="192.168.1.68",port=1883,keepalive=60)
        time.sleep(.5)
        
        if flag != False:
            break
 
        

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.