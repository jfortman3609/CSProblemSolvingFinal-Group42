from tkinter import filedialog as fd # Necessary for selecting a file
from tkinter.messagebox import showinfo
from pydub import AudioSegment

class Model:
    def __init__(self):
        self.file = None
        self.dst = "output.wav"  # Output file name.

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
    def convertToWav(self):
        # A check is ran to see if the file is a .mp3 or .aac.
        if self.file[-4:] == ".mp3":
            sound = AudioSegment.from_mp3(self.file)
            sound = sound.set_channels(1)
            sound.export(self.dst, format="wav")
        elif self.file[-4:] == ".aac":
            sound = AudioSegment.from_file(self.file, "aac")
            sound = sound.set_channels(1)
            sound.export(self.dst, format="wav")

    # Clears any metadata attached to the file.
    # Does not need to be ran unless the file is .wav.
    def removeMeta(self):
        sound = AudioSegment.from_file(self.file, format="wav")
        sound = sound.set_channels(1)
        sound.export(self.dst, format="wav")