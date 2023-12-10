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
        self.audio_button.grid(row=0)

        # The file's directory gets set at the bottom.
        # This is updated with the use of file_selection().
        self.selfile_label = ttk.Label(self, text="Select a file.")
        self.selfile_label.grid(row=1)

        # The graph of the currently loaded waveform will be displayed here.


        # How long the audio file is (in seconds).
        # By default, this will be blank; it'll only appear once everything is loaded.
        self.sound_length = ttk.Label(self, text="")
        self.sound_length.grid(row=3)

        # A controller will be set here.
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def file_selection(self):
        self.controller.file()