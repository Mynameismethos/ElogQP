import tkinter as tk
from tkinter import Button, Entry, Label, Tk
from tkinter.constants import INSERT


class frame_start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        entry = Entry(self)
        myText = Label(self, text="Hello World")
        entry.pack()
        entry.insert(INSERT, "Path to XES")
        hello_button = Button(
            self, text="hello Button", command=lambda: display_hello(self)
        )
        hello_button.pack()
        forget_button = Button(
            self, text="Remove Button", command=lambda: remove_hello(self)
        )
        forget_button.pack()
        load_Log_button = Button(
            self, text="Load XES", command=lambda: import_xes_Log(self)
        )
        load_Log_button = Button(
            self, text="Load Module", command=lambda: importModule(self)
        )

        load_Log_button.pack()
