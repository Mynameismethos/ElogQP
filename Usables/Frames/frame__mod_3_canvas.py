from Usables.Frames.ModFrame import ModFrame
import tkinter as tk
from tkinter import Button, Entry, Label, StringVar, IntVar
from tkinter.constants import ANCHOR, INSERT, NO, NONE


#TODO change Class Name MUST start with frame
class frame_mod_canvas(ModFrame):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
    
        self.settingsCanvas = tk.Frame(self)
        self.settingsCanvas.pack(fill="both", expand="yes")

        self.box_bellowList = tk.Frame(master=self)
        self.box_bellowList.pack(fill="x", expand="no")
        self.box_bellowList.columnconfigure(0, weight=1)
        self.box_bellowList.columnconfigure(1, weight=1)
        self.button1_text = StringVar()
        self.button1_command = IntVar()
        self.button2_text = StringVar()
        self.button2_command = IntVar()
        self.button3_text = StringVar()
        self.button3_command = IntVar()
        self.button1 = Button(self.box_bellowList, textvariable=self.button1_text, command=lambda: [
                              self.modController.callBack(self.button1_command)])
        self.button2 = Button(self.box_bellowList, textvariable=self.button2_text, command=lambda: [
                              self.modController.callBack(self.button2_command)])
        self.button3 = Button(self.box_bellowList, textvariable=self.button3_text, command=lambda: [
                              self.modController.callBack(self.button3_command)])
        self.button1.grid(row=0, column=0, sticky="nsew")
        self.button2.grid(row=0, column=1, sticky="nsew")
        self.button3.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.set_Widgets_Visible(button1="no", button2="no", button3="no")

    def showMe(self):
        pass

    #TODO fill in, find Data that needs to be added by the module

    def update_Data(self, modController=None, next=None, previous=None, title="", intro="", desc="", canDict={}, canList=[], highlight=[],
                    button1_text="", button1_command=None, button2_text="", button2_command=None, button3_text="", button3_command=None):
                        """  
        function to update Data represented in this module
        
        Keyword arguments:

        modController   --  Module that is in charge of Frame (default : None)
        next            -- if not None --> has next Frame (default: None)
        previous        -- if not None --> has previous Frame (default: None)
        title           -- String of the title (default: "")
        desc            -- String of describtion (default: "")
        canDict         -- Dictionary to be displayed on canvas (default: {})
        canList         -- List  to be displayed on canvas (default:[])
        highlight       -- List of elements to be highlighted (default: [])
        button1_text    -- String shown on Button1 (default: "")
        button1_command -- int flag for callback of Button1 (default: None)
        button2_text    -- String shown on Button2 (default: "")
        button2_command -- int flag for callback of Button2 (default: None)
        button3_text    -- String shown on Button3 (default: "")
        button3_command -- int flag for callback of Button3 (default: None)
        """
        super().update_Data(modController,next, previous, title)
        if intro:
            self.intro_text.set(intro)
        if desc:
            self.desc_text.set(desc)
        if button1_text:
            self.button1_text.set(button1_text)
            self.set_Widgets_Visible(button1="yes")
        if button1_command:
            self.button1_command.set(button1_command)

        if button2_text:
            self.button2_text.set(button2_text)
            self.set_Widgets_Visible(button2="yes")
        if button2_command:
            self.button2_command.set(button2_command)

        if button3_text:
            self.button3_text.set(button3_text)
            self.set_Widgets_Visible(button3="yes")
        if button3_command:
            self.button3_command.set(button3_command)
        if canDict:
            for widget in self.settingsCanvas.winfo_children():
                widget.destroy()

            for key, value in canDict.items():
                frame = tk.Frame(self.settingsCanvas)
                frame.pack(fill="none", expand="yes", side="top")
                l = Label(frame, text=key, anchor="center")
                l.grid(row=0, column=0)
                e = Entry(frame)
                e.insert(INSERT, value)
                e.grid(row=0, column=1)

        if canList:
            for widget in self.settingsCanvas.winfo_children():
                widget.destroy()

            for step in canList:
                frame = tk.Frame(self.settingsCanvas)
                frame.pack(fill="y", expand="yes", side="top")
                frame.columnconfigure(0, weight=1)
                frame.columnconfigure(1, weight=1)
                nameAc = step["concept:name"]
                timeAc = step["time:timestamp"]
                l = Label(frame, text=nameAc, anchor="center")
                l.grid(row=0, column=0, sticky="nsew")
                e = Entry(frame)
                e.insert(INSERT, timeAc)
                e.grid(row=0, column=1, sticky="nsew")

    def set_Widgets_Visible(self, button1=None, button2=None, button3=None, buttonNext=None, buttonPrev=None):

        if(button1 == "yes"):
            self.button1.grid()
        elif(button1 == "no"):
            self.button1.grid_remove()

        if(button2 == "yes"):
            self.button2.grid()
        elif(button2 == "no"):
            self.button2.grid_remove()

        if(button3 == "yes"):
            self.button3.grid()
        elif(button3 == "no"):
            self.button3.grid_remove()

        if(buttonPrev == "yes"):
            self.prev_button.pack()
        elif(buttonPrev == "no"):
            self.prev_button.pack_forget()

        if(buttonNext == "yes"):
            self.next_Button.pack()
        elif(buttonNext == "no"):
            self.next_Button.pack_forget()

    def getCanvasAsDict(self):
        returndict = {}
        for frame in self.settingsCanvas.winfo_children():
            key = NONE
            value = NONE
            for child in frame.winfo_children():
                if isinstance(child, Entry):
                    value = child.get()
                if isinstance(child, Label):
                    key = child.cget("text")
            returndict[key] = value
        return returndict

    def getCanvasAsList(self):
        returnList = []
        for frame in self.settingsCanvas.winfo_children():

            for child in frame.winfo_children():
                if isinstance(child, Entry):
                    returnList.append(child.get())

        return returnList
