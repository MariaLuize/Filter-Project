import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from numpy.fft import fft

# Extract Raw Audio from Wav File
spf = wave.open(r'/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/Codes/Filter-Project/Data/mountain_king_16kHz.wav')
# Caso Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)

Fs = 16000  # Frequência de Amostragem
n = np.arange(0, 8, 1/Fs)  # Amostras

signal = np.frombuffer(spf.readframes(128000), dtype=np.int16)

# Sinal Portadora de transmissão
Fc = 0.5
Ac = 3
carrier = Ac*np.cos(2*np.pi*Fc*n)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.show()

# Modulação Sinal original com portadora
s = carrier * (1 + signal/Ac)
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Transformada de Fourier Discreta
#spectrum = np.fft.fftshift(s)
Ts = 1.0/Fs
t = np.arange(0,1,Ts) # time vector

d = len(s)
k = np.arange(d)
sigFFT = fft(s)/d
spectrum = sigFFT[range(d//2)]
T = d/Fs
frq = k/T
frq = frq[range(d//2)]
#spectrum = np.fft.rfft(s)
freqs = np.fft.fftfreq(len(spectrum))
magnitude = np.abs(spectrum)
phase = np.angle(spectrum)

#   Graficos de espectros
plt.subplot(2, 1, 1)
#plt.magnitude_spectrum(s, Fs=Fs, color='C1')
plt.plot(frq, magnitude)
plt.title('Espectros do Sinal Modulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
#plt.phase_spectrum(s, Fs=Fs, color='C2')
plt.plot(frq, phase)
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()