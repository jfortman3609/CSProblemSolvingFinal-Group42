# The goal of this script is to handle all of the processing of the program.
# All non-visible things occur here, such as file conversion,
# generating graphs and finding important values.
# Any info here gets sent to controller.py which
# also gets loaded into view.py.
from tkinter import filedialog as fd # Necessary for selecting a file
from tkinter.messagebox import showinfo
from pydub import AudioSegment # Used for reading the file
from scipy.io import wavfile # Reads the .wav file and collects useful info from it
from scipy.signal import welch # Used to find resonance

# Graphing stuff
import numpy as np
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        # Basic stuff
        self.file = None # What file is currently selected
        self.dst = "output.wav"  # Output file name

        # .wav file info
        self.sound = None # What sound is currently loaded (Planned to be output.wav.)
        self.soundsec = None # How long the audio file lasts for
        self.wave_fig, self.wave_ax = plt.subplots(figsize=(4, 2)) # Plot for the waveform

        # The specifics of the file
        self.highest_res = None # Highest resonance of the file
        self.rt20 = None
        self.rt60 = None # Reverb time
        self.maxdb = None # Highest decibel (dB)
        self.maxindex = None
        self.lowerdb = None # Highest decibel - 5
        self.lowerindex = None
        self.lowestdb = None # Lowest db
        self.lowestindex = None
        self.freq_fig, self.freq_ax = plt.subplots(figsize=(4, 2))  # Plot for the frequency
        self.spec_fig, self.spec_ax = plt.subplots(figsize=(4, 2))  # Plot for the specgram

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
        self.wave_ax.clear() # Used to clear out any previous graph stored
        # .wav file is read into samplerate and data
        samplerate, data = wavfile.read(self.dst)
        # time linspace made from how long the file lasts
        time = np.linspace(0, self.sound.duration_seconds, data.shape[0])
        # Plot is stored in wave_ax, used to load into view.py
        self.wave_ax.plot(time, data)
        self.wave_ax.set(xlabel="Time [s]", ylabel="Amplitude")

    def resonance(self):
        # .wav file is read into samplerate and data
        samplerate, data = wavfile.read(self.dst)
        frequencies, power = welch(data, samplerate, nperseg=4096)
        self.highest_res = frequencies[np.argmax(power)]

    # Used for selecting a frequency under 1kHz.
    def find_target_freq(self, freqs):
        x = 0
        for x in freqs:
            if x > 1000:
                break
        return x

    # Used for checking a frequency.
    def freq_check(self):
        samplerate, data = wavfile.read(self.dst)
        spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, NFFT=1024)

        # The target frequency is found using the function that was created beforehand.
        target_freq = self.find_target_freq(freqs)
        # The index is found...
        index_of_freq = np.where(freqs == target_freq)[0][0]
        # The index is plugged into the spectrum...
        data_for_freq = spectrum[index_of_freq]
        # Since it's in a logarithm it'll need to be accounted for.
        data_in_db_funct = 10 * np.log10(data_for_freq)
        return data_in_db_funct

    # Used to find the index of the max dB. How handy!
    def highest_db(self):
        data_in_db = self.freq_check()
        self.maxindex = np.argmax(data_in_db)
        self.maxdb = data_in_db[self.maxindex]
        self.lowerdb = self.maxdb - 5

    # Finding the nearest value of less than 5 db.
    def find_near_value(self, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    # Finding the true lower db
    def true_lowerdb(self):
        data_in_db = self.freq_check()
        sliced_array = data_in_db[self.maxindex:]
        self.lowerdb = self.find_near_value(sliced_array, self.lowerdb)
        self.lowerindex = np.where(data_in_db == self.lowerdb)

    # Another one, minus -25
    def lowest_db(self):
        data_in_db = self.freq_check()
        sliced_array = data_in_db[self.maxindex:]
        self.lowestdb = self.maxdb - 25
        self.lowestdb = self.find_near_value(sliced_array, self.lowestdb)

    # RT values
    def reverbtime(self):
        samplerate, data = wavfile.read(self.dst)
        spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, NFFT=1024)

        self.rt20 = (t[self.lowerindex] - t[self.lowestindex])[0]
        self.rt60 = 3 * self.rt20

    # A bunch of plotting
    def plot_freqs(self, mode):
        samplerate, data = wavfile.read(self.dst)
        spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, NFFT=1024)
        self.freq_ax.clear() # Used to clear out any previous graph stored
        # Used for obtaining the data in decibels
        data_in_db = self.freq_check()
        # Plot is stored in freq_ax, used to load into view.py
        if mode == 1:
            self.freq_ax.plot(t[self.maxindex], data_in_db[self.maxindex])
        elif mode == 2:
            self.freq_ax.plot(t[self.lowerindex], data_in_db[self.lowerindex])
        elif mode == 3:
            self.freq_ax.plot(t[self.lowestindex], data_in_db[self.lowestindex])
        elif mode == 4:
            self.freq_ax.plot(t[self.maxindex], data_in_db[self.maxindex])
            self.freq_ax.plot(t[self.lowerindex], data_in_db[self.lowerindex])
            self.freq_ax.plot(t[self.lowestindex], data_in_db[self.lowestindex])

