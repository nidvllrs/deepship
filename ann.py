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
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve

data = pd.read_csv(r'C:\Users\ndvll\PycharmProjects\MDM3\Techmodal\dataset.csv')
data.head()# Dropping unneccesary columns
data = data.drop(['filename'],axis=1)#Encoding the Labels
genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)#Scaling the Feature columns
scaler = StandardScaler()
X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype = float))#Dividing data into training and Testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential()
model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

classifier = model.fit(X_train,
                    y_train,
                    epochs=100,
                    batch_size=128)

preds=model.predict(X_test)
print(accuracy_score(y_test,preds))