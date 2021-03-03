import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, Tk
from tkinter.constants import INSERT


class frame_modules(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        myText = Label(self, text="List of all Modules")
        myText.pack()
        self.box_nav = tk.Frame(master=self)
        self.box_nav.pack(side="bottom", fill="x")
        Button(self, text="List all Modules",
               command=lambda: [self.update_Modules()]).pack()
        self.listbox = tk.Listbox(self)
        self.listbox["selectmode"] = "extended"
        self.listbox.pack(fill="both", expand="yes")
        self.modStack = []
        Button(self.box_nav, text="Continue", command=lambda: [
               self.goToNext()]).pack(side="right", fill="both")
        Button(self.box_nav, text="Show Error", command=lambda: [
               self.showError()]).pack(side="right", fill="both")
        Button(self.box_nav, text="Previous Page", command=lambda: [
               self.controller.showPrevFrame()]).pack(side="left", fill="both")

    def showMe(self):
        self.update_Modules()

    def showNextMod(self):
        if(self.modStack):
            self.modStack.pop().exec()
        else:
            self.controller.showFrame("frame_modules")

    def update_Modules(self):
        module_List = self.controller.getModules()
        self.listbox.delete(0, "end")
        for modules in module_List:
           self.listbox.insert("end", modules.getName())

    def goToNext(self):
        chosen = self.listbox.curselection()
        for x in chosen:
            self.modStack.insert(0, self.controller.getModules()[x])
        self.showNextMod()

    def showError(self):
        self.controller.showFrame("frame_showError")
