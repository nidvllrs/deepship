import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

cargoList       = [15,27,38,41,44,62,69,78,96,99,103,110]
passengerList   = [1,4,5,6,8,9,12,14,16,17,23,27,29,30,31,32,33,37,41,50]
tankerList      = [2,5,6,8,9,10,12,13,14,18,19,20,21,24,29,30,32,33,35,38,39,41,42,43,47,48,49,50]
tugList         = [9,40,49]

def plotmelspecs(wavno,i,j,boatType,fig,ax):
    y, sr = librosa.load((f"C:\\Users\\camer\\MDM3\\PHASE_B\\Dataset\\{boatType}\\{wavno}.wav"))
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, ax=ax[i,j])
    fig.colorbar(img, ax=ax[i,j], format='%+2.0f dB')

def plotTwelve(i,j,type):
    fig, ax = plt.subplots(i,j)
    for k in range(i):
        for v in range(j):
            if type == "onlyCargo":
                cargoNum = cargoList[3*k+v]
                plotmelspecs(cargoNum,k,v,"Cargo",fig,ax)
            if type == "onlyPassenger":
                passengerNum = passengerList[3*k+v]
                plotmelspecs(passengerNum,k,v,"Passenger",fig,ax)
            if type == "onlyTanker":
                tankerNum = tankerList[3*k+v]
                plotmelspecs(tankerNum,k,v,"Tanker",fig,ax)
            if type == "onlyTug":
                tugNum = tugList[3*k+v]
                plotmelspecs(tugNum,k,v,"Tug",fig,ax)
            if type == "allTypes":
                cargoNum = cargoList[v]
                passengerNum = passengerList[v]
                tankerNum = tankerList[v]
                tugNum = tugList[v]
                if k == 0:
                    plotmelspecs(cargoNum,k,v,"Cargo",fig,ax)
                if k == 1:
                    plotmelspecs(passengerNum,k,v,"Passengership",fig,ax)
                if k == 2:
                    plotmelspecs(tankerNum,k,v,"Tanker",fig,ax)
                if k == 3:
                    plotmelspecs(tugNum,k,v,"Tug",fig,ax)

plotTwelve(4,3,"onlyTanker")

plt.show()
