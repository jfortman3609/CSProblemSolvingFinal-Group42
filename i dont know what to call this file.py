from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

# Uses the output.wav file in the main file directory
dst = "output.wav"

# pydub is used here to store the audio file in a variable
# This will be used to load things like how long it lasts and such
sound = AudioSegment.from_file(dst, format="wav")
print(sound.duration_seconds)

# scipy is used to load the file as something else other than how long it lasts
samplerate, data = wavfile.read(dst)

# Waveform of the .wav file
# A time array is created for how long the wav file lasts
time = np.linspace(0, sound.duration_seconds, data.shape[0])
waveform = plt.plot(time, data)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

#
plt.plot(time, data)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

