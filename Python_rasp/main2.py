"""
Code designed to identify the dominant frequency within a signal.
Coded by: Ricardo Navarro
"""

import numpy as np
from numpy.fft import fft, ifft, fftshift
from numpy import sin, cos, pi
import matplotlib.pyplot as plt

plots = lambda rows = 1, cols = 1, size = (20, 10): plt.subplots(rows, cols, figsize = size)


#sen1 = [0.3536,0.356,0.5317,0.9954,0.8401,-0.2984,-1.349,-1.1961]
#fs = len(sen1)
fs = 4000
ts = 1/fs
total_samples = fs*1
n = np.arange(total_samples)
y = 2*sin(2*pi*30*ts*n)
y2 = sin(2*pi*15*ts*n)
y3 = y + y2

#"""
_, ax = plots()
ax.plot(n*ts, y, 'o',label = 'Wacha perro')
ax.plot(n*ts, y2, 'o',label = 'Wacha perro2')
ax.plot(n*ts, y3, 'o',label = 'Wacha perro3')
ax.legend()
plt.show()
#"""

# Create the array that would contain only our positive frequency data
#Final = []
#Final2 = []
Final3 = np.arange(total_samples / 2)
Y3 = np.arange(total_samples)
YS3 = np.arange(total_samples)

# Transform the array in time, so now is in frequency, and we shift it
#Y = fft(y)
#YS = np.abs(fftshift(Y))

#Y2 = fft(y2)
#YS2 = np.abs(fftshift(Y2))

Y3 = fft(y3)
#print(Y3)
YS3 = np.abs(fftshift(Y3))


if len(YS3)%2 == 1:
    freqs = np.arange(-len(YS3)/2, len(YS3)/2) * fs/len(YS3) +.5
else:
    freqs = np.arange(-len(YS3)/2, len(YS3)/2) * fs/len(YS3)


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


print("The higgest frequency on the signal is: " + str(freq) + " Hz")


_,ax2 = plots()
ax2.plot(freqs, YS3, 'o', label = 'Wacha pt. 2')
ax2.legend()
plt.show()