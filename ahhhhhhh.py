# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:31:18 2022

@author: rebec
"""
# comment out = ctrl + 4
# uncomment = crtl + 1

import matplotlib.pyplot as plt
from scipy.io import wavfile
#import librosa
import soundfile as sf
import scipy
from scipy import signal
import numpy as np

cargoList       = [15,27,38,41,44,62,69,78,96,99,103,110]
passengerList   = [1,4,5,6,8,9,12,14,16,17,23,27,29,30,31,32,33,37,41,50]
tankerList      = [2,5,6,8,9,10,12,13,14,18,19,20,21,24,29,30,32,33,35,38,39,41,42,43,47,48,49,50]
tugList         = [9,40,49]

f = sf.SoundFile(f'Project_2/Cargo/15.wav')
cargoTimes = []
passengerTimes = []
tankerTimes = []
tugTimes = []


for boatNum in cargoList:
    f = sf.SoundFile(f'Project_2/Cargo/{boatNum}.wav')
    time = f.frames/f.samplerate
    cargoTimes.append(time)
    
for boatNum in passengerList:
    f = sf.SoundFile(f'Project_2/Passengership/{boatNum}.wav')
    time = f.frames/f.samplerate
    passengerTimes.append(time)
    
for boatNum in tankerList:
    f = sf.SoundFile(f'Project_2/Tanker/{boatNum}.wav')
    time = f.frames/f.samplerate
    tankerTimes.append(time)

for boatNum in tugList:
    f = sf.SoundFile(f'Project_2/Tug/{boatNum}.wav')
    time = f.frames/f.samplerate
    tugTimes.append(time)    
    
    
# =============================================================================
# fig, axs = plt.subplots(2, 2)
# axs[0, 0].hist(cargoTimes)
# axs[0, 1].hist(passengerTimes)
# axs[1, 0].hist(tankerTimes)
# axs[1, 1].hist(tugTimes)
# =============================================================================


# =============================================================================
# cargoList       = [15,27,38,41,44,62,69,78,96,99,103,110]
# passengerList   = [1,4,5,6,8,9,12,14,16,17,23,27,29,30,31,32,33,37,41,50]
# tankerList      = [2,5,6,8,9,10,12,13,14,18,19,20,21,24,29,30,32,33,35,38,39,41,42,43,47,48,49,50]
# tugList         = [9,40,49]
# =============================================================================
def plotSigSpec(boatNum,boatType):
    samplerate, data = wavfile.read(f'Project_2/{boatType}/{boatNum}.wav')
    plt.subplot(211)
    plt.title(f'Spectrogram {boatType} {boatNum}')
    plt.plot(data)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')

    plt.subplot(212)
    plt.specgram(data,Fs=samplerate)
    plt.xlabel('Time')
    plt.ylabel('Frequency')

    plt.show()



def plotISI(boatNum,boatType,plotIdx):
    samplerate, data = wavfile.read(f'Project_2/{boatType}/{boatNum}.wav')
    ISI = np.diff(data)
    plt.subplot(plotIdx)
    plt.hist(ISI,bins=100)
    plt.title(f"{boatType} {boatNum}")
    plt.show()
    kurt = scipy.stats.kurtosis(data)
    print ("kurtosis = ", kurt)
    
# =============================================================================
# plotISI(15,"Cargo",311) # normal all the way through
# plotISI(27,"Cargo",312) # front heavy
# plotISI(69,"Cargo",313) # back heavy ish
# =============================================================================

plotISI(38,"Cargo",111)
plotSigSpec(38,"Cargo")










