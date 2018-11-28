import scipy.io.wavfile
import os
import argparse
from log import logger

import matplotlib

# To be able to use matplotlib in venv on OSX
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# For mel-spectograms
import librosa
import librosa.display
import numpy as np
from tqdm import tqdm


def make_spectogram(cmap="Greys"):
    out_path = "data/spectogram_{}".format(cmap.lower())
    os.system("./init_genre_dir.sh {}".format(out_path))
    for root, _, files in tqdm(list(os.walk(wav_path)), desc='Looping genres'):
        genre = os.path.basename(root)
        genre_path = os.path.join(out_path, genre)
        for f in tqdm([f for f in files if f.endswith('.wav')], desc=genre):
            rate, audData = scipy.io.wavfile.read(os.path.join(root, f))
            channel1 = audData  # left

            fig, ax = plt.subplots(1)
            fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
            plt.specgram(channel1, Fs=rate, NFFT=1024, cmap=cmap)
            ax.axis('off')

            plt.savefig(os.path.join(genre_path, f.replace(".wav", ".png")), frameon='false')
            plt.close('all')


def make_mel_spectogram(cmap="Greys"):
    out_path = "data/mel_spectogram_{}".format(cmap.lower())
    os.system("./init_genre_dir.sh {}".format(out_path))
    for root, _, files in tqdm(list(os.walk(wav_path)), desc='Looping genres'):
        genre = os.path.basename(root)
        genre_path = os.path.join(out_path, genre)
        for f in tqdm([f for f in files if f.endswith('.wav')], desc=genre):
            sig, fs = librosa.load(os.path.join(root, f))

            fig, ax = plt.subplots(1)
            fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
            S = librosa.feature.melspectrogram(y=sig, sr=fs, fmax=8000)
            librosa.display.specshow(librosa.power_to_db(S, ref=np.max), y_axis='linear', x_axis='time', cmap=cmap)
            ax.axis("off")

            plt.savefig(os.path.join(genre_path, f.replace(".wav", ".png")), frameon='false')
            plt.close('all')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate spectograms as PNGs (greyscale by default)')

    parser.add_argument('-m', '--mel', action='store_true', help='generate mel-spectograms')
    parser.add_argument('-c', '--colour', action='store_true', help='generate coloured spectograms (autumn cmap)')
    args = parser.parse_args()

    wav_path = 'data/wav/'
    genres = [g for g in os.listdir(wav_path) if os.path.isdir(wav_path + g)]

    if args.colour:
        cmap = "autumn"
    else:
        cmap = "Greys"

    if args.mel:
        make_mel_spectogram(cmap)
    else:
        make_spectogram(cmap)
