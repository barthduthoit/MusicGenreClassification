import argparse
import util.utils
import util.NNs
import os
import numpy as np


def main(nn_type, dir_path):
    if nn_type == "CNN":
        X_train, X_test, y_train, y_test = util.utils.load_spectograms(dir_path, reshape=True)
        model = util.NNs.get_CNN(X_train[0].shape)
    elif nn_type == "LSTM":
        X_train, X_test, y_train, y_test = util.utils.load_spectograms(dir_path, reshape=False)
        model = util.NNs.get_LSTM(X_train[0].shape)
    elif nn_type == "conv_LSTM":
        X_train, X_test, y_train, y_test = util.utils.load_spectograms(dir_path, reshape=False)
        model = util.NNs.get_conv_LSTM(X_train[0].shape)

    history = model.fit(X_train, y_train, batch_size=128, epochs=10, verbose=1, validation_data=(X_test, y_test))

    name = "{}_{}".format(os.path.basename(dir_path), nn_type)
    model.save(name)

    util.utils.plot_history(history.history, name)

    y_pred = model.predict_classes(X_test, verbose=0)
    util.utils.save_confusion_matrix(np.argmax(y_test, axis=1), y_pred, name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='train the NN')
    parser.add_argument('nn_type', type=str, choices=['CNN', 'LSTM'], help='type of NN to train')
    parser.add_argument('dir_path', type=str,
                        choices=[os.path.join("data/", f) for f in os.listdir("data/") if "spectogram" in f],
                        help='data to use')
    args = parser.parse_args()
    main(args.nn_type, args.dir_path)
