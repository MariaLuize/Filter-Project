import librosa
import matplotlib.pyplot as plt
import librosa.display

sig, sr = librosa.load(r'/Data/queen_of_the_night_16KHz.wav', duration=8.0)
#ipd.Audio(sig, rate=sr)
print ("Taxa de amostragem Sinal 1: ", sr)
print ("Numero de amostras Sinal 1: ", sig.shape)

plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
librosa.display.waveplot(sig, sr=sr)
plt.title('Sinal 1')
plt.show()

sig2, sr2 = librosa.load(r'/Data/mountain_king_16kHz.wav', duration=8.0)
#ipd.Audio(sig2, rate=sr2)
print ("Taxa de amostragem Sinal 2: ", sr2)
print ("Numero de amostras Sinal 2: ", sig2.shape)

plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
librosa.display.waveplot(sig2, sr=sr2)
plt.title('Sinal 2')
plt.show()

librosa.output.write_wav('/Data/Saida_queen_of_the_night_16KHz.wav', sig, sr)
#ipd.Audio(sig, rate=sr)
librosa.output.write_wav('/Data/Saida_mountain_king_16KHz.wav', sig2, sr2)
#ipd.Audio(sig2, rate=sr2)
