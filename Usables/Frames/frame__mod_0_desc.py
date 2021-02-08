from Usables.Frames.ModFrame import ModFrame
import tkinter as tk
from tkinter import Button, Label, Message, StringVar


class frame_mod_desc(ModFrame):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.intro_text = StringVar()
        self.desc_text = StringVar()
        self.title_text.set("This is Mod1")
        Label(self, textvariable=self.title_text).pack(fill="x", side="top")

        self.message1 = Message(self, textvariable=self.intro_text, width=400)
        self.message1.pack(fill="x", side="top")
        self.message2 = Message(self, textvariable=self.desc_text, width=400)
        self.message2.pack(fill="x", side="top")

    def showMe(self):
        pass

    def update_Data(self, modController=None, next=None, previous=None, title="", intro="", desc=""):
        super().update_Data(modController,next, previous, title)
        if intro:
            self.intro_text.set(intro)
        if desc:
            self.desc_text.set(desc)

    def set_Widgets_Visible(self, buttonNext=None, buttonPrev=None):

        if(buttonPrev == "yes"):
            self.prev_button.pack()
        elif(buttonPrev == "no"):
            self.prev_button.pack_forget()

        if(buttonNext == "yes"):
            self.next_Button.pack()
        elif(buttonNext == "no"):
            self.next_Button.pack_forget()