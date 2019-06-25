import librosa
import matplotlib.pyplot as plt
import librosa.display
import  numpy as np

# Carregar Sinal de Audio .wav 1
sig, sr = librosa.load(r'/home/jean/Documentos/Filter-Project/Data/mountain_king_16kHz.wav', duration=8.0)
#ipd.Audio(sig, rate=sr)
print ("Taxa de amostragem Sinal 1: ", sr)
print ("Numero de amostras Sinal 1: ", sig.shape)

Fs = 16000
n = np.arange(0, 8, 1/Fs)

# Plotar sinal de audio 1
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
librosa.display.waveplot(sig, sr=sr)
plt.title('Sinal 1')
plt.show()

# Carregar Sinal de Audio .wav 2
sig2, sr2 = librosa.load(r'/home/jean/Documentos/Filter-Project/Data/mountain_king_16kHz.wav', duration=8.0)
#ipd.Audio(sig2, rate=sr2)
print ("Taxa de amostragem Sinal 2: ", sr2)
print ("Numero de amostras Sinal 2: ", sig2.shape)

# Plotar sinal de audio 2
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
librosa.display.waveplot(sig2, sr=sr2)
plt.title('Sinal 2')
plt.show()

Ac = 1
c = Ac*np.cos(2*np.pi*16000*n)

Fm = 2
Am = 1
m = Am*np.sin(2*np.pi*Fm*n)

s = c * (1 + sig/Ac)

plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Modulation Case')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()



# #plt.plot(sorted(freq_interest_points), abs(frequency_response), marker='o', linestyle='-', color='red', label="Resposta Aproximada")
# plt.plot(frequency_list, amplitude_list, label="Resposta Desejada")
# plt.xlabel("Frequência")
# plt.ylabel("Amplitude")
# plt.title("Transformada")
# plt.legend()
# plt.grid()
# plt.figure()
#
#
# #plt.plot(sorted(freq_interest_points), [180*angle(f)/pi for f in frequency_response], marker='o', linestyle='-', color='red', label="Resposta Aproximada")
# plt.plot(frequency_list, phase_list, label="Resposta Desejada")
# plt.xlabel("Frequência")
# plt.ylabel("Fase")
# plt.title("Transformada")
# plt.legend()
# plt.grid()
# plt.show()
#
# # Gerar arquivos de audio .wav
# librosa.output.write_wav('/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/FIles/Saida_Voz01_16KHz.wav', sig, sr)
# #ipd.Audio(sig, rate=sr)
# librosa.output.write_wav('/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/FIles/Saida_Voz02_16KHz.wav', sig2, sr2)
# #ipd.Audio(sig2, rate=sr2)
