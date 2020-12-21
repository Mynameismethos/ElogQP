import tkinter as tk
from tkinter import Button, Label, Message, Scrollbar, StringVar

#TODO change Class Name MUST start with frame
class frame_mod_List(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller
        self.box_nav = tk.Frame(master = self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command= lambda:[self.leaveModule()]).pack(side="left", fill="both")
        #### Add The Layout of the Frame here ###############
        self.title_text = StringVar()
        Label(self, textvariable=self.title_text).pack(fill="x",side="top")
        self.listBox = tk.Listbox(self)
        self.listBox.pack(fill="both")

        #Example
       # self.title_text = StringVar()
       # self.intro_text = StringVar()
       # self.desc_text = StringVar()
       # self.title_text.set("This is Mod1")
       # Label(self, textvariable=self.title_text).pack(fill="x",side="top")
       # #TODO better Width
       # Message(self, textvariable=self.intro_text,width=400).pack(fill="x",side="top")
       # Message(self, textvariable=self.desc_text,width=400).pack(fill="x",side="top")



        

        #TODO fill in, find Data that needs to be added by the module
    def update_Data(self,next,previous,title="", list ={}):
        self.set_Next_Frame(next)
        self.set_Prev_Frame(previous)
        
        if title: self.title_text.set(title)

        for x in list:
            print(x)
            self.listBox.insert("end", x)
        
        print(self.title_text)
        

        # No Need to Change
    def set_Prev_Frame(self, prevFrame):
        if prevFrame:
            prev_button = Button(
            self.box_nav, text="Previous Page", command=lambda: [self.controller.showFrame(prevFrame)])
            prev_button.pack(side="right",fill="both")
        # No Need to Change
    def set_Next_Frame(self, nextFrame):
        next_Button = Button(
        self.box_nav, text="Next Page", command=lambda: [self.controller.showFrame(nextFrame)])
        next_Button.pack(side="right",fill="both")

    def leaveModule(self):
        #TODO SHOW WARNING
        #TODO implement delete Frames
         self.controller.showFrame("frame_modules")
