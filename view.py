import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd # Necessary for selecting a file
from tkinter.messagebox import showinfo


class View(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Audio button is set up here.
        self.audio_button = tk.Button(
            self,
            text="Choose file...",
            command=self.file_selection
        )
        self.audio_button.pack(side="top")

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
        filename = fd.askopenfilename(
            title='Choose a file...',
            initialdir='/',
            filetypes=filetypes)

        # A check is ran to see if the file type is valid.
        if filename[-4:] in filetuple:
            # This stores the file's name and location into a variable.
            selectedFile = filename

            # Text on the bottom of the window is updated so that it reflects the selected file.
            selfile_label = ttk.Label(self, text=selectedFile)
            selfile_label.pack(side="bottom")
        else:
            # Popup that tells the user the file type they chose is invalid.
            showinfo(
                title='Invalid file type',
                message=filename[-4:] + " is not supported. Please use\n.wav, .mp3 or .aac."
            )