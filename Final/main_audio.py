
import librosa
import os
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate
import serial
from numpy.fft import fft, ifft, fftshift
import time
import paho.mqtt.publish as publish


# Una función lambda es una función anónima
plots = lambda rows = 1, cols = 1, size = (20, 10): plt.subplots(rows, cols, figsize = size)
ser = serial.Serial('COM9', 115200, timeout=0)


fs = 4000
ts = 1/fs
total_samples = fs*1
n = np.arange(total_samples)
tiempo = np.arange(total_samples)
datos = np.arange(total_samples)
datos_mic1 = np.zeros(total_samples)
datos_mic2 = np.zeros(total_samples)
datos_mic3 = np.zeros(total_samples)
datos_mic4 = np.zeros(total_samples)
maxi = np.zeros(4)
flag = False
second = 0
third = 0
mj = 0

print("Inicia")

while True:
    for i in range(total_samples):
        while True:
            try:
                raw_data = ((ser.readline()).decode()).strip()
                #print("Raw data" + raw_data)
                identifier = raw_data[0]
                dato = int(raw_data[1:])
                
                if dato > 1023:
                    raw_data = ((ser.readline()).decode()).strip()
                    identifier = raw_data[0]
                    dato = int(raw_data[1:])

                while identifier != "A" or dato > 1023:
                    raw_data = ((ser.readline()).decode()).strip()
                    identifier = raw_data[0]
                    dato = int(raw_data[1:])
                    if dato > 1023:
                        raw_data = ((ser.readline()).decode()).strip()
                        identifier = raw_data[0]
                        dato = int(raw_data[1:])
                datos_mic1[i] = dato

                while identifier != "B" or dato > 1023:
                    raw_data = ((ser.readline()).decode()).strip()
                    identifier = raw_data[0]
                    dato = int(raw_data[1:])

                datos_mic2[i] = dato

                while identifier != "C" or dato > 1023:
                    raw_data = ((ser.readline()).decode()).strip()
                    identifier = raw_data[0]
                    dato = int(raw_data[1:])

                datos_mic3[i] = dato

                while identifier != "D" or dato > 1023:
                    raw_data = ((ser.readline()).decode()).strip()
                    identifier = raw_data[0]
                    dato = int(raw_data[1:])

                datos_mic4[i] = dato

                #print("Ya ando ajuera")
                break     
            except ValueError:
                #print("No toy juera")
                dato = 0

            except IndexError:
                #print("No toy juera")
                dato = 0

        #datos[i] = dato



    _, ax = plots()
    ax.plot(n*ts, datos_mic1, 'o',label = 'Wacha perro1')
    ax.plot(n*ts, datos_mic2, 'o',label = 'Wacha perro2')
    ax.plot(n*ts, datos_mic3, 'o',label = 'Wacha perro3')
    ax.plot(n*ts, datos_mic4, 'o',label = 'Wacha perro3')
    ax.legend()
    plt.show()

    # Datos Mic 1
    Final1 = np.arange(total_samples / 2)
    Y1 = np.arange(total_samples)
    YS1 = np.arange(total_samples)
    Y1 = fft(datos_mic1)
    YS1 = np.abs(fftshift(Y1))

    if len(YS1)%2 == 1:
        freqs = np.arange(0, len(Final1)) +.5
    else:
        freqs = np.arange(0, len(Final1))


    for i in n:
        if i < len(n)//2:
            Final1[i] = YS1[i + len(YS1)//2]

    Final1[0] = 0

    # Datos Mic 2

    Final2 = np.arange(total_samples / 2)
    Y2 = np.arange(total_samples)
    YS2 = np.arange(total_samples)
    Y2 = fft(datos_mic2)
    YS2 = np.abs(fftshift(Y2))

    if len(YS2)%2 == 1:
        freqs = np.arange(0, len(Final2)) +.5
    else:
        freqs = np.arange(0, len(Final2))


    for i in n:
        if i < len(n)//2:
            Final2[i] = YS2[i + len(YS2)//2]

    Final2[0] = 0

    # Micro 3

    Final3 = np.arange(total_samples / 2)
    Y3 = np.arange(total_samples)
    YS3 = np.arange(total_samples)
    Y3 = fft(datos_mic3)
    YS3 = np.abs(fftshift(Y3))

    if len(YS3)%2 == 1:
        freqs = np.arange(0, len(Final3)) +.5
    else:
        freqs = np.arange(0, len(Final3))


    for i in n:
        if i < len(n)//2:
            Final3[i] = YS3[i + len(YS3)//2]

    Final3[0] = 0

    # Datos Mic 2

    Final4 = np.arange(total_samples / 2)
    Y4 = np.arange(total_samples)
    YS4 = np.arange(total_samples)
    Y4 = fft(datos_mic4)
    YS4 = np.abs(fftshift(Y4))

    if len(YS4)%2 == 1:
        freqs = np.arange(0, len(Final4)) +.5
    else:
        freqs = np.arange(0, len(Final4))


    for i in n:
        if i < len(n)//2:
            Final4[i] = YS4[i + len(YS4)//2]

    Final4[0] = 0

    _,ax3 = plots()
    ax3.plot(freqs, Final1, 'ro', label = 'Wacha pt. 1')
    ax3.plot(freqs, Final2, 'go', label = 'Wacha pt. 2')
    ax3.plot(freqs, Final3, 'bo', label = 'Wacha pt. 3')
    ax3.plot(freqs, Final4, 'mo', label = 'Wacha pt. 4')
    ax3.legend()
    plt.show()

    Ambulancia1 = Final1[1249:1999]
    Ambulancia2 = Final2[1249:1999]
    Ambulancia3 = Final3[1249:1999]
    Ambulancia4 = Final3[1249:1999]
    
    print("--------------------")

    for i, array in enumerate([Ambulancia1, Ambulancia2, Ambulancia3, Ambulancia4]):
        maxi[i] = array.max()

    final = np.argmax(maxi) + 1
    #print('The microphone with the biggest presence of the sample, is the microphone no. %2d' %final)

    print("<<<<<<<<<<<<<<<<<<<<<")

    if flag == False:
        # The case for the 1st traffic light
        if maxi[final - 1] > 750:
            if final == 4:
                topic = "esp32/alarm1"
            else:
                topic = "esp32/alarm" + str(final + 1)
            
            publish.single(topic, "on", hostname = "192.168.1.68", port=1883,keepalive=60)

            print('The traffic light no. %2d is now in green' %final)
            tempMax = final - 1
            flag = True
        else:
            flag = False


    elif flag == True:
        # The case for the 2nd traffic light
        maxi[tempMax] = 0
        final = np.argmax(maxi) + 1
        if second == 0 and maxi[final - 1] > 750:
            publish.single(topic, "off", hostname = "192.168.1.68", port=1883,keepalive=60)
            topic = "esp32/alarm" + str(final)
            publish.single(topic, "on", hostname = "192.168.1.68", port=1883,keepalive=60)
            print('The traffic light no. %2d is now in green' %final)
            second = final - 1

        elif second == 0 and maxi[final - 1] <= 750:
            msgs = [("esp32/alarm1","off"),("esp32/alarm","off"),("esp32/alarm","off"),("esp32/alarm","off")]
            publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
            flag = False
            tempMax = 0

        elif second != 0:
            # The case for the 3rd traffic light
            maxi[second] = 0
            final = np.argmax(maxi) + 1
            if third == 0 and maxi[final - 1] > 750:
                publish.single(topic, "off", hostname = "192.168.1.68", port=1883,keepalive=60)
                topic = "esp32/alarm" + str(final)
                publish.single(topic, "on", hostname = "192.168.1.68", port=1883,keepalive=60)
                print('The traffic light no. %2d is now in green' %final)
                third = final - 1

            elif third == 0 and maxi[final - 1] <= 750:
                msgs = [("esp32/alarm1","off"),("esp32/alarm","off"),("esp32/alarm","off"),("esp32/alarm","off")]
                publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
                flag = False
                tempMax = 0
                second = 0
            
            elif third != 0:
                # The case of the 4th traffic light
                maxi[third] = 0
                final = np.argmax(maxi) + 1
                if maxi[final - 1] > 750:
                    publish.single(topic, "off", hostname = "192.168.1.68", port=1883,keepalive=60)
                    topic = "esp32/alarm" + str(final)
                    publish.single(topic, "on", hostname = "192.168.1.68", port=1883,keepalive=60)
                    print('The traffic light no. %2d is now in green' %final)
                    flag = False
                    tempMax = 0
                    second = 0
                    third = 0
                    time.sleep(2)
                    msgs = [("esp32/alarm1","off"),("esp32/alarm","off"),("esp32/alarm","off"),("esp32/alarm","off")]
                    publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)

                else:
                    msgs = [("esp32/alarm1","off"),("esp32/alarm","off"),("esp32/alarm","off"),("esp32/alarm","off")]
                    publish.multiple(msgs,hostname="192.168.1.68",port=1883,keepalive=60)
                    flag = False
                    tempMax = 0
                    second = 0
                    third = 0

    #time.sleep(2)

    mj+=1
    if mj == 8:
        break

ser.close()