import matplotlib.pyplot as plt
import numpy as np
import wave
from spectres import Spectres
from scipy import signal as sgn
import librosa
from sklearn import metrics
from scipy.signal import freqs, iirfilter


# Setar diretório e arquivo
caminho = 'C:/Users/Maria Luize/Downloads/blocos engcomp/Git_Projects/Filter-Project/Data/'
arquivo_audio1 = "queen_of_the_night_16kHz"
arquivo_audio2 = "mountain_king_16kHz"

spf1 = wave.open(caminho + arquivo_audio1 + '.wav', 'rb')
spf2 = wave.open(caminho + arquivo_audio2 + '.wav', 'rb')

# Caso Stereo
if spf1.getnchannels() == 2:
    spf1 = spf1.mean(axis=1)
elif spf2.getnchannels() == 2:
    spf2 = spf2.mean(axis=1)
# elif spf3.getnchannels() == 2:
#     spf3 = spf3.mean(axis=1)

# Parâmetros Gerais da Simulação
F_Amostragem = 16000  # Frequência de Amostragem Inicial dos Audios
SimTime = 8  # Tempo real de Simulação (s)
T = 1/F_Amostragem  # Período de Amostragem
n = np.arange(0, SimTime, T)  # Array de Amostras

sz = F_Amostragem * SimTime  # Taxa do Projeto (Hz) (Para os sinais de audio terem a mesma taxa de amostragem)

signal1 = np.frombuffer(spf1.readframes(sz), dtype=np.int16)  # Carregar sinal 1
signal2 = np.frombuffer(spf2.readframes(sz), dtype=np.int16)  # Carregar sinal 2
signal2_orig =signal2
signal1_orig = signal1

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
# librosa.output.write_wav(caminho + arquivo_audio1 + '_downsampling1.wav', signal1, F_Amostragem)

# Downsampling do Sinal 2
M = 2  # Fator de dizimação
signal2 = sgn.decimate(signal2, M)  # Dizimação de parte do Sinal


# Ajuste no Número de Amostras
Fs = 8000
n2 = np.arange(0, SimTime, 1/Fs)  # Array de Amostras Após o Downsampling

# Criação do Sinal Portadora de Transmissão1
Fcarrier = 4  # Frequência da Portadora
Acarrier = 0.7  # Amplitude da Portadora
Phcarrier = np.pi/2  # Fase da Portadora
carrier = Acarrier*np.cos(2*np.pi*Fcarrier*n2 + Phcarrier)  # Senóide
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora1')
plt.plot(n2, carrier)
plt.grid()
plt.show()


# Criação do Sinal Portadora de Transmissão2
Fcarrier2 = 2  # Frequência da Portadora2
Acarrier2 = 1  # Amplitude da Portadora2
Phcarrier2 = np.pi/2  # Fase da Portadora2
carrier2 = Acarrier2*np.cos(2*np.pi*Fcarrier2*n2 + Phcarrier2)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora2')
plt.plot(n2, carrier2)
plt.grid()
plt.show()


# Modulação Sinal de Audio 1 com Portadora(Carrier)
s1 = carrier * signal1
plt.figure(figsize=(12, 4))
plt.plot(n2, s1)
plt.title('Sinal Modulado 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Modulado 1
Spectres.generate_spectres(path=caminho, signal=s1, Fs=Fs, stypeName='Modulado_Sinal_1')

# Salvar sinal Modulado 1
# librosa.output.write_wav(caminho + arquivo_audio1 + '_modulado1.wav', s1, Fs)


# Modulação Sinal de Audio 2 com Portadora2(Carrier2)
s2 = carrier2 * signal2
plt.figure(figsize=(12, 4))
plt.plot(n2, s2)
plt.title('Sinal Modulado 2')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Espectros do sinal Modulado 2
Spectres.generate_spectres(path=caminho, signal=s2, Fs=Fs, stypeName='Modulado_Sinal_2')

# Salvar sinal Modulado 1
# librosa.output.write_wav(caminho + arquivo_audio2 + '_modulado2.wav', s2, Fs)

# Somatório dos Sinais Modulados
sinal_somado = s1 + s2
plt.figure(figsize=(12, 4))
plt.plot(n2, sinal_somado)
plt.title('Sinal Somado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()



# Filtro Passa-Faixa, obter sinal1
gpass= 2 # Ripple na banda de passagem
gstop= 40 # Atenuação na banda de rejeição
fs1=9000 # Frequências de rejeição
fp1= 11000# Frequências de corte
fp2=13000
fs2=14000
fn = Fs/2 # Frequência de Nyquist
Wp1=fp1/fn  # Frequências normalizada
Wp2=fp2/fn  
Ws1=fs1/fn 
Ws2=fs2/fn 

a = abs(np.fft.fftshift(np.fft.fft(sinal_somado)))
#a = a[int(len(a)/2):len(a)-1]
freqs = np.fft.fftfreq(len(a))
#order, Wc = sgn.buttord([Wp1, Wp2], [Ws1, Ws2], gpass, gstop)
#B, A = sgn.butter(order, Wc, btype='bandpass', fs=Fs2)
B,A = sgn.iirdesign(wp = [0.15, 0.4], ws= [0.05, 0.55], gstop= gstop, gpass=gpass, ftype='butter')
filtered_signal = sgn.lfilter(B, A, sinal_somado, axis=0)
w, h = sgn.freqz(B, A)
print(Wp1)
print(Wp2)
print(Ws1)
print(Ws2)
#print(Wc)
#print(order/2)

fig = plt.figure(figsize=(18,5))
ax1 = fig.add_subplot(1, 1, 1)
ax2 = ax1.twinx()
t = np.linspace(0., 10., 100)
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax2.plot(freqs, a, 'g')

ax1.set_title('Digital filter frequency response')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
plt.show()

#plt.plot(freqs, a,  color='green')

#angles = np.unwrap(np.angle(h))

#ax2.set_ylabel('', color='g')

#plt.figure(figsize=(12, 4))
#plt.title('Sinal Filtrado')
#plt.xlabel('Tempo(s)')
#plt.ylabel('Amplitude')
#plt.plot(n2, y)

# Demodulação do sinal Somado, obter sinal1
h1 = filtered_signal * np.cos(2*np.pi*Fcarrier*n2 + np.pi/2)
plt.figure(figsize=(12, 4))
plt.plot(n2, h1)
plt.title('Sinal Demodulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()

#  Espectros Sinal Demodulado
spectrum = np.fft.fft(h1)
freqs = np.fft.fftfreq(len(spectrum))
magnitude = np.abs(spectrum)    # Amplitude do Sinal
plt.figure(figsize=(12, 4))
plt.plot(freqs, magnitude)
plt.title('Espectros do Sinal Modulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.show()


# Upsampling do Sinal
L = 2 
x = sgn.upfirdn([1], h1, L)
#x = sgn.resample(x, 128000)
print(x)
plt.figure(figsize=(12, 4))
plt.plot(n, x)
plt.title('Sinal')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.show()
# Salvar Audio
librosa.output.write_wav(caminho + arquivo_audio1 + '_saida.wav', x, F_Amostragem)


# Erro Medio Quadratico(MSE)
erro = metrics.mean_squared_error(x, signal1_orig)
print('Erro Medio Quadratico(MSE): ', erro)


#Calculo de SNR
avgPower1 = 0
avgPower2 = 0
for i in signal1_orig:
    avgPower1 += i ** 2
for i in x:
    avgPower2 += i ** 2

print('SNR: ', 10 * np.log10(avgPower1 / len(signal1_orig) / (avgPower2 / len(x))))
