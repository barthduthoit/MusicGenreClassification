import numpy as np
import os
from tqdm import tqdm
from keras.utils import np_utils
import cv2
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools
import datetime

import matplotlib

# To be able to use matplotlib in venv on OSX
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

genre_dict = {"Alt_Rock": 0, "Ambient": 1, "Classical": 2, "Electro_Rock": 3, "Electronica": 4, "Hard_Rock": 5,
              "Hip-Hop": 6, "Jazz": 7, "New_Age": 8, "World": 9}


def load_spectograms(dir_path, reshape=False, test_size=.15):
    """ Loads the spectograms and returns training and testing sets
    :param dir_path:
    :param test_size:
    :return : X_train, X_test, y_train, y_test
    """

    X, y = [], []
    for root, _, files in tqdm(list(os.walk(dir_path)), desc='Looping genres'):
        genre = os.path.basename(root)
        if "greys" in root:
            colour_flag = cv2.IMREAD_GRAYSCALE
        else:
            colour_flag = cv2.MREAD_COLOR
        for f in tqdm([f for f in files if f.endswith('.png')], desc=genre):
            img = cv2.imread(os.path.join(root, f), colour_flag)
            X.append(img)
            y.append(genre_dict[genre])
    X = np.divide(X, 255.)
    y = np_utils.to_categorical(np.array(y), 10)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    if reshape and colour_flag == cv2.IMREAD_GRAYSCALE:
        X_train = X_train.reshape(X_train.shape + (1,))
        X_test = X_test.reshape(X_test.shape + (1,))
    return X_train, X_test, y_train, y_test


def plot_history(history, name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.plot(history["acc"], label="Training")
    plt.plot(history["val_acc"], label="Validation")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Accuracy over epochs")
    plt.savefig(os.path.join("data/plots", "{}_accuracy_{}.png".format(name, timestamp)))

    plt.gcf().clear()

    plt.plot(history["loss"], label="Training")
    plt.plot(history["val_loss"], label="Validation")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss over epochs")
    plt.savefig(os.path.join("data/plots", "{}_loss_{}.png".format(name, timestamp)))


def plot_confusion_matrix(cm, classes, cmap=plt.cm.Oranges):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label', fontsize=14)
    plt.xlabel('Predicted label', fontsize=14)


def save_confusion_matrix(y_test, y_pred, name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=genre_dict.keys())
    plt.tight_layout()
    plt.savefig(os.path.join("data/plots", "{}_confusion_{}.png".format(name, timestamp)))
