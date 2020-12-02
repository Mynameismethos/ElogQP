# import tkinter
from tkinter.constants import INSERT
import pm4py

from tkinter import Button, Entry, Label, Tk
import loadmodules

frame = Tk()

frame.geometry("300x300+100+100")
myText = Label(frame, text="Hello World")
entry = Entry(frame)
entry.pack()
entry.insert(INSERT, "Path to XES")


def display_hello():
    myText.pack()


def remove_hello():
    myText.pack_forget()


def import_xes_Log():
    log = pm4py.read_xes(entry.get())


def importModule():
    module_list = loadmodules.loadmodules()
    for module in module_list:
        print(
            "This Module is called: '"
            + module.getName()
            + "' it´s descibed as: "
            + module.getOneDesc()
        )
        module.exec("null")


hello_button = Button(frame, text="hello Button", command=display_hello)
hello_button.pack()
forget_button = Button(frame, text="Remove Button", command=remove_hello)
forget_button.pack()
load_Log_button = Button(frame, text="Load XES", command=import_xes_Log)
load_Log_button = Button(frame, text="Load Module", command=importModule)
load_Log_button.pack()

frame.mainloop()
