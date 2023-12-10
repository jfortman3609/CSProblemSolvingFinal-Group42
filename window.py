# All of the important files that the program needs to run with are imported.
# tkinter is also here. Say hi!
import tkinter as tk
from view import View
from model import Model
from controller import Controller


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root window information
        self.title('Replace me later')
        self.resizable(False, False)

        # A model is loaded here.
        model = Model()

        # Code from view.py is loaded here.
        # In order for the view to display, .pack() has to be used.
        view = View(self)
        view.grid()

        # Load a controller here
        controller = Controller(model, view)

        # Set the controller's view. The view and the controller communicate
        # directly with one another!
        view.set_controller(controller)


# Runs the program.
# Simple as that.
if __name__ == '__main__':
    app = App()
    app.mainloop()
