import tkinter as tk
from tkinter import Button, Label
import internalModules.objects as objects
from tkinter import ttk


class frame_showError(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        Label(self, text="Tool zum Finden und Beheben von Fehlern in Eventlog",
              bg="light blue").pack(fill="x")
        self.controller = controller
        self.errorTree = ttk.Treeview(self)

        self.errorTree["columns"] = (
            "ID", "Desc", "Trace", "Event", "Value", "Module", "Repair")
        self.errorTree.column("#0", width=25, stretch=False)
        self.errorTree.column("ID", anchor="w", width=120)
        self.errorTree.column("Desc", anchor="w")
        self.errorTree.column("Trace", anchor="w")
        self.errorTree.column("Event", anchor="w")
        self.errorTree.column("Value", anchor="w")
        self.errorTree.column("Module", anchor="w")
        self.errorTree.column("Repair", anchor="w")

        self.errorTree.heading("#0", text="", anchor="w")
        self.errorTree.heading("ID", text="ID", anchor="w")
        self.errorTree.heading("Desc", text="Desc", anchor="w")
        self.errorTree.heading("Trace", text="Trace", anchor="w")
        self.errorTree.heading("Event", text="Event", anchor="w")
        self.errorTree.heading("Value", text="Value", anchor="w")
        self.errorTree.heading("Module", text="Module", anchor="w")
        self.errorTree.heading("Repair", text="Repair", anchor="w")

        self.errorTree.pack(fill="both", expand="yes")
        self.filterList(self.controller.getErrorList())

        box_nav = tk.Frame(master=self)
        box_nav.pack(side="bottom", fill="x")
        for x in range(7):
            box_nav.columnconfigure(x, weight=1)

        buttonAutoSolve = Button(
            box_nav, text="Auto Solve Selected", command=lambda: [self.autoSolve()]
        )
        buttonEdit = Button(box_nav, text="Edit Selected",
                            command=lambda: self.editSelected())
        leave = Button(box_nav, text="Go Back",
                       command=lambda: self.controller.showPrevFrame())

        leave.grid(row=0, column=0, columnspan=2, sticky="nsew")
        buttonEdit.grid(row=0, column=5, sticky="nsew")
        buttonAutoSolve.grid(row=0, column=6, sticky="nsew")

    def showMe(self):
        self.updateList()

    def updateTable(self, list):
        self.cleanTree()
        counter = 0
        for x in list:
            val = (counter, x.desc, x.trace, x.event,
                   x.dictVal, x.errorModul, x.autoRepair)
            self.errorTree.insert(parent="", index="end",
                                  iid=counter, text="", values=val)
            #TODO add Repairchild
            if(x.autoRepair):
                val = (counter, x.desc, x.trace, x.event,
                       x.fixedVal, x.errorModul, x.autoRepair)
                self.errorTree.insert(
                    parent=counter, index="end", iid=counter+1, text="", values=val)
                counter += 1
            counter += 1

    def filterList(self, list):
        self.updateTable(list)

    def updateList(self):
        self.filterList(self.controller.getErrorList())

    def editSelected(self):
        pass

    def autoSolve(self):
        pass

    def cleanTree(self):
        self.errorTree.delete(*self.errorTree.get_children())
