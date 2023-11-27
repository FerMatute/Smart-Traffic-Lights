import matplotlib.pyplot as plt
import numpy as np
import serial

plots = lambda rows = 1, cols = 1, size = (20, 10): plt.subplots(rows, cols, figsize = size)

ser = serial.Serial('COM11', 9600, timeout=1)
tiempo = np.arange(50)
datos = np.arange(50)

for i in range(50):
    dato = ((ser.readline()).decode()).strip()
    try:
        dato = float(dato)
    except ValueError:
        if i == 0:
            dato = 0.0
        else:
            try:
                dato = float(datos[i - 1])
            except ValueError:
                dato = 0.0


    #dato_int = int(float(dato))
    #print(dato_int)
    datos[i] = dato

ser.close()

_,ax2 = plots()
ax2.plot(tiempo, datos, 'o', label = 'Wacha pt. 2')
ax2.legend()
plt.show()

print(datos)
#print("\nAcabo bro")

