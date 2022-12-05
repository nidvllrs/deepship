# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:31:18 2022

@author: rebec
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile
import librosa

cargoList       = [15,27,38,41,44,62,69,78,96,99,103,110]
passengerList   = [1,4,5,6,8,9,12,14,16,17,23,27,29,30,31,32,33,37,41,50]
tankerList      = [2,5,6,8,9,10,12,13,14,18,19,20,21,24,29,30,32,33,35,38,39,41,42,43,47,48,49,50]
tugList         = [9,40,49]


y, sr = wavfile.read(f'Project_2/Cargo/15.wav')
librosa.get_duration(f'Project_2/Cargo/15.wav')

plt.subplot(211)
plt.title('Spectrogram of a wav file')
plt.plot(sr)
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.specgram(sr,Fs=y)
plt.xlabel('Time')
plt.ylabel('Frequency')

plt.show()