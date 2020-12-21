import tkinter as tk
from tkinter import Button, Entry, Frame, Label
from tkinter.constants import BOTTOM, INSERT, X


class frame_start(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        Label(self, text="Tool zum Finden und Beheben von Fehlern in Eventlog", bg ="light blue").pack(fill="x")
        Label(self, text="Bitte geben Sie den Namen der Logdatei an und Laden sie den Log", bg ="light blue").pack(fill="x")
        entry = Entry(self)
        entry.insert(INSERT, "LOGEDV.xes")
        entry.pack()
        load_Log_button = Button(
            self, text="Load XES", command=lambda: [load_Log_button.configure(bg = "orange") ,controller.import_xes_Log(__class__.__name__, load_Log_button, str(entry.get()))]
        )
        load_Log_button.pack()
        load_module_button = Button(
            self, text="Load Module", command=lambda: [load_module_button.configure(bg = "orange"), controller.importModule(__class__.__name__,load_module_button)]
        )
        
        load_module_button.pack()

        box_nav = tk.Frame(master = self)
        box_nav.pack(side="bottom", fill="x")
        next_button = Button(
            box_nav, text="Next Page", command=lambda: [self.goToNext(controller)]
        )
        next_button.pack(side="right", fill="both")

    def button_feedback(Frame,button, successfull):
        if successfull: button.configure(bg = "green")
        else : button.configure(bg = "red")
    
    def goToNext(self,controller):
        if(len(controller.getModules())> 0 and not ( not controller.getLog())):
            controller.showFrame("frame_modules",__class__.__name__)
        #else set Buttoncolor to red


    def set_prev_Frame(self, prevFrame):
        prev_frame=prevFrame
        if prev_frame:
            prev_button = Button(
            super.box_nav, text="Previous Page", command=lambda: [self.controller.showFrame(prevFrame), prev_button.destroy()])
            prev_button.pack(side="left",fill="both")
