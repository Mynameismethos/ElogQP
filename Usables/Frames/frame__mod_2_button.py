from Usables.Frames.ModFrame import ModFrame
from tkinter import Button, IntVar, Label, StringVar

#TODO Comment Module
class frame_mod_button(ModFrame):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        #### Add The Layout of the Frame here ###############
        self.button1_text = StringVar()
        self.button1_command = IntVar()
        self.button2_text = StringVar()
        self.button2_command = IntVar()

        Label(self, textvariable=self.title_text).pack(fill="x", side="top")
        self.button1 = Button(self, textvariable=self.button1_text, command=lambda: [
                              self.modController.callBack(self.button1_command)])
        self.button2 = Button(self, textvariable=self.button2_text, command=lambda: [
                              self.modController.callBack(self.button2_command)])
        self.button1.pack()
        self.button2.pack()
        
    def showMe(self):
        pass



    def update_Data(self, modController=None, next=None, previous=None, title="", button1_text="", button1_command=None,  button2_text="", button2_command=None):
        """  
        function to update Data represented in this module
        
        Keyword arguments:

        modController   --  Module that is in charge of Frame (default : None)
        next            -- if not None --> has next Frame (default: None)
        previous        -- if not None --> has previous Frame (default: None)
        title           -- String of the title (default: "")
        button1_text    -- String shown on Button1 (default: "")
        button1_command -- int flag for callback of Button1 (default: None)
        button2_text    -- String shown on Button2 (default: "")
        button2_command -- int flag for callback of Button2 (default: None)
        """
        super().update_Data(modController,next, previous, title)
        if button1_text:
            self.button1_text.set(button1_text)
        if button1_command:
            self.button1_command.set(button1_command)
        if button2_text:
            self.button2_text.set(button2_text)
        if button1_command:
            self.button2_command.set(button2_command)
        print("Hello")

    def set_Widgets_Visible(self, button1=None, button2=None,buttonNext=None, buttonPrev=None):
        #TODO comment
        if(button1 == "yes"):
            self.button1.pack()
        elif(button1 == "no"):
            self.button1.pack_forget()
        if(button2 == "yes"):
            self.button2.pack()
        elif(button2 == "no"):
            self.button2.pack_forget()

        if(buttonPrev == "yes"):
            self.prev_button.pack()
        elif(buttonPrev == "no"):
            self.prev_button.pack_forget()

        if(buttonNext == "yes"):
            self.next_Button.pack()
        elif(buttonNext == "no"):
            self.next_Button.pack_forget()
