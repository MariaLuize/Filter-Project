import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from spectres import Spectres


# Setar diretório e arquivo
caminho = "/home/jean/Documentos/Filter-Project/Data/"
arquivo_audio1 = "mountain_king_16kHz"
arquivo_audio2 = "queen_of_the_night_16kHz"
spf1 = wave.open(caminho + arquivo_audio1 + '.wav', 'rb')
spf2 = wave.open(caminho + arquivo_audio2 + '.wav', 'rb')

# Caso Stereo
if spf1.getnchannels() == 2 or spf2.getnchannels() == 2:
    print('Apenas arquivos mono')
    sys.exit(0)

# Parâmetros Gerais da Simulação
Fs = 16000  # Frequência de Amostragem
SimTime = 8  # Tempo de Simulação (s)
n = np.arange(0, SimTime, 1/Fs)  # Array de Amostras
sz = 128000  # Taxa do Projeto (Hz)
signal1 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)  # Carregar sinal 1
signal2 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)  # Carregar sinal 2

# Criação do Sinal Portadora de Transmissão
Fc = 6  # Frequência da Portadora
Ac = 3  # Amplitude da Portadora
carrier = Ac*np.cos(2*np.pi*Fc*n)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.grid()
plt.show()

# Criação do sinal Modulante (Somente para testes)
# Fm = 0.5  # Frequência do Modulante
# Am = 1  # Amplitude do Modulante
# m = Am*np.cos(2*np.pi*Fm*n)
# plt.figure(figsize=(12, 4))
# plt.title('Sinal Modulante')
# plt.plot(n, m)
# plt.show()


# Modulação Sinal de Audio 1 com Portadora(Carrier)
s = carrier * (1 + signal1/Ac)

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
h = s * np.cos(2*np.pi*fa*n)

plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Demodulado 1
Spectres.generate_spectres(path=caminho, signal=h, Fs=Fs, stypeName='Demodulado_Sinal_1')

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
fa = 10
h = s * np.cos(2*np.pi*fa*n)

plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Demodulado 2
Spectres.generate_spectres(path=caminho, signal=h, Fs=Fs, stypeName='Demodulado_Sinal_2')



