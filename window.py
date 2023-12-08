import tkinter as tk
from view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root window information
        self.title('Replace me later')
        self.resizable(False, False)
        self.geometry('400x150')

        # A model would be loaded here.
        # IF WE HAD ONE. (its a reference)

        # Code from view.py is loaded here.
        # In order for the view to display, .pack() has to be used.
        view = View(self)
        view.pack()

        # Load a controller here

        # Set the controller's view, don't completely understand this yet


# Runs the program.
# Simple as that.
if __name__ == '__main__':
    app = App()
    app.mainloop()
