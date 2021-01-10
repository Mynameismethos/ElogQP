import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Listbox
from tkinter.constants import BOTTOM, INSERT, X


class frame_start(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        Label(self, text="Tool zum Finden und Beheben von Fehlern in Eventlog",
              bg="light blue").pack(fill="x")
        Label(self, text="Bitte geben Sie den Namen der Logdatei an und Laden sie den Log",
              bg="light blue").pack(fill="x")
        #entry = Entry(self)
        #entry.insert(INSERT, "LOGEDV.xes")
        b_search = Button(self, text="Find XES Files", command=lambda: [
                          controller.get_xes_file_list()])
        b_search.pack()
        self.listbox = Listbox(self)
        self.listbox["selectmode"] = "single"
        self.listbox.pack(fill="both", expand="yes")
        #entry.pack()
        self.load_Log_button = Button(
            self, text="Load XES", command=lambda: [self.load_Log_button.configure(bg="orange"), controller.import_xes_Log(self.load_Log_button, self.listbox.get(self.listbox.curselection()))]
        )
        self.load_Log_button.pack()
        load_module_button = Button(
            self, text="Load Module", command=lambda: [load_module_button.configure(bg="orange"), controller.importModule(load_module_button)]
        )

        load_module_button.pack()

        box_nav = tk.Frame(master=self)
        box_nav.pack(side="bottom", fill="x")
        next_button = Button(
            box_nav, text="Next Page", command=lambda: [self.goToNext(controller)]
        )
        next_button.pack(side="right", fill="both")

    def showMe(self):
        self.controller.get_xes_file_list()

    def button_feedback(Frame, button, successfull):
        if successfull:
            button.configure(bg="green")
        else:
            button.configure(bg="red")

    def updateData(self, list=[],highlight=None):
        if list:
            self.listbox.delete(0, "end")
            for x in list:
                self.listbox.insert("end", x)
            self.listbox.select_set(0)


    def goToNext(self, controller):
        if(len(controller.getModules()) > 0 and not (not controller.getLog())):
            controller.showFrame("frame_modules", __class__.__name__)
        #else set Buttoncolor to red

    def set_Prev_Frame(self):
        if self.controller.hasPrevFrame():
            prev_button = Button(
                self.box_nav, text="Previous Page", command=lambda: [self.controller.showPrevFrame(), prev_button.destroy()])
            prev_button.pack(side="left", fill="both")
    