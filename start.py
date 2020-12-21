import tkinter as tk
import Frames.frame_start
import Frames.frame_modules
import loadmodules
import loadLog 
import Data as data



#init the Display and load the singular fames
class Display(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        print("hello")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        
        for F in  (Frames.frame_start.frame_start, Frames.frame_modules.frame_modules):
            display = F(container, Controller)
            frame_name= F.__name__
            data.frames[frame_name] = display
            display.grid(row=0, column=0, sticky="nsew")
            
        Display.showFrame("frame_start")

    def showFrame(cont, prevPage= None):
        display = data.frames[cont]
        display.tkraise()
        if prevPage: display.set_prev_Frame(prevPage)


class Controller:
    def import_xes_Log(moduleName, button, name):
        data.log = loadLog.loadLogByName(name)
        successfull = not (not data.log)
        print(successfull)
        if successfull :
            data.frames[moduleName].button_feedback(button,True)
        else:
            data.frames[moduleName].button_feedback(button,False)

    def importModule(moduleName, button):
        data.module_List = loadmodules.loadmodules()
        for module in data.module_List:
            print(
                "This Module is called: '"
                + module.getName()
                + "' it´s descibed as: "
                + module.getOneDesc()
            )
            module.exec("null")
            
        successfull = len(data.module_List)>0    
        if successfull :
            data.frames[moduleName].button_feedback(button,True)
        else:
            data.frames[moduleName].button_feedback(button,False)
            
            

    def showFrame(page,prevPage=None):
        Display.showFrame(page,prevPage)

    def getModules():
        return data.module_List

    def getLog():
        return data.log


# Start of Programm
app = Display()
app.mainloop()