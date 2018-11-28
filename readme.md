### Instructions

Initialize the project (download data and convert mp3s to wavs):
'''
$ ./init.sh
'''

Compute mel spectogram (-c option for coloured spectograms and -m option for mel-spectogram):
'''
$ python3 util/make_spectogram.py
'''

Resize spectograms (for faster computation and better performance on simple NNs):
'''
$ python3 util/resize.py factor path_to_spectogram_dir
'''
factor should preferably be a multiple of 2
