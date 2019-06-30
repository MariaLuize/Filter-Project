import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from spectres import Spectres
from scipy import signal
#from skimage import util

# Setar diretório e arquivo
caminho = 'C:\\Users\\jeanm\\Documents\\Filter-Project\\Data\\'
arquivo_audio1 = "mountain_king_16kHz"
arquivo_audio2 = "queen_of_the_night_16kHz"
spf1 = wave.open(caminho + arquivo_audio1 + '.wav', 'rb')
spf2 = wave.open(caminho + arquivo_audio2 + '.wav', 'rb')

# Caso Stereo
if spf1.getnchannels() == 2:
    spf1 = spf1.mean(axis=1)
elif spf2.getnchannels() == 2:
    spf2 = spf2.mean(axis=1)

# Parâmetros Gerais da Simulação
Fs = 16000  # Frequência de Amostragem
SimTime = 8  # Tempo de Simulação (s)
n = np.arange(0, SimTime, 1/Fs)  # Array de Amostras
sz = 128000  # Taxa do Projeto (Hz)
signal1 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)  # Carregar sinal 1
signal2 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)  # Carregar sinal 2


# Criação do Sinal Portadora de Transmissão
Fc = 3  # Frequência da Portadora
Ac = 1  # Amplitude da Portadora
carrier = Ac*np.cos(2*np.pi*Fc*n + np.pi/2)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.grid()
plt.show()

# Criação do sinal Modulante (Somente para testes)
Fm = 0.5  # Frequência do Modulante
Am = 1  # Amplitude do Modulante
m = Am*np.cos(2*np.pi*Fm*n + np.pi/2)
plt.figure(figsize=(12, 4))
plt.title('Sinal Modulante')
plt.plot(n, m)
plt.show()


# Modulação Sinal de Audio 1 com Portadora(Carrier)
s = carrier * (1 + m/Ac)
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Modulado 1
Spectres.generate_spectres(path=caminho, signal=s, Fs=Fs, stypeName='Modulado_Sinal_1')

# Demodulação do sinal de Audio 1 (COM ERRO, PRECISAMOS REFAZER)
fa = 10
h = s * np.cos(2*np.pi*Fc*n + np.pi/2)
#h = Ac*(1 + (Am/Ac)*m)

plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.ylim(-3, 3)
plt.grid()
plt.show()

# Espectros do sinal Demodulado 1
Spectres.generate_spectres(path=caminho, signal=h, Fs=Fs, stypeName='Demodulado_Sinal_1')

# Filtro Passa-Baixa com Circuito RC
print((1/Fm)*(np.sqrt(1-(Am/Ac)**2)/(Am/Ac)))
RC = 1.5
cutoff = 1/(2*np.pi*RC)  # frequência de corte
B, A = signal.butter(5, Fc*2/Fs, btype='low') # 1st order Butterworth low-pass
filtered_signal = signal.lfilter(B, A, h, axis=0)
plt.figure(figsize=(12, 4))
plt.plot(n, filtered_signal)
plt.title('Sinal Filtrado 1')
plt.show()

#   DownSampling
samps = SimTime * 16000
signal2 = signal.resample(signal2, samps)

# Modulação Sinal de Audio 2 com Portadora(Carrier)
s = carrier * (1 + signal2/Ac)
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Modulado 2
Spectres.generate_spectres(path=caminho, signal=s, Fs=Fs, stypeName='Modulado_Sinal_2')

# Demodulação do sinal de Audio 2 (COM ERRO, PRECISAMOS REFAZER)
h = s * np.cos(2*np.pi*Fc*n + np.pi/2)
plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Demodulado 2
Spectres.generate_spectres(path=caminho, signal=h, Fs=Fs, stypeName='Demodulado_Sinal_2')

# Filtro Passa-Baixa com Circuito RC
B, A = signal.butter(5, Fc*2/Fs, btype='low') # 1st order Butterworth low-pass
filtered_signal = signal.lfilter(B, A, h, axis=0)
plt.figure(figsize=(12, 4))
plt.plot(n, filtered_signal)
plt.title('Sinal Filtrado 2')
plt.show()

