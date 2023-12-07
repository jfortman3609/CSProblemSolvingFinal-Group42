import tkinter as tk
from view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root window information
        self.title('Replace me later')
        self.resizable(False, False)
        self.geometry('300x150')

        view = View(self)
        view.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()