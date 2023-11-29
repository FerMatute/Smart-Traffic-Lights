import time
import matplotlib.pyplot as plt
from drawnow import *
import serial
import numpy as np

val = np.zeros(51, dtype=float)
val2 = np.zeros(51, dtype=float)
cnt = 0
i = 0

port = serial.Serial('COM11', 115200, timeout=0.5)

plt.ion()

def plot_wave():
    plt.ylim(0,5)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'r' ,label='Channel 0')
    plt.plot(val2, 'g', label='Channel 1' )
    plt.legend(loc='lower left')


while (True):
    port.write(b's') #handshake with Arduino
    if (port.inWaiting()):# if the arduino replies
        value = port.readline().decode().strip()# read the reply
        print(value)#print so we can monitor it
        if value.startswith("1."):
            number = float(value[len("1."):]) #convert received data to integer 
            print('Channel 0: {0}'.format(number))
            val[i] = number

        if value.startswith("2."):
            number = float(value[len("2."):]) #convert received data to integer 
            print('Channel 1: {0}'.format(number))
            val2[i] = number
        
        time.sleep(0.01)

    drawnow(plot_wave)#update plot to reflect new data input
    plt.pause(.000001)

    i += 1
    if(i>50):
        val[:50] = val[1:]
        i -= 1