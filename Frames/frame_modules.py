import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, Tk
from tkinter.constants import INSERT


class frame_modules(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller
        myText = Label(self, text="Hello World from Modules")
        myText.pack()
        self.box_nav = tk.Frame(master = self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self, text="List all Modules", command= lambda: [self.update_Modules()]).pack()
        self.listbox = tk.Listbox(self)
        self.listbox["selectmode"] = "extended"
        self.listbox.pack()
        Button(self.box_nav, text="Continue",command=lambda:[self.goToNext()]).pack(side="right", fill="both")

        
    def update_Modules(self):
        module_List=self.controller.getModules()
        self.listbox.delete(0,"end")
        for modules in module_List:
           self.listbox.insert("end", modules.getName())

    def set_prev_Frame(self, prevFrame):
        prev_frame=prevFrame
        if prev_frame:
            prev_button = Button(
            self.box_nav, text="Previous Page", command=lambda: [self.controller.showFrame(prevFrame), prev_button.destroy()])
            prev_button.pack(side="left",fill="both")

    def goToNext(self):
        chosen= self.listbox.curselection()
        print(chosen)
        for x in chosen:
            self.controller.getModules()[x].exec()


