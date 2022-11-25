import librosa
import os
import csv
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import keras
from sklearn.model_selection import train_test_split
from keras import layers
from keras import layers
import pandas as pd
from keras.models import Sequential
import warnings
warnings.filterwarnings('ignore')


files = os.listdir(r"C:/Users/ndvll/Desktop/Project 2/")

header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()

file = open('dataset.csv', 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)

genres = 'Cargo Passengership Tanker Tug'.split()

for g in genres:
    for filename in os.listdir(f'C:/Users/ndvll/Desktop/Project 2//{g}'):
        songname = f'C:/Users/ndvll/Desktop/Project 2//{g}/{filename}'
        y, sr = librosa.load(songname)
        rmse = librosa.feature.rms(y=y)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        to_append += f' {g}'
        file = open('dataset.csv', 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(to_append.split())

