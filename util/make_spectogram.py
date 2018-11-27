import scipy.io.wavfile
import os

import matplotlib
# To be able to use matplotlib in venv on OSX
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# For mel-spectograms
import librosa
import librosa.display
import numpy as np

wav_path = 'data/wav/'
genres = [g for g in os.listdir(wav_path) if os.path.isdir(wav_path + g)]

def make_spectogram():
    for genre in genres:
        for f in [f for f in os.listdir(wav_path + genre) if (f.endswith(".wav"))]:
            rate, audData = scipy.io.wavfile.read(wav_path + genre + "/" + f)
            channel1 = audData  # left

            fig, ax = plt.subplots(1)
            fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.specgram(channel1, Fs=rate, NFFT=1024, cmap="Greys")
            ax.axis('off')

            plt.savefig('data/spectogram/{}/{}'.format(genre, f.replace(".wav", ".png")), frameon='false')
            plt.close('all')


def make_mel_spectogram():
    for genre in genres:
        for f in [f for f in os.listdir(wav_path + genre) if (f.endswith(".wav"))]:
            sig, fs = librosa.load(wav_path + genre + "/" + f)

            fig, ax = plt.subplots(1)
            fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
            S = librosa.feature.melspectrogram(y=sig, sr=fs, fmax=8000)
            librosa.display.specshow(librosa.power_to_db(S, ref=np.max), y_axis='linear', x_axis='time', cmap="Greys")
            ax.axis("off")

            plt.savefig('data/spectogram/{}/{}'.format(genre, f.replace(".wav", ".png")), frameon='false')
            plt.close('all')


if __name__ == '__main__':
    make_spectogram()
