# All the visuals are managed here!
# (Well, most of it. controller.py manages a thing or two.)
# The controller.py and view.py files communicate with one another.
# Any command that gets activated here executes things in controller.py.
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
# from tkinter import filedialog as fd # Necessary for selecting a file
# from tkinter.messagebox import showinfo


class View(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # A frame is created to show the user the current file's info.
        self.file_info = tk.Frame(root)
        self.file_info.grid(row=0)

        # Audio button is set up here.
        self.audio_button = tk.Button(
            self.file_info,
            text="Choose file...",
            command=self.file_selection
        )
        self.audio_button.grid(row=0)

        # The file's directory gets set at the bottom.
        # This is updated with the use of file_selection().
        self.selfile_label = ttk.Label(self.file_info, text="Select a file.")
        self.selfile_label.grid(row=1)

        # The graph of the currently loaded waveform will be displayed here.
        self.waveform_frame = tk.Frame(root)
        self.waveform_frame.grid(row=1)

        # Another frame is created here to show statistics of the loaded waveform.
        self.stats_frame = tk.Frame(root)
        self.stats_frame.grid(row=2)

        # How long the audio file is (in seconds).
        # By default, this will be blank; it'll only appear once everything is loaded.
        self.sound_length = ttk.Label(self.stats_frame, text="")
        self.sound_length.grid(row=0)
        # In extension to this, resonance is also displayed here.
        self.highest_res = ttk.Label(self.stats_frame, text="")
        self.highest_res.grid(row=1)

        # Frequencies are down here!
        # Frame for displaying the frequency plot.
        self.freq_frame = tk.Frame(root)
        self.freq_frame.grid(row=3)
        # Another frame for controlling the frequency plot.
        self.freq_control_frame = tk.Frame(root)
        self.freq_control_frame.grid(row=4)
        # Buttons are here for controlling it.
        # By default, these are disabled until a file is loaded.
        self.freq_switch_button = tk.Button(
            self.freq_control_frame,
            text="Display Next Frequency",
            command=self.file_selection,
            state="disabled"
        )
        self.freq_switch_button.grid(row=0)
        self.all_freq_button = tk.Button(
            self.freq_control_frame,
            text="Display All Frequencies",
            command=self.file_selection,
            state="disabled"
        )
        self.all_freq_button.grid(row=1)

        # A controller will be set here.
        self.controller = None

    # The controller gets set here. (For use in window.py.)
    def set_controller(self, controller):
        self.controller = controller

    # For use with audio_button.
    # When the audio button is clicked, this function gets ran and causes a sequence
    # of events in controller.py.
    def file_selection(self):
        self.controller.file()

    # Used to display the waveform's plot.
    def waveform(self):
        # A canvas is used to display the graph.
        # Pulls from model.py's wave_fig variable and it sets the waveform_frame as its master.
        canvas1 = FigureCanvasTkAgg(self.controller.model.wave_fig, self.waveform_frame)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=2)
