Music genre classification using Keras and the [MagnaTagATune dataset](http://mirg.city.ac.uk/codeapps/the-magnatagatune-dataset), as part of a paired research project. We've included scripts to download the dataset and preprocess the data. Our approach was to compute the spectograms of the songs to then train the neural networks on these spectograms.

## Instructions

#### Initialization
Initialize the project (download data and convert mp3s to wavs):
```
$ ./init.sh
```
#### Preprocessing
Compute mel spectogram (-c option for coloured spectograms and -m option for mel-spectogram):
```
$ python3 util/make_spectogram.py
```

Resize spectograms (for faster computation and better performance on simple NNs):
```
$ python3 util/resize.py factor path_to_spectogram_dir
```
factor should preferably be a multiple of 2.

#### Training
Finaly, train a neural network (loss and accuracy plots, and a confusion matrix will be saved to data/plots, the model will be save to data/models):
```
$ python3 main.py NN_type path_to_spectogram_dir
```
NN_type should be one of CNN or LSTM.
