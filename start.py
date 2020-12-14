import tkinter as tk

import Frames.frame_start as fr_start
import loadmodules
import loadLog 

module_List = []
log = object


class Display(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        print("hello")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        display = fr_start.frame_start(container, Controller)
        display.grid(row=0, column=0, sticky="nsew")
        display.tkraise()

class Controller:
    def import_xes_Log(name):
        log = loadLog.loadLogByName(name)

    def importModule():
        module_List = loadmodules.loadmodules()
        for module in module_List:
            print(
                "This Module is called: '"
                + module.getName()
                + "' it´s descibed as: "
                + module.getOneDesc()
            )
            module.exec("null")


app = Display()
app.mainloop()