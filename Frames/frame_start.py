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
        load_Log_button = Button(
            self, text="Load XES", command=lambda: controller.import_xes_Log(str(entry.get()))
        )
        load_module_button = Button(
            self, text="Load Module", command=lambda: controller.importModule()
        )
        load_Log_button.pack()
        load_module_button.pack()
