import numpy as np
import tensorflow as tf
from flask import Flask, request
from flask_cors import CORS, cross_origin
from tensorflow.keras.models import load_model
import os
from utils.preprocessing import preprocessing

app = Flask(__name__)


# Apply Flask CORS
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/')
def hello_world():
    print(__name__)
    return 'Hello world'


@app.route('/predict')
def make_prediction():
    model = load_model('model/audio_classification.hdf5')

    path = 'AudioRecording.3gp'
    os.system('ffmpeg -i ' + str(path) + ' audio_test.wav')
    filename = 'audio_test.wav'

    mfccs = preprocessing(filename)
    mfccs = np.array(mfccs)
    mfccs = mfccs.reshape((20, 157, 1))
    mfccs = np.expand_dims(mfccs, axis=0)

    diseases = ['Bronchiectasis', 'Bronchiolitis', 'COPD', 'Healthy', 'Pneumonia', 'URTI']
    predicted_label=model.predict(mfccs)
    classpreds = np.argmax(predicted_label, axis=1)
    prediction_class = diseases[classpreds[0]]
    return 'Your situation: ' + prediction_class


@app.route('/uploadfile',methods=['GET','POST'])
def uploadfile():
    if request.method == 'POST':
        f = request.files['audio']
        filePath = "path/to/your/folder/AudioRecording.3gp"
        f.save(filePath)
        return "Upload file sucess"


# Start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')