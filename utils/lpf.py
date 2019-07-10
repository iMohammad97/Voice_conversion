'''
Implements low pass filter for using in TD-PSOLA
'''

import numpy as np
from scipy.signal import butter, filtfilt


def lpf(x, cutoff, fs, order=5):
    '''
    Args:
        x      (array): signal data (numpy array)
        cutoff (float): cutoff frequency (Hz)
        fs       (int): sample rate (Hz)
        order    (int): order of filter (default 5)

    Returns:
        filtered (array): low pass filtered data
    '''
    nyquist = fs / 2
    b, a = butter(order, cutoff / nyquist)
    # if not np.all(np.abs(np.roots(a)) < 1):
    #     raise PsolaError('Filter with cutoff at {} Hz is unstable given '
    #                      'sample frequency {} Hz'.format(cutoff, fs))
    filtered = filtfilt(b, a, x, method='gust')
    return filtered
