# haceCalorSpecgram.py
from tkinter import filedialog as fd # Necessary for selecting a file
from os import path
from pydub import AudioSegment
from pydub.playback import play
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile

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

dst = "test.wav"


def convertToWav():
    if filename[-4:] == ".mp3":
        sound = AudioSegment.from_mp3(filename)
        sound.export(dst, format="wav")
    elif filename[-4:] == ".aac":
        sound = AudioSegment.from_file(filename, "aac")
        sound.export(dst, format="wav")

convertToWav()
