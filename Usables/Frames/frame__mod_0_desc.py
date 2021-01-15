import tkinter as tk
from tkinter import Button, Label, Message, StringVar


class frame_mod_desc(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.modController = None
        #Title
        self.title_text = StringVar()
        self.intro_text = StringVar()
        self.desc_text = StringVar()
        self.title_text.set("This is Mod1")
        Label(self, textvariable=self.title_text).pack(fill="x", side="top")
        self.box_nav = tk.Frame(master=self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command=lambda: [
               self.leaveModule()]).pack(side="left", fill="both")
        self.prev_button = Button(self.box_nav, text="Previous Page")
        self.next_Button = Button(self.box_nav, text="Next Page")

        self.message1 = Message(self, textvariable=self.intro_text, width=400)
        self.message1.pack(fill="x", side="top")
        self.message2 = Message(self, textvariable=self.desc_text, width=400)
        self.message2.pack(fill="x", side="top")

    def showMe(self):
        pass

    def update_Data(self, modController=None, next=None, previous=None, title="", intro="", desc=""):
        if modController:
            self.set_Controller(modController)
        if next:
            self.set_Next_Frame(next)
        if previous:
            self.set_Prev_Frame()

        if title:
            self.title_text.set(title)
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

    def set_Prev_Frame(self):
        if self.controller.hasPrevFrame():
            prev_button = Button(
                self.box_nav, text="Previous Page", command=lambda: [self.controller.showModFrame(prev=True)])
            prev_button.pack(side="left", fill="both")

    def set_Next_Frame(self, nextFrame):
        self.next_Button.configure(
            command=lambda: [self.controller.showModFrame(next=True)])
        self.next_Button.pack(side="right", fill="both")

    def set_Controller(self, modController):
        self.modController = modController

    def leaveModule(self):
        self.modController.leaveMod()
