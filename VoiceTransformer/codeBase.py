#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sp
import IPython
from scipy.io import wavfile

plt.rcParams["figure.figsize"] = (14,4)

Fs, s = wavfile.read('speech.wav')
s = s / 32767.0 # scale the signal to floats in [-1, 1]
print('sampling rate: {}Hz'.format(Fs))
IPython.display.Audio(s, rate=Fs)

def ms2smp(ms, Fs):
    return int(float(Fs) * float(ms) / 1000.0)

def plot_spec(x, Fs, max_freq=None, do_fft=True):
    C = int(len(x) / 2)  # positive frequencies only
    if max_freq:
        C = int(C * max_freq / float(Fs) * 2)
    X = np.abs(np.fft.fft(x)[0:C]) if do_fft else x[0:C]
    N = Fs * np.arange(0, C) / len(x);
    plt.plot(N, X)
    return N, X

plot_spec(s, Fs, 8000);

def robot_voice(x, f, Fs):
    w = (float(f) / Fs) * 2 * np.pi  # normalized modulation frequency
    return 2 * np.multiply(x, np.cos(w * np.arange(0,len(x))))

IPython.display.Audio(robot_voice(s, 500, Fs), rate=Fs)