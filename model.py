# The goal of this script is to handle all of the processing of the program.
# All non-visible things occur here, such as file conversion,
# generating graphs and finding important values.
# Any info here gets sent to controller.py which
# also gets loaded into view.py.
from tkinter import filedialog as fd # Necessary for selecting a file
from tkinter.messagebox import showinfo
from pydub import AudioSegment # Used for reading the file
from scipy.io import wavfile # Reads the .wav file and collects useful info from it

# Graphing stuff
import numpy as np
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self.file = None
        self.dst = "output.wav"  # Output file name.
        self.sound = None # What sound is currently loaded. (Planned to be output.wav.)
        self.soundsec = None # How long the audio file lasts for
        self.wave_fig, self.wave_ax = plt.subplots(figsize=(4,2)) # Plot for the waveform

    def file_selection(self):
        # Four options are listed below.
        filetypes = (
            ('.wav files', '*.wav'),
            ('.mp3 files', '*.mp3'),
            ('.aac files', '*.aac'),
            ('All files', '*.*')
        )
        filetuple = ['.wav', '.mp3', '.aac']  # Tuple of supported file types.

        # File explorer prompt.
        self.file = fd.askopenfilename(
            title='Choose a file...',
            initialdir='/',
            filetypes=filetypes)

        # A check is ran to see if the file type is valid.
        if self.file[-4:] in filetuple:
            return True

            # Text on the bottom of the window is updated so that it reflects the selected file.
            # self.selfile_label['text'] = "Current file: " + selectedFile
        else:
            # Popup that tells the user the file type they chose is invalid.
            showinfo(
                title='Invalid file type',
                message=self.file[-4:] + " is not supported. Please use\n.wav, .mp3 or .aac."
            )

    # As the function explains this converts the file to a .wav file.
    # It also merges the sound channels into 1.
    # It also sets the sound second duration variable to equal the output file's!
    def convertToWav(self):
        # A check is ran to see if the file is a .mp3 or .aac.
        # Both of these run virtually the same, it just depends on what file it is.
        if self.file[-4:] == ".mp3":
            sound = AudioSegment.from_mp3(self.file) # Loads in audio
            sound = sound.set_channels(1) # Sets to one audio channel
            sound.export(self.dst, format="wav") # Exports as output.wav
        elif self.file[-4:] == ".aac":
            sound = AudioSegment.from_file(self.file, "aac") # Loads in audio
            sound = sound.set_channels(1) # Sets to one audio channel
            sound.export(self.dst, format="wav") # Exports as output.wav

        # Once the conversion process is done, the sound is loaded into memory!
        self.sound = AudioSegment.from_file(self.dst, format="wav")
        self.soundsec = self.sound.duration_seconds

    # Clears any metadata attached to the file.
    # Does not need to be ran unless the file is .wav.
    def removeMeta(self):
        # Sound is loaded, channels set to 1, then re-exported.
        sound = AudioSegment.from_file(self.file, format="wav")
        sound = sound.set_channels(1)
        sound.export(self.dst, format="wav")
        # Like convertToWav(), this also loads the sound into memory
        # and also stores how long the audio lasts into soundsec.
        self.sound = AudioSegment.from_file(self.dst, format="wav")
        self.soundsec = self.sound.duration_seconds

    # Generates a plot of the waveform. As simple as is!
    def waveformPlot(self):
        # .wav file is read into samplerate and data
        samplerate, data = wavfile.read(self.dst)
        # time linspace made from how long the file lasts
        time = np.linspace(0, self.sound.duration_seconds, data.shape[0])
        # Plot is stored in wave_ax, used to load into view.py
        self.wave_ax.plot(time, data)
        self.wave_ax.set_xlabel("Time [s]")
        self.wave_ax.set_ylabel("Amplitude")
