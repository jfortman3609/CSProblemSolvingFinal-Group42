from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

dst = "output.wav"

sound = AudioSegment.from_file(dst, format="wav")
print(sound.duration_seconds)

samplerate, data = wavfile.read(dst)

time = np.linspace(0, sound.duration_seconds, data.shape[0])
plt.plot(time, data)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
