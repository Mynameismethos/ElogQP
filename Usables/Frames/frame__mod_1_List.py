import tkinter as tk
from tkinter import Button, IntVar, Label, Listbox, Message, Scrollbar, StringVar

#TODO change Class Name MUST start with frame
class frame_mod_List(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller
        self.modController=None
        self.box_nav = tk.Frame(master = self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self.box_nav, text="Leave Module", command= lambda:[self.leaveModule()]).pack(side="left", fill="both")
        #### Add The Layout of the Frame here ###############
        self.title_text = StringVar()
        Label(self, textvariable=self.title_text).pack(fill="x",side="top")
        self.listBox = tk.Listbox(self)
        self.listBox.pack(fill="both", expand="yes")
        self.button1_text=StringVar()
        self.button2_text=StringVar()
        self.button1_command=IntVar()
        self.button2_command=IntVar()
        self.box_bellowList = tk.Frame(master = self)
        self.box_bellowList.pack(fill="x", expand="no")
        Button(self.box_bellowList, textvariable=self.button1_text, command=lambda:[self.modController.callBack(self.button1_command)]).grid(row=0, column=0, sticky="nsew")
        Button(self.box_bellowList, textvariable=self.button2_text, command=lambda:[self.modController.callBack(self.button2_command)]).grid(row=0, column=1, sticky="nsew")
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
    def update_Data(self,modController=None, next=None,previous=None,title="", list =[], button1_text="", button2_text="", button1_command=None,button2_command=None):
        if modController: self.set_Controller(modController)
        if next:     self.set_Next_Frame(next)
        if previous: self.set_Prev_Frame(previous)
        if title: self.title_text.set(title)
        if button1_text: self.button1_text.set(button1_text)
        if button1_command: self.button1_command.set(button1_command)
        if button2_text: self.button2_text.set(button2_text)
        if button2_command: self.button2_command.set(button2_command)
        
        if list: 
            self.listBox.delete(0,"end")
            for x in list:
                print(x)
                self.listBox.insert("end", x)
        
        print(self.title_text)

    def setMultiselect(self, multiselect):
        if multiselect:self.listBox["selectmode"] = "extended"
        else: self.listBox["selectmode"] = "single"
        

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
         self.modController.leaveMod()



    def set_Controller(self, modController):
        self.modController= modController

    def getSelected(self):
        return self.listBox.curselection()
    def setSelected(self, list):
        pass
