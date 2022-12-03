import scipy 
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
'''
File number lists
'''
cargoList       = [15,27,38,41,44,62,69,78,96,99,103,110]
passengerList   = [1,4,5,6,8,9,12,14,16,17,23,27,29,30,31,32,33,37,41,50]
tankerList      = [2,5,6,8,9,10,12,13,14,18,19,20,21,24,29,30,32,33,35,38,39,41,42,43,47,48,49,50]
tugList         = [9,40,49]

CargoFileList = []
PassengerFileList = []
TankerFileList = []
TugFileList = []
def GetFile():
    '''
    run this to get all file names into a list for each boattype
    '''
    for count,value in enumerate(cargoList):
        CargoFileList.append(f'Project_2/Cargo/{value}.wav')
        try:
            PassengerFileList.append(f'Project_2/Passengership/{passengerList[count]}.wav')
        except IndexError:
            continue
        try:
            TankerFileList.append(f'Project_2/Tanker/{tankerList[count]}.wav')
        except IndexError:
            continue
        try:    
            TugFileList.append(f'Project_2/Tug/{tugList[count]}.wav')
        except IndexError:
            continue
    return CargoFileList, PassengerFileList, TankerFileList, TugFileList
GetFile()
def CheckType(BoatType, *args):
    '''
    Use CheckType to run code on seperate boat types, can be used in the future if we need to apply different functions for different boat types
    but right now I'm kinda an idiot since I basically repeated the function 
    '''
    # fileNum = args[0]
    # BoatTypeList = args[1]
    if BoatType == 'Cargo':
        # FastFT(fileNum, BoatTypeList)
        print('null')
    if BoatType == 'Passenger':
        print('null')
        # FastFT(fileNum, BoatTypeList)
    if BoatType == 'Tanker':
        print('null')
        # FastFT(fileNum, BoatTypeList)
    if BoatType == 'Tug':
        print('null')
        # xFastFT(fileNum, BoatTypeList)

def FastFTplot(listIndex, boatTypeList, log=False):
    '''
    using scipy to do fourier transform video used: Fast Fourier Transform (FFT) analysis on wav file using python by Metallicode מטאליקוד
    '''
    s_rate, signal = wavfile.read(boatTypeList[listIndex])
    FFT = abs(scipy.fft.fft(signal)) # fast fourier transform 
    freqVec = fftpk.fftfreq(len(FFT), (1.0/s_rate))
    if log:
        fig = plt.figure()
        ax = plt.gca()
        ax.set_xscale('log')
        ax.set_yscale('log')
    plt.plot(freqVec[range(int(len(FFT)/2))], FFT[range(int(len(FFT)/2))])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title(f'This is a FFT of {boatTypeList[listIndex]}')
    plt.show() 

FastFTplot(0, CargoFileList)
