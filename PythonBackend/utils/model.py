from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras.layers import LSTM, Bidirectional

def CNN_model(input_shape, dropout_rate):
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=2,
                 input_shape=input_shape, activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(dropout_rate))
    model.add(Dense(64, activation='relu'))

    model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(dropout_rate))
    model.add(Dense(64, activation='relu'))

    model.add(Conv2D(filters=64, kernel_size=2, activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(dropout_rate))


    model.add(GlobalAveragePooling2D())

    model.add(Dense(6, activation='softmax')) 
    return model

def LSTM_model(input_shape, dropout_rate):
    model_lstm = Sequential()
    model_lstm.add(LSTM(128, dropout = 0.3, input_shape=input_shape, recurrent_dropout = 0.3, return_sequences=True))
    model_lstm.add(LSTM(64,  dropout=0.05, recurrent_dropout=0.3, return_sequences=False))
    model_lstm.add(Dense(256, activation = 'relu'))
    model_lstm.add(Dense(64, activation = 'relu'))
    model_lstm.add(Dropout(dropout_rate))
    model_lstm.add(Dense(6, activation = 'softmax'))

    return model_lstm