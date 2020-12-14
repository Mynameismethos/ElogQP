import pm4py
import tkinter as tk

import frames as fr
import loadmodules

class Display(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        print("hello")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        display = fr.frame_start(container, self)
        display.grid(row=0, column=0, sticky="nsew")
        display.tkraise()

class Controller:
     def display_hello():
        self.myText.pack()

    def remove_hello():
        self.myText.pack_forget()

    def import_xes_Log():
        log = pm4py.read_xes()

    def importModule():
        module_list = loadmodules.loadmodules()
        for module in module_list:
            print(
                "This Module is called: '"
                + module.getName()
                + "' it´s descibed as: "
                + module.getOneDesc()
            )
            module.exec("null")


app = Display()
app.mainloop()