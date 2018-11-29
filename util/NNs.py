from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Flatten
from keras.layers.recurrent import LSTM


def get_CNN(input_shape):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding="same", input_shape=input_shape, activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 4)))

    model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 4)))

    model.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 4)))

    model.add(Flatten())
    model.add(Dense(500, activation="relu"))

    model.add(Dense(10, activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=["accuracy"])

    return model


def get_LSTM(input_shape):
    print(input_shape)
    model = Sequential()

    model.add(LSTM(units=128, dropout=0.05, recurrent_dropout=0.35, return_sequences=True, input_shape=input_shape))

    model.add(LSTM(units=32, dropout=0.05, recurrent_dropout=0.35, return_sequences=False))

    model.add(Dense(10, activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=["accuracy"])

    return model
