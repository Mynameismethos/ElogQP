import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, Tk
from tkinter.constants import INSERT
from typing import Text
__className__ = "frame_mod_V1"
#TODO change Class Name
class frame_mod_V1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller
        #Title
        self.title= Label(self, text="This is Mod1").pack()
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

    def update_Data(self,title_text="This is Mod1"):
        #TODO impl
        self.title.configue(Text=title_text)


    def leaveModule(self):
        #TODO SHOW WARNING
         self.controller.showFrame("frame_modules")
