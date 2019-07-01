import librosa
import matplotlib.pyplot as plt
import wave
import numpy as np
from scipy import signal

# Carregar Sinais de Audio
caminho = 'C:\\Users\\jeanm\\Documents\\Filter-Project\\Data\\'
arquivo_audio1 = "Voz01_16KHz"
arquivo_audio2 = "Voz02_16KHz"
sz = 128000  # Taxa do Projeto (Hz)
spf1 = wave.open(caminho + arquivo_audio1 + '.wav', 'rb')
signal1 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)
spf2 = wave.open(caminho + arquivo_audio2 + '.wav', 'rb')
signal2 = np.frombuffer(spf2.readframes(sz), dtype=np.int16)

Fs = 16000  # Frequência de Amostragem
n = np.arange(0, 8, 1/Fs)  # Array de Amostras

# Criação do Sinal Portadora de Transmissão
Fc = 3  # Frequência da Portadora
Ac = 1  # Amplitude da Portadora
phc = np.pi/2  # Fase da Portadora
carrier = Ac*np.cos(2*np.pi*Fc*n + phc)
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.grid()
plt.show()

# # Criação do sinal Modulante (Somente para testes)
Fm = 0.5  # Frequência do Modulante
Am = 1  # Amplitude do Modulante
m = Am*np.cos(2*np.pi*Fm*n + np.pi/2)

# sinal de Audio 1
samps = 8 * 16000
signal1 = signal.resample(signal1, samps)
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
plt.title('Sinal Modulante 1')
plt.plot(n, m)
plt.show()

# Modulação Sinal de Audio 1
s = carrier * (1 + m/Ac)
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#  Espectros Sinal Modulado 1
spectrum = np.fft.fft(s)
freqs = np.fft.fftfreq(len(spectrum))
magnitude = np.abs(spectrum)    # Amplitude do Sinal
phase = np.angle(spectrum)  # Fase do Sinal
plt.subplot(2, 1, 1)
plt.plot(freqs, magnitude)
plt.title('Espectros do Sinal Modulado 1')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.plot(freqs, phase)
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# Demodulação do sinal 1
Pha = np.pi/2
h = s * np.cos(2*np.pi*Fc*n + Pha)
plt.figure()
plt.plot(n, h)
plt.title('Sinal Demodulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.ylim(-(Ac+Am), Ac+Am)
plt.grid()
plt.show()

#  Espectros Sinal Demodulado 1
spectrum = np.fft.fft(h)
freqs = np.fft.fftfreq(len(spectrum))
magnitude = np.abs(spectrum)    # Amplitude do Sinal
phase = np.angle(spectrum)  # Fase do Sinal
plt.subplot(2, 1, 1)
plt.plot(freqs, magnitude)
plt.title('Espectros do Sinal Demodulado 1')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.plot(freqs, phase)
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()


# Plotar sinal de audio 2
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
plt.plot(n, signal1)
plt.title('Sinal Modulante 2')
plt.show()

# Modulação Sinal de Audio 2
s = carrier * (1 + signal1/Ac)
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#  Espectros Sinal Modulado 2
spectrum = np.fft.fft(s)
freqs = np.fft.fftfreq(len(spectrum))
magnitude = np.abs(spectrum)    # Amplitude do Sinal
phase = np.angle(spectrum)  # Fase do Sinal
plt.subplot(2, 1, 1)
plt.plot(freqs, magnitude)
plt.title('Espectros do Sinal Modulado 2')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.plot(freqs, phase)
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()


# Demodulação do sinal de audio 2
Pha = np.pi/2
h = s * np.cos(2*np.pi*Fc*n + Pha)
plt.figure()
plt.plot(n, h)
plt.title('Sinal Demodulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#  Espectros Sinal Demodulado 2
spectrum = np.fft.fft(h)
freqs = np.fft.fftfreq(len(spectrum))
magnitude = np.abs(spectrum)    # Amplitude do Sinal
phase = np.angle(spectrum)  # Fase do Sinal
plt.subplot(2, 1, 1)
plt.plot(freqs, magnitude)
plt.title('Espectros do Sinal Demodulado 2')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.plot(freqs, phase)
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()


# Gerar arquivos de audio .wav
# librosa.output.write_wav(caminho + 'Saida_' + arquivo_audio1 + '.wav', signal1, sr)
# # #ipd.Audio(sig, rate=sr)
# librosa.output.write_wav(caminho + 'Saida_' + arquivo_audio2 + '.wav', signal2, sr2)
# #ipd.Audio(sig2, rate=sr2)
