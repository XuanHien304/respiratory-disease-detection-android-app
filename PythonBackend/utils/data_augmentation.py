import librosa
import numpy as np

def add_white_noise(signal, noise_factor):
  noise = np.random.normal(0, signal.std(), signal.size)
  augmented_signal = signal + noise * noise_factor
  return augmented_signal


def time_stretch(signal, stretch_rate):
  return librosa.effects.time_stretch(signal, stretch_rate)


def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr, num_semitones)

