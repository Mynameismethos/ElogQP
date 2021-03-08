import tkinter as tk
from tkinter import Button, StringVar

class ModFrame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.modController = None
        self.title_text = StringVar()
        self.box_nav = tk.Frame(master=self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command=lambda: [
               self.leaveModule()]).pack(side="left", fill="both")
        self.prev_button = Button(self.box_nav, text="Previous Page")
        self.next_Button = Button(self.box_nav, text="Next Page")

    def update_Data(self, modController, next, previous, title):
        """"
        function to update Data represented in this module
        
        Keyword arguments:

        modController   --  Module that is in charge of Frame (default : None)
        next            -- if not None --> has next Frame (default: None)
        previous        -- if not None --> has previous Frame (default: None)
        title           -- String of the title (default: "")
        """
        if modController:
            self.modController=modController
        if next:
            self.set_Next_Frame()
        if previous:
            self.set_Prev_Frame()
        if title:
            self.title_text.set(title)


    def set_Prev_Frame(self):
        if self.controller.hasPrevFrame():
            prev_button = Button(
                self.box_nav, text="Previous Page", command=lambda: [self.controller.showModFrame(self.modController.__class__,prev=True)])
            prev_button.pack(side="left", fill="both")

    def set_Next_Frame(self):
        next_Button = Button(
            self.box_nav, text="Next Page", command=lambda: [self.controller.showModFrame(self.modController.__class__,next=True)])
        next_Button.pack(side="right", fill="both")

    def leaveModule(self):
        self.modController.leaveMod()