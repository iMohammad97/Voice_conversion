import amfm_decompy.basic_tools as basic
import amfm_decompy.pYAAPT as pYAAPT
import matplotlib.pyplot as plt
import numpy as np
# load audio
signal = basic.SignalObj('file.wav')
filename = 'file.wav'
# YAAPT pitches
pitchY = pYAAPT.yaapt(signal, frame_length=40,
                      tda_frame_length=40, f0_min=75, f0_max=600)

print(np.asarray(pitchY.samp_values))

# plot

fig = plt.subplots(1, 1, sharex=True, sharey=True, figsize=(12, 8))
plt.plot(pitchY.samp_values, label='YAAPT', color='blue')
# plt.savefig('YAAPT.png')
plt.show()
