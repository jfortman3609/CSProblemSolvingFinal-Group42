import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd # Necessary for selecting a file
from tkinter.messagebox import showinfo

def file_selection():
    # Four options are listed below.
    filetypes = (
        ('.wav files', '*.wav'),
        ('.mp3 files', '*.mp3'),
        ('.aac files', '*.aac'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Choose a file...',
        initialdir='/',
        filetypes=filetypes)

    # This seems to store the file's name and directory as a string into the variable.
    # gfile = filename

    # This opens up a prompt based on what file was selected.
    # Should probably be scrapped for later.
    showinfo(
        title='Selected File',
        message=filename
    )

root = tk.Tk()
root.title('Replace me later')

audio_button = tk.Button(
    root,
    text="Choose file...",
    command=file_selection
)
audio_button.pack()

root.mainloop()
