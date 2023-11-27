import numpy as np
np.set_printoptions(precision=4)
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

class Sinusoidals_samples:
    '''
    kwargs: dictionary containing keys for 'fs', 'total time', and data = {'':(amplitude, freq, phase, sin or cos)}
    '''
    def __init__(self, fs = 1000, total_time = 1, num_samples=None, compute_sum = True, **kwargs):
        self.fs = fs
        self.total_time = total_time
        self.signals = kwargs

        self.ts = 1/self.fs
        self.total_samples = self.fs * self.total_time
        self.N = np.arange(self.total_samples)

        self.num_samples = num_samples
        self.compute_sum = compute_sum
        self.sinusoidals = {}
        self.Y = {}

    def __call__(self):
        sinus = self.gen_sinusoidals()
        self.plot_signals()
        for k, signal in sinus.items():
            print(f'for signal {k}')
            print(f'the sin value {signal}')
            self.dft(signal, k)

    def gen_sinusoidals(self):
        if self.signals:
            functions = {'sin':sin, 'cos':cos}
            total_signals = len(self.signals)
            print(self.total_samples)
            for A, freq, phi, sinu in self.signals.values():
                self.sinusoidals[str(freq)+'_Hz_'+sinu] = A*functions[sinu](2*pi*freq*self.N*self.ts + phi)

            if self.compute_sum:
                self.sinusoidals['Signals_sum'] = sum(self.sinusoidals.values())
                print(f" the signals sum is:  { self.sinusoidals['Signals_sum']}")

            return self.sinusoidals

    def plot_signals(self):
        if self.sinusoidals:
            total_sinusoidals = len(self.sinusoidals)
            _, ax = plt.subplots(figsize=(20, 10))
            for k, v in self.sinusoidals.items():
                ax.plot(self.N*self.ts, v, 'o', label = k)

            ax.legend()
            plt.show()
            
        else:
            print('There is nothing to plot')

    def dft(self, signal, name):

      N = len(signal)

      X = np.zeros(N, dtype=complex)
      self.Y = np.zeros(N, dtype=complex)

      for m in range(N):
          X[m] = 0
          for n in range(N):
              #X[m] += signal[n] * np.exp(-2j * pi * m * n / N)
              X[m] += signal[n] * (cos((-2*pi*m*n)/N) + 1j*sin((-2*pi*m*n)/N))

      N2 = int(N/2)
      for m in range (N2):
        self.Y[m] = X[m + N2]

      for n in range (N2):
        self.Y[n + N2] = X[n]


      self.Y = abs(self.Y)

      for m in range (N):
        if self.Y[m] < .5:
          self.Y[m] = 0


      print(f"the fouriert transform of the function is:  { self.Y}")
      self.plot_dft(name)


    def plot_dft(self, name):
            total = len(self.Y)
            _, ax = plt.subplots(figsize=(20, 10))
            total_data = np.arange(-total/2,total/2)
            ax.plot(total_data,self.Y, 'o', label = name)

            ax.legend()
            plt.show()
            


s1= Sinusoidals_samples(8, 1, 8, True, **{'y1':(1, 1, 0, 'sin'), 'y2':(0.5, 2, 3/4*pi, 'sin')})
s1()