"""Output a audio file"""

import numpy as np
import scipy.io.wavfile as wavfile

rate, data = wavfile.read('myRecording.wav')

sin_data = np.sin(data)

print(sin_data)
