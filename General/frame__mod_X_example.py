import tkinter as tk
from tkinter import Button, Label, Message, StringVar

#Impl TODO change Class Name MUST start with frame


class frame_mod_example(tk.Frame):
    """
    Example Frame for Modules

    This Frame can be used as a template for developing frames

    """
    def __init__(self, parent, controller):
        """
        Function to create the Layout of the Frame

        some examples are given
        #Impl TODO indicates areas that need to be adjusted for a new Modul

        """
        super().__init__(parent)
        self.controller = controller
        self.box_nav = tk.Frame(master=self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command=lambda: [
               self.leaveModule()]).pack(side="left", fill="both")
        #### Add The Layout of the Frame here ###############
        #Example
       # self.title_text = StringVar()
       # self.intro_text = StringVar()
       # self.desc_text = StringVar()
       # self.title_text.set("This is Mod1")
       # Label(self, textvariable=self.title_text).pack(fill="x",side="top")

       # Message(self, textvariable=self.intro_text,width=400).pack(fill="x",side="top")
       # Message(self, textvariable=self.desc_text,width=400).pack(fill="x",side="top")

    def showMe():
        """ function that is called right after the frame is shown"""
        pass

    #Impl TODO fill in, find Data that needs to be added by the module
    def update_Data(self, modController=None, next=None, previous=None, title="", intro="", desc=""):
        """ function to recive Data that is to be shown on the Frame """
        if modController:
            self.set_Controller(modController)
        if next:
            self.set_Next_Frame(next)
        if previous:
            self.set_Prev_Frame(previous)

        if title:
            self.title_text.set(title)
        if intro:
            self.intro_text.set(intro)
        if desc:
            self.desc_text.set(desc)
        print(self.title_text)

 ############## No Need to Change these Functions ######################

    def set_Prev_Frame(self, prevFrame):
        """ function to check if a previous Frame exists and adjust the button accordingly """
        if prevFrame:
            prev_button = Button(
                self.box_nav, text="Previous Page", command=lambda: [self.controller.showFrame(prevFrame)])
            prev_button.pack(side="right", fill="both")
        

    def set_Next_Frame(self, nextFrame):
        """ function to check if a following Frame exists and adjust the button accordingly """
        next_Button = Button(
            self.box_nav, text="Next Page", command=lambda: [self.controller.showFrame(nextFrame)])
        next_Button.pack(side="right", fill="both")

    def set_Controller(self, modController):
        """ function set the executing Modul as a controller """
        self.modController = modController

    def leaveModule(self):
        """ function to exit out of the Module """
        self.modController.leaveMod()
