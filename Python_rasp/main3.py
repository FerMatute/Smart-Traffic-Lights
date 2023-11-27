import numpy as np
import serial
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftshift

plots = lambda rows = 1, cols = 1, size = (20, 10): plt.subplots(rows, cols, figsize = size)
ser = serial.Serial('COM11', 9600, timeout=1)


fs = 4000
ts = 1/fs
total_samples = fs*1
n = np.arange(total_samples)

tiempo = np.arange(total_samples)
datos = np.arange(total_samples)

for i in range(total_samples):
    dato = ((ser.readline()).decode()).strip()
    try:
        dato = int(dato)
    except ValueError:
        if i == 0:
            dato = 200
        else:
            try:
                dato = int(datos[i - 1])
            except ValueError:
                dato = 200

    #dato_int = int(float(dato))
    #print(dato_int)
    datos[i] = dato

ser.close()


#"""
_, ax = plots()
ax.plot(n*ts, datos, 'o',label = 'Wacha perro3')
ax.legend()
plt.show()
#"""

# Create the array that would contain only our positive frequency data
#Final = []
#Final2 = []
Final3 = np.arange(total_samples / 2)
print(total_samples/2)
Y3 = np.arange(total_samples)
YS3 = np.arange(total_samples)

# Transform the array in time, so now is in frequency, and we shift it
#Y = fft(y)
#YS = np.abs(fftshift(Y))

#Y2 = fft(y2)
#YS2 = np.abs(fftshift(Y2))

Y3 = fft(datos)
#print(Y3)
YS3 = np.abs(fftshift(Y3))


if len(YS3)%2 == 1:
    freqs = np.arange(0, len(Final3)) +.5
else:
    freqs = np.arange(0, len(Final3))

print(len(freqs))

# Sort the shifted array, so we only have the positive frequencies
for i in n:
    if i < len(n)//2:
        #Final.append(YS[i + len(YS)//2])
        #Final2.append(YS2[i + len(YS2)//2])
        Final3[i] = YS3[i + len(YS3)//2]
        #np.append(Final3, YS3[i + len(YS3)//2])

# Search the maximum value within the signal we are interested and it's corresponding frequency
#print(Final3)
freq = np.argmax(Final3)
Final3[0] = 6

print(freq)

print("The higgest frequency on the signal is: " + str(freq) + " Hz")


_,ax2 = plots()
ax2.plot(freqs, Final3, 'o', label = 'Wacha pt. 2')
ax2.legend()
plt.show()

print(datos)
print(Final3)