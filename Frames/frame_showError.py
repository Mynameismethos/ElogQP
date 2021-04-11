import tkinter as tk
from tkinter import Button, Label, StringVar
import internalModules.objects as objects
from tkinter import ttk


class frame_showError(tk.Frame):
    """ 
    Frame to show the error codes
    """
    def __init__(self, parent, controller):
        """
        Initializing the layout of the Eventlog

        in this function Coloumns can be created, edited and removed 
        """
        super().__init__(parent)
        Label(self, text="Discovering error patterns in eventlogs",
              bg="light blue").pack(fill="x")
        self.controller = controller
        self.errorTree = ttk.Treeview(self)
        self.eRate=StringVar()
        ErrorRate = Label(self, textvariable=self.eRate)
        ErrorRate.pack()

        self.errorTree["columns"] = (
            "ID", "Desc", "Trace", "Value", "Module", "Repair")
        self.errorTree.column("#0", width=50, stretch=False)
        self.errorTree.column("ID", anchor="w", width=120)
        self.errorTree.column("Desc", anchor="w")
        self.errorTree.column("Trace", anchor="w")
       # self.errorTree.column("Event", anchor="w")
        self.errorTree.column("Value", anchor="w")
        self.errorTree.column("Module", anchor="w")
        self.errorTree.column("Repair", anchor="w")

        self.errorTree.heading("#0", text="", anchor="w")
        self.errorTree.heading("ID", text="ID", anchor="w")
        self.errorTree.heading("Desc", text="Desc", anchor="w")
        self.errorTree.heading("Trace", text="Trace", anchor="w")
       # self.errorTree.heading("Event", text="Event", anchor="w")
        self.errorTree.heading("Value", text="Value", anchor="w")
        self.errorTree.heading("Module", text="Module", anchor="w")
        self.errorTree.heading("Repair", text="Repair", anchor="w")

        scroll=ttk.Scrollbar(self, orient="vertical", command=self.errorTree.yview)
        scroll.pack(side="right", fill="y")
        self.errorTree.configure(yscrollcommand=scroll.set)
        self.filterList(self.controller.getErrorList())
        box_nav = tk.Frame(master=self)
        box_nav.pack(side="bottom", fill="x")
        self.errorTree.pack(fill="both", expand="yes")

        for x in range(7):
            box_nav.columnconfigure(x, weight=1)

        buttonAutoSolve = Button(
            box_nav, text="Auto Solve Selected", command=lambda: [self.autoSolve()]
        )
        buttonEdit = Button(box_nav, text="Edit Selected",
                            command=lambda: self.editSelected())
        buttonClearList = Button(box_nav, text="Clear Error List",
                            command=lambda: self.clearErrorList())
        leave = Button(box_nav, text="Go Back",
                       command=lambda: self.controller.showPrevFrame())

        leave.grid(row=0, column=0, columnspan=2, sticky="nsew")
        buttonClearList.grid(row=0, column=4, sticky="nsew")

        """ 
        These elements lie dorment until some Autosolving functions are implemented
        """
        #buttonEdit.grid(row=0, column=5, sticky="nsew")
        #buttonAutoSolve.grid(row=0, column=6, sticky="nsew")

    def showMe(self):
        """ function to be called right after Frame is shown """
        self.updateList()

    def updateTable(self, list):
        """ this functions updates the tabe visualizing the Error Codes"""
        self.cleanTree()
        self.eRate.set("Log Quality: "+str(self.controller.data.errorRate))
        counter = 0
        parentDict = {}
        for x in list:
            errorMod=x.errorModul.name
            

            val = (counter, x.desc, x.trace,
                   x.dictVal, errorMod, x.autoRepair)
            parent=""
            if(x.parent in parentDict):parent=parentDict[x.parent]
            id=self.errorTree.insert(parent=parent, index="end",
                                  iid=counter, text="", values=val)
            parentDict[x]=id
            counter += 1

    def filterList(self, list):
        """ function to possibly filter the Errorcodes"""
        self.updateTable(list)

    def updateList(self):
        """ remote function to update the Table"""
        self.filterList(self.controller.getErrorList())

    def editSelected(self):
        """ 
        This function lies dorment until some Autosolving functions are implemented
        """
        pass

    def clearErrorList(self):
        """ 
        this function calles the controller clean the errorlists
        and updates the table accordingly
        """
        self.controller.clearErrorList()
        self.updateList()

    def autoSolve(self):
        """ 
        This function lies dorment until some Autosolving functions are implemented
        """
        pass

    def cleanTree(self):
        """ 
        This functions removes all elements from the table
        """
        self.errorTree.delete(*self.errorTree.get_children())
