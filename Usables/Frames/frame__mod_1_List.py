from Usables.Frames.ModFrame import ModFrame
import tkinter as tk
from tkinter import Button, IntVar, Label, StringVar

#TODO Comment Module
class frame_mod_List(ModFrame):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)

        #### Add The Layout of the Frame here ###############

        Label(self, textvariable=self.title_text).pack(fill="x", side="top")
        self.listBox = tk.Listbox(self)
        self.listBox.pack(fill="both", expand="yes")
        self.button1_text = StringVar()
        self.button2_text = StringVar()
        self.button1_command = IntVar()
        self.button2_command = IntVar()
        self.box_bellowList = tk.Frame(master=self)
        self.box_bellowList.pack(fill="x", expand="no")
        self.box_bellowList.columnconfigure(0, weight=1)
        self.box_bellowList.columnconfigure(1, weight=1)
        self.button1 = Button(self.box_bellowList, textvariable=self.button1_text, command=lambda: [
                              self.modController.callBack(self.button1_command)])
        self.button2 = Button(self.box_bellowList, textvariable=self.button2_text, command=lambda: [
                              self.modController.callBack(self.button2_command)])
        self.button1.grid(row=0, column=0, sticky="nsew")
        self.button2.grid(row=0, column=1, sticky="nsew")

    #TODO Comment Function
    def showMe(self):
        pass


    def update_Data(self, modController=None, next=None, previous=None, title="", list=[], button1_text="", button2_text="", button1_command=None, button2_command=None, selected=[]):
        """  
        function to update Data represented in this module
        
        Keyword arguments:

        modController   --  Module that is in charge of Frame (default : None)
        next            -- if not None --> has next Frame (default: None)
        previous        -- if not None --> has previous Frame (default: None)
        title           -- String of the title (default: "")
        list            -- a list of elements to be displayed (default :[])
        button1_text    -- String shown on button1 (default: "")
        button1_command -- int flag for callback of button1 (default: None)
        button2_text    -- String shown on button2 (default: "")
        button2_command -- int flag for callback of button2 (default: None)
        selected        -- list of highlighted elements (default: [])
        """
        super().update_Data(modController,next, previous, title)
        if button1_text:
            self.button1_text.set(button1_text)
        if button1_command:
            self.button1_command.set(button1_command)
        if button2_text:
            self.button2_text.set(button2_text)
        if button2_command:
            self.button2_command.set(button2_command)

        if list:
            self.listBox.delete(0, "end")
            for x in list:
                print(x)
                self.listBox.insert("end", x)

        if selected:
            self.listBox.selection_set(selected)

    #TODO Comment Function
    def setMultiselect(self, multiselect):
        #TODO comment
        if multiselect:
            self.listBox["selectmode"] = "extended"
        else:
            self.listBox["selectmode"] = "single"

        # No Need to Change

    def set_Widgets_Visible(self, button1=None, button2=None, buttonNext=None, buttonPrev=None):
        #TODO comment
        if(button1 == "yes"):
            self.button1.grid()
        elif(button1 == "no"):
            self.button1.grid_remove()

        if(button2 == "yes"):
            self.button2.grid()
        elif(button2 == "no"):
            self.button2.grid_remove()

        if(buttonPrev == "yes"):
            self.prev_button.pack()
        elif(buttonPrev == "no"):
            self.prev_button.pack_forget()

        if(buttonNext == "yes"):
            self.next_Button.pack()
        elif(buttonNext == "no"):
            self.next_Button.pack_forget()

    def getSelected(self):
        return self.listBox.curselection()

    def setSelected(self, list):
        pass
