import tkinter as tk
from tkinter import Button, Label, Message, StringVar


class frame_mod_desc(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller
        #Title
        self.title_text = StringVar()
        self.intro_text = StringVar()
        self.desc_text = StringVar()
        self.title_text.set("This is Mod1")
        Label(self, textvariable=self.title_text).pack(fill="x",side="top")
        #TODO better Width
        Message(self, textvariable=self.intro_text,width=400).pack(fill="x",side="top")
        Message(self, textvariable=self.desc_text,width=400).pack(fill="x",side="top")

        self.box_nav = tk.Frame(master = self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command= lambda:[self.leaveModule()]).pack(side="left", fill="both")

            

    def update_Data(self,next,previous,title="",intro="", desc=""):
        self.set_Next_Frame(next)
        self.set_Prev_Frame(previous)
        
        if title: self.title_text.set(title)
        if intro: self.intro_text.set(intro)
        if desc:  self.desc_text.set(desc)
        print(self.title_text)
        

    def set_Prev_Frame(self, prevFrame):
        if prevFrame:
            prev_button = Button(
            self.box_nav, text="Previous Page", command=lambda: [self.controller.showFrame(prevFrame)])
            prev_button.pack(side="right",fill="both")

    def set_Next_Frame(self, nextFrame):
        next_Button = Button(
        self.box_nav, text="Next Page", command=lambda: [self.controller.showFrame(nextFrame)])
        next_Button.pack(side="right",fill="both")

    def leaveModule(self):
        #TODO SHOW WARNING
        #TODO implement delete Frames
         self.controller.showFrame("frame_modules")
