import numpy as np
import os
from tqdm import tqdm
from keras.utils import np_utils
from scipy.misc import imread
from sklearn.model_selection import train_test_split

genre_dict = {"Alt_Rock": 0, "Ambient": 1, "Classical": 2, "Electro_Rock": 3, "Electronica": 4, "Hard_Rock": 5,
              "Hip-Hop": 6, "Jazz": 7, "New_Age": 8, "World": 9}


def load_spectograms(dir_path, flatten="L", test_size=.15):
    """ Loads the spectograms and returns training and testing sets
    :param dir_path:
    :param flatten: ('L' for greyscale, 'RGB' otherwise)
    :param test_size:
    :return : X_train, X_test, y_train, y_test
    """

    X, y = [], []
    for root, _, files in tqdm(list(os.walk(dir_path)), desc='Looping genres'):
        genre = os.path.basename(root)
        for f in tqdm([f for f in files if f.endswith('.png')], desc=genre):
            img = imread(os.path.join(root, f), flatten=flatten)
            X.append(img)
            y.append(genre_dict[genre])
    X = np.divide(X, 255.)
    y = np_utils.to_categorical(np.array(y), 10)

    return train_test_split(X, y, test_size=test_size)
