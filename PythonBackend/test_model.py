import numpy as np
import tensorflow as tf
from flask import Flask 
from flask_cors import CORS, cross_origin
from tensorflow.keras.models import load_model
import librosa
import os

def preprocessing(audio_file):
    sr_new = 16000 # 16kHz sample rate
    x, sr = librosa.load(audio_file, sr=sr_new)

    max_len = 5 * sr_new  
    if x.shape[0] < max_len:
      # padding with zero
      pad_width = max_len - x.shape[0]
      x = np.pad(x, (0, pad_width))
    elif x.shape[0] > max_len:
      # truncated
      x = x[:max_len]

      feature = librosa.feature.mfcc(x, sr=sr_new)
      
      return feature



def make_prediction():
  
    model = load_model('audio_classification.hdf5')
    
    path = 'Hien.3gp'
    os.system('ffmpeg -i ' + str(path) + ' HienVu.wav')
    filename = 'HienVu.wav'
    mfccs = preprocessing(filename)
    mfccs = np.array(mfccs)
    mfccs = mfccs.reshape((20, 157, 1))
    mfccs = np.expand_dims(mfccs, axis=0)

    diseases = ['Bronchiectasis', 'Bronchiolitis', 'COPD', 'Healthy', 'Pneumonia', 'URTI']
    predicted_label=model.predict(mfccs)
    classpreds = np.argmax(predicted_label, axis=1)
    prediction_class = diseases[classpreds[0]]
    return prediction_class

if __name__ == '__main__':
    pred = make_prediction()
    print(pred)
    