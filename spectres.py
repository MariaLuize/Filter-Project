import matplotlib.pyplot as plt
import numpy as np


#  Método Gerador de Graficos de espectros
class Spectres(object):  # (É NECESSÁRIO REVER COERÊNCIA DAS FUNÇÕES QUE GERAM MAGNITUDE E FASE)
    @staticmethod
    def generate_spectres(path, signal, Fs, stypeName):
        spectrum = np.fft.fft(signal)  # Transformada de Fourier
        freqs = np.fft.fftfreq(len(spectrum))  # Frequências do Sinal
        magnitude = np.abs(spectrum)    # Amplitude do Sinal
        phase = np.angle(spectrum)  # Fase do Sinal
        plt.subplot(2, 1, 1)
        #plt.magnitude_spectrum(s, Fs=Fs, color='C1')
        plt.plot(freqs, magnitude)
        plt.title('Espectros do Sinal Modulado')
        plt.ylabel("Magnitude")
        plt.xlabel('Frequência (kHz)')
        plt.subplot(2, 1, 2)
        plt.phase_spectrum(signal, Fs=Fs, color='C2')
        #plt.plot(freqs, phase)
        plt.xlabel('Frequência (kHz)')
        plt.ylabel("Fase")
        plt.tight_layout()
        plt.savefig(path + "Amplitude_Fase_" + stypeName)
