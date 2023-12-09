# This file is used for file conversion, and also...
# - Removing metadata
# - Converting to mono sound
# I just find it easier to call it file_conversion.py.

from tkinter import filedialog as fd # Necessary for selecting a file
from pydub import AudioSegment
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile

class FileConversion():
    def __init__(self):
        # Output file name.
        self.dst = "output.wav"


    filetypes = (
        ('.wav files', '*.wav'),
        ('.mp3 files', '*.mp3'),
        ('.aac files', '*.aac'),
        ('All files', '*.*')
    )
    filetuple = ['.wav', '.mp3', '.aac']  # Tuple of supported file types.

    filename = fd.askopenfilename(
        title='Choose a file...',
        initialdir='/',
        filetypes=filetypes)

    # As the function explains this converts the file to a .wav file.
    # It also merges the sound channels into 1.
    def convertToWav(self):
        # A check is ran to see if the file is a .mp3 or .aac.
        if self.filename[-4:] == ".mp3":
            sound = AudioSegment.from_mp3(self.filename)
            sound = sound.set_channels(1)
            sound.export(self.dst, format="wav")
        elif self.filename[-4:] == ".aac":
            sound = AudioSegment.from_file(self.filename, "aac")
            sound = sound.set_channels(1)
            sound.export(self.dst, format="wav")

    # Clears any metadata attached to the file.
    # Does not need to be ran unless the file is .wav.
    def removeMeta(self):
        sound = AudioSegment.from_file(self.filename, format="wav")
        sound = sound.set_channels(1)
        sound.export(self.dst, format="wav")

test = FileConversion()
test.removeMeta()
