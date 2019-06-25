import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

# Extract Raw Audio from Wav File
spf = wave.open(r'/home/jean/Documentos/Filter-Project/Data/mountain_king_16kHz.wav', mode='rb')
# If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)

Fs = 16000
n = np.arange(0, 8, 1/Fs)

sz = 44100  # Read and process 1 second at a time.
signal = np.fromstring(spf.readframes(128000), dtype=np.int16)
left, right = signal[0::2], signal[1::2]
print(len(signal))
# discrete fourier transform
lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))

plt.figure(figsize=(12, 4))
plt.title('Signal Wave...')
plt.plot(n, signal)
plt.show()

# # plot time signal:
# axes[0, 0].set_title("Signal")
# axes[0, 0].plot(t, spf, color='C0')
# axes[0, 0].set_xlabel("Time")
# axes[0, 0].set_ylabel("Amplitude")

# plot different spectrum types:
plt.figure(figsize=(12, 4))
plt.title("Magnitude Spectrum")
plt.magnitude_spectrum(signal, Fs=Fs, color='C1')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
plt.title("Phase Spectrum ")
plt.phase_spectrum(signal, Fs=Fs, color='C2')
plt.tight_layout()
plt.show()

# freq = 13
# x = np.arange(0, 1, 1.0/Fs)
# y = np.sin(2 * np.pi * freq * x + (np.pi/2)) * np.cos(np.pi * x + (np.pi/2))
# np.cos(6.28*fc*t)
# plt.plot(x, y)
# plt.show()

#Fc = 50
Ac = 1
c = Ac*np.cos(2*np.pi*0.5*n)


plt.figure(figsize=(12, 4))
plt.title('Signal Wave...')
plt.plot(n, c)
plt.show()


#Fm = 2
#Am = 1
#m = Am*np.sin(2*np.pi*Fm*n)

s = c * (1 + signal/Ac)

plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Modulation Case')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
