import librosa
import numpy as np

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

def features_extractor(file_name):
    #audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast', duration=20)
    audio, sample_rate = librosa.load(file_name)  
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    
    return mfccs_features