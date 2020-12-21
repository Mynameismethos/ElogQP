import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, Tk
from tkinter.constants import INSERT

#TODO change Class Name
class frame_example(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller= controller
        #Title
        title= Label(self, text="Hello World from Modules")
        title.pack()
        self.box_nav = tk.Frame(master = self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Continue",command=lambda:[self.goToNext()]).pack(side="right", fill="both")

        

    def set_prev_Frame(self, prevFrame):
        prev_frame=prevFrame
        if prev_frame:
            prev_button = Button(
            self.box_nav, text="Previous Page", command=lambda: [self.controller.showFrame(prevFrame), prev_button.destroy()])
            prev_button.pack(side="left",fill="both")

    def goToNext(self):
        #TODO impl
        pass

    def update_Data():
        #TODO impl
        pass

    def leaveModule(self):
        #TODO SHOW WARNING
         self.controller.showFrame("frame_modules")
    