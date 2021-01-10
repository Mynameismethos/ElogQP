import tkinter as tk
from tkinter import Button, IntVar, Label, Message, Scrollbar, StringVar

#TODO change Class Name MUST start with frame


class frame_mod_button(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.modController = None
        self.box_nav = tk.Frame(master=self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command=lambda: [
               self.leaveModule()]).pack(side="left", fill="both")
        self.prev_button = Button(self.box_nav, text="Previous Page")
        self.next_Button = Button(self.box_nav, text="Next Page")
        #### Add The Layout of the Frame here ###############
        self.title_text = StringVar()
        self.button_text = StringVar()
        self.button_command = IntVar()
        Label(self, textvariable=self.title_text).pack(fill="x", side="top")
        self.button1 = Button(self, textvariable=self.button_text, command=lambda: [
                              self.modController.callBack(self.button_command)])
        self.button1.pack()

        #Example
       # self.title_text = StringVar()
       # self.intro_text = StringVar()
       # self.desc_text = StringVar()
       # self.title_text.set("This is Mod1")
       # Label(self, textvariable=self.title_text).pack(fill="x",side="top")
       # #TODO better Width
       # Message(self, textvariable=self.intro_text,width=400).pack(fill="x",side="top")
       # Message(self, textvariable=self.desc_text,width=400).pack(fill="x",side="top")

    def showMe(self):
        pass

        #TODO fill  in, find Data that needs to be added by the module

    def update_Data(self, modController=None, next=None, previous=None, title="", button_text="", button_command=None):
        if modController:
            self.set_Controller(modController)
        if next:
            self.set_Next_Frame(next)
        if previous:
            self.set_Prev_Frame()
        if title:
            self.title_text.set(title)
        if button_text:
            self.button_text.set(button_text)
        if button_command:
            self.button_command.set(button_command)
        print("Hello")

    def set_Widgets_Visible(self, button1=None, buttonNext=None, buttonPrev=None):
        if(button1 == "yes"):
            self.button1.pack()
        elif(button1 == "no"):
            self.button1.pack_forget()

        if(buttonPrev == "yes"):
            self.prev_button.pack()
        elif(buttonPrev == "no"):
            self.prev_button.pack_forget()

        if(buttonNext == "yes"):
            self.next_Button.pack()
        elif(buttonNext == "no"):
            self.next_Button.pack_forget()

        # No Need to Change
    def set_Prev_Frame(self):
        if self.controller.hasPrevFrame():
            prev_button = Button(
                self.box_nav, text="Previous Page", command=lambda: [self.controller.showPrevFrame(), prev_button.destroy()])
            prev_button.pack(side="left", fill="both")
        # No Need to Change

    def set_Next_Frame(self, nextFrame):
        next_Button = Button(
            self.box_nav, text="Next Page", command=lambda: [self.controller.showFrame(nextFrame)])
        next_Button.pack(side="right", fill="both")

    def set_Controller(self, modController):
        self.modController = modController

    def leaveModule(self):
        self.modController.leaveMod()
