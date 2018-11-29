import pandas as pd
import os
import pydub
from tqdm import tqdm
from log import logger


class Track:
    def __init__(self, s):
        L = s.replace(".wav", "").replace("_", " ").split("-")
        self.artist = L[0]
        self.album = L[1]
        self.tracknum = int(L[2])
        self.trackname = L[3]
        self.start = L[4]
        self.end = L[5]


df = pd.read_csv("data/csv/song_info.csv", error_bad_lines=False, warn_bad_lines=False)

df["albumname"] = df["albumname"].str.lower()
df["artist"] = df["artist"].str.lower()
df["trackname"] = df["trackname"].str.lower()


def get_genre(t):
    """
    Returns the genre of a track based on data/csv/song_info.csv. Does not work for every track, but allows for a
    decent amount of tracks to be labelled.
    :param t: Track object
    :return: track genre
    """
    L1 = t.trackname.split(" ")
    L1.sort(key=len, reverse=True)
    L1 = L1[0:int(len(L1) * 0.2) + 1]
    L2 = t.album.split(" ")
    L2.sort(key=len, reverse=True)
    L2 = L2[0:int(len(L2) * 0.2) + 1]
    L3 = t.artist.split(" ")
    L3.sort(key=len, reverse=True)
    L3 = L3[0:int(len(L3) * 0.2) + 1]
    bool_1 = df["trackname"].str.match('|'.join(L1))
    bool_2 = df["tracknum"] == t.tracknum
    bool_3 = df["albumname"].str.match('|'.join(L2))
    bool_4 = df["artist"].str.match('|'.join(L3))

    try:
        return df[(bool_1 & bool_2)]["mp3genre"].unique().item()
    except ValueError:
        pass
    try:
        return df[(bool_1 & bool_3)]["mp3genre"].unique().item()
    except ValueError:
        pass
    try:
        return df[(bool_1 & bool_4)]["mp3genre"].unique().item()
    except ValueError:
        pass
    try:
        return df[(bool_1 & (bool_2 | bool_3))]["mp3genre"].unique().item()
    except ValueError:
        pass
    try:
        return df[(bool_1 & (bool_2 | bool_4))]["mp3genre"].unique().item()
    except ValueError:
        pass
    try:
        return df[(bool_1 & (bool_3 | bool_4))]["mp3genre"].unique().item()
    except ValueError:
        return None


def make_wav():
    MP3s = [f for f in os.listdir("data/mp3/") if f.endswith('.mp3')]
    for f in tqdm(MP3s):
        genre = get_genre(Track(f))
        if genre is not None:
            genre = genre.replace(" ", '_')
            try:
                mp3 = pydub.AudioSegment.from_mp3("data/mp3/" + f)
                mp3.export("data/wav/{}/{}".format(genre, f.replace(".mp3", ".wav")), format="wav")
            except pydub.exceptions.CouldntDecodeError:
                logger.error("could not convert file {} to wav".format(f), exc_info=True)


if __name__ == '__main__':
    make_wav()
