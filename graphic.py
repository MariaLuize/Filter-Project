import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

# Extract Raw Audio from Wav File
spf = wave.open(r'C:\Users\jeanm\Documents\Filter-Project\Data\Voz01_16KHz.wav')
# Caso Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)

Fs = 16000  # Frequência de Amostragem
n = np.arange(0, 8, 1/Fs)  # Amostras

sz = 44100  # Read and process 1 second at a time.
signal = np.frombuffer(spf.readframes(128000), dtype=np.int16)
left, right = signal[0::2], signal[1::2]
#print(len(signal))



# Transformada de Fourier Discreta
lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))
# spectrum = np.fft.rfft(right)
# freqs = np.fft.fftfreq(len(spectrum))

# Sinal Portadora de transmissão
Fc = 6
Ac = 3
carrier = Ac*np.cos(2*np.pi*Fc*n)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.show()

# # Criação de sinal Modulante
# Fm = 0.5
# Am = 1
# m = Am*np.sin(2*np.pi*Fm*n)
# plt.figure(figsize=(12, 4))
# plt.title('Sinal Original')
# plt.plot(n, m)
# plt.show()

# Modulação Sinal original com portadora
#s = carrier * (1 + m/Ac)
s = carrier * signal
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#   Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(s, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Modulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(s, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# Demodulação do sinal
fa = 10
h = s * np.cos(2*np.pi*fa*n)
plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#magnitude = np.abs(spectrum)
#phase = np.angle(spectrum)

# Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(h, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Demodulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(h, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()


# Extract Raw Audio from Wav File
spf1 = wave.open(r'C:\Users\jeanm\Documents\Filter-Project\Data\Voz02_16KHz.wav')
# Caso Stereo
if spf1.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)

#sz = 44100  # Read and process 1 second at a time.
signal1 = np.frombuffer(spf.readframes(128000), dtype=np.int16)
left1, right1 = signal1[0::2], signal1[1::2]
#print(len(signal))

# Transformada de Fourier Discreta
lf1, rf1 = abs(np.fft.rfft(left1)), abs(np.fft.rfft(right1))
# spectrum = np.fft.rfft(right)
# freqs = np.fft.fftfreq(len(spectrum))

# Sinal Portadora de transmissão
Fc1 = 6
Ac1 = 3
carrier1 = Ac1*np.cos(2*np.pi*Fc1*n)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier1)
plt.show()

# Criação de sinal Modulante
# Fm1 = 0.5
# Am1 = 1
# m1 = Am1*np.sin(2*np.pi*Fm1*n1)
# plt.figure(figsize=(12, 4))
# plt.title('Sinal Original')
# plt.plot(n1, m1)
# plt.show()

# Modulação Sinal original com portadora
#s = carrier * (1 + m/Ac)
s1 = carrier1 * signal1
plt.figure(figsize=(12, 4))
plt.plot(n, s1)
plt.title('Sinal Modulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#   Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(s1, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Modulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(s1, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# Demodulação do sinal
fa1 = 10
h1 = s1 * np.cos(2*np.pi*fa1*n)
plt.figure(figsize=(12, 4))
plt.plot(n, h1)
plt.title('Sinal Demodulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#magnitude = np.abs(spectrum)
#phase = np.angle(spectrum)

# Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(h1, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Demodulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(h1, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()