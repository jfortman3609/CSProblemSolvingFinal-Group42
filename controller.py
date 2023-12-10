# This file is purely meant to send commands to and from files.
# It's a lot to wrap one's head around if they aren't experienced with it!
# (I can certainly say that for myself...)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # file() is a command that is ran from view.py.
    # This:
    # - Prompts the user to select a file (otherwise it does nothing)
    # - Converts the selected file to a .wav
    # - Updates visuals in view.py to reflect the current file loaded
    def file(self):
        # This function only runs if model.file_selection() returns true.
        # (This means that the user has selected a valid file.)
        if self.model.file_selection() == True:
            self.view.selfile_label['text'] = "Current file: " + self.model.file
            # A check is done to see if the selected file is either a .mp3 or a .aac.
            # If it's a .wav instead it skips to removing metadata.
            if self.model.file[-4:] in ['.mp3', '.aac']:
                self.model.convertToWav()
            else:
                self.model.removeMeta()
            # The sound length gets displayed visually here.
            self.view.sound_length['text'] = ("File length (in seconds): "
                                               + str(round(self.model.soundsec, 3)))
            self.model.waveformPlot()
            self.view.waveform()
            # The sound's resonance gets displayed here.
            self.model.resonance()
            self.view.highest_res['text'] = ("Highest resonance (in Hz): "
                                               + str(int(self.model.highest_res)))
