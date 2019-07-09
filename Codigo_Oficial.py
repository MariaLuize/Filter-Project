import matplotlib.pyplot as plt
import numpy as np
import wave
from spectres import Spectres
from scipy import signal as sgn

# Setar diretório e arquivo
caminho = 'C:\\Users\\jeanm\\Documents\\Filter-Project\\Data\\'
arquivo_audio1 = "High-pitch-sound"
arquivo_audio2 = "Low-frequency-sound-60-hz"
spf1 = wave.open(caminho + arquivo_audio1 + '.wav', 'rb')
spf2 = wave.open(caminho + arquivo_audio2 + '.wav', 'rb')

# Caso Stereo
if spf1.getnchannels() == 2:
    spf1 = spf1.mean(axis=1)
elif spf2.getnchannels() == 2:
    spf2 = spf2.mean(axis=1)

# Parâmetros Gerais da Simulação
F_Amostragem = 16000  # Frequência de Amostragem Inicial dos Audios
SimTime = 8  # Tempo real de Simulação (s)
T = 1/F_Amostragem  # Período de Amostragem
n = np.arange(0, SimTime, T)  # Array de Amostras

sz = F_Amostragem * SimTime  # Taxa do Projeto (Hz) (Para os sinais de audio terem a mesma taxa de amostragem)

signal1 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)  # Carregar sinal 1
signal2 = np.frombuffer(spf2.readframes(sz), dtype=np.int16)  # Carregar sinal 2

# sinal de Audio 1
plt.figure(figsize=(12, 4))
plt.title('Sinal Modulante 1')
plt.plot(n, signal1)
plt.show()

# sinal de Audio 2
plt.figure(figsize=(12, 4))
plt.title('Sinal Modulante 2')
plt.plot(n, signal2)
plt.show()

# Downsampling do Sinal 1
M = 2  # Fator de dizimação
signal1 = sgn.decimate(signal1, M)  # Dizimação de parte do Sinal

# Downsampling do Sinal 2
M = 2  # Fator de dizimação
signal2 = sgn.decimate(signal2, M)  # Dizimação de parte do Sinal


# Ajuste no Número de Amostras
Fs = 8000
n2 = np.arange(0, SimTime, 1/Fs)  # Array de Amostras Após o Downsampling

# Criação do Sinal Portadora de Transmissão
Fcarrier = 6  # Frequência da Portadora
Acarrier = 1  # Amplitude da Portadora
Phcarrier = np.pi/2  # Fase da Portadora
carrier = Acarrier*np.cos(2*np.pi*Fcarrier*n2 + Phcarrier)  # Senóide
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n2, carrier)
plt.grid()
plt.show()

# Modulação Sinal de Audio 1 com Portadora(Carrier)
s1 = carrier * (1 + signal1/Acarrier)
plt.figure(figsize=(12, 4))
plt.plot(n2, s1)
plt.title('Sinal Modulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Modulado 1
Spectres.generate_spectres(path=caminho, signal=s1, Fs=Fs, stypeName='Modulado_Sinal_1')

# Modulação Sinal de Audio 2 com Portadora(Carrier)
s2 = carrier * (1 + signal2/Acarrier)
plt.figure(figsize=(12, 4))
plt.plot(n2, s2)
plt.title('Sinal Modulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Modulado 2
Spectres.generate_spectres(path=caminho, signal=s2, Fs=Fs, stypeName='Modulado_Sinal_2')

# Somatório dos Sinais Modulados
sinal_somado = s1 + s2
plt.figure(figsize=(12, 4))
plt.plot(n2, sinal_somado)
plt.title('Sinal Somado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Demodulação do sinal
h = sinal_somado * np.cos(2*np.pi*Fcarrier*n2 + Phcarrier)
plt.figure(figsize=(12, 4))
plt.plot(n2, h)
plt.title('Sinal Demodulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Demodulado
Spectres.generate_spectres(path=caminho, signal=h, Fs=Fs, stypeName='Demodulado_Sinal')

# Filtro Passa-Faixa
gpass= 3 # Ripple na banda de passagem
gstop= 80 # Atenuação na banda de rejeição
fp1= 13000# Frequências de corte
fp2=2000
fs1=1000 # Frequências de rejeição
fs2=0
fn = Fs/2 # Frequência de Nyquist
Wp1=fp1/fn # Frequências normalizada
Wp2=fp2/fn
Ws1=fs1/fn
Ws2=fs2/fn

a = abs(np.fft.fftshift(np.fft.fft(h)))
a = a[int(len(a)/2):len(a)-1]
freqs = np.fft.fftfreq(len(a))
order, Wc = sgn.buttord([Wp1, Wp2], [Ws1, Ws2], gpass, gstop)
B, A = sgn.butter(order, Wc, btype='bandpass', fs=Fs)
filtered_signal = sgn.lfilter(B, A, h1, axis=0)
w, h = sgn.freqz(B, A)
print(Wp1)
print(Wp2)
print(Ws1)
print(Ws2)
print(Wc)

fig, ax1 = plt.subplots()
#plt.plot(freqs, a,  color='green')
ax1.set_title('Digital filter frequency response')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax2 = ax1.twinx()
#angles = np.unwrap(np.angle(h))
ax2.plot(freqs, a, 'g')
ax2.set_ylabel('', color='g')

plt.figure(figsize=(12, 4))
plt.plot(n2, filtered_signal)
plt.title('Sinal')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')


# Upsampling do Sinal
L = 2
x = sgn.upfirdn([1], filtered_signal, L)
plt.figure(figsize=(12, 4))
plt.plot(n, x)
plt.title('Sinal')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')