import tkinter as tk
from typing import Container
import Frames.frame_start
import Frames.frame_modules
import inspect
import loadmodules
import loadLog 
import Data as data
import sys




#init the Display and load the singular fames
class Display(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Lennart Brandt")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        
        for F in  (Frames.frame_start.frame_start, Frames.frame_modules.frame_modules):
            self.createFrame(F, F.__name__)
        data.modFrames=loadmodules.loadFrames()
        self.showFrame("frame_start")

    def showFrame(self,cont, prevPage= None):
        display = data.frames[cont]
        display.tkraise()
        if prevPage: display.set_prev_Frame(prevPage)
    
    def createFrame(self, module, name):
        if name not in  data.frames:
            display = module(self.container,self)
            display.grid(row=0, column=0, sticky="nsew")
            data.frames[name] = display


    def createModFrame(self, number, modName):
        frame=data.modFrames[number]
        for name, obj in inspect.getmembers(sys.modules[frame]):
            if inspect.isclass(obj) and obj.__name__.startswith("frame"):
                self.createFrame(obj, modName)
                return modName
        
       
    def getFrameByName(self, frameName):
        return data.frames[frameName]

    def import_xes_Log(self,moduleName, button, name):
        data.log = loadLog.loadLogByName(name)
        successfull = not (not data.log)
        print(successfull)
        if successfull :
            data.frames[moduleName].button_feedback(button,True)
        else:
            data.frames[moduleName].button_feedback(button,False)

    def importModule(self, moduleName, button):
        data.module_List = loadmodules.loadmodules(self)
        for module in data.module_List:
            print(
                "This Module is called: '"
                + module.getName()
                + "' it´s descibed as: "
                + module.getOneDesc()
            )
                    
        successfull = len(data.module_List)>0  
        if successfull :
            data.frames[moduleName].button_feedback(button,True)
        else:
            data.frames[moduleName].button_feedback(button,False)
              
    
   
    

    def getModules(self):
        return data.module_List

    def getLog(self):
        return data.log

    def setLog(self, log):
        data.log=log
        
        


# Start of Programm
app = Display()
app.mainloop()