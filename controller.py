class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def file(self):
        if self.model.file_selection() == True:
            self.view.selfile_label['text'] = "Current file: " + self.model.file
            if self.model.file[-4:] in ['.mp3', '.aac']:
                self.model.convertToWav()
            else:
                self.model.removeMeta()
            self.view.sound_length['text'] = ("File length (in seconds): "
                                               + str(round(self.model.soundsec, 3)))
