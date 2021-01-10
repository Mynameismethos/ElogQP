import tkinter as tk
import Frames.frame_start
import Frames.frame_modules
import Frames.frame_showError
import internalModules.loadmodules as loadmodules

import internalModules.loadLog as loadLog
import internalModules.Data as data


#init the Display and load the singular fames
class Display(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Lennart Brandt")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.activeFrames = []

        for F in (Frames.frame_start.frame_start, Frames.frame_modules.frame_modules, Frames.frame_showError.frame_showError):
            self.createFrame(F, F.__name__)
        data.modFrames = loadmodules.loadFrames()
        self.showFrame("frame_start")

    def showFrame(self, cont, prevPage=None):
        display = data.frames[cont]
        self.activeFrames.append(display)
        display.tkraise()
        display.showMe()

    def showPrevFrame(self):
        if(self.hasPrevFrame()):
            self.activeFrames.pop()
            self.activeFrames[-1].tkraise()
        else:
            self.showFrame("frame_start")

    def hasPrevFrame(self):
        self.deleteDouble()
        return (len(self.activeFrames) > 1)

    def deleteDouble(self):
        prev=None
        for x in reversed(self.activeFrames):
            if(prev):
                if(isinstance(x ,prev.__class__)):
                    del self.activeFrames[self.activeFrames.index(prev)]
            prev=x

    def createFrame(self, module, name):
        if name not in data.frames:
            display = module(self.container, self)
            display.grid(row=0, column=0, sticky="nsew")
            data.frames[name] = display

    def addToErrorList(self, modErrorList):
        #Check if Entrys already Exist
        for x in modErrorList:
            data.error_List.append(x)

    def createModFrame(self, number, modName):
        frame = data.modFrames[number]
        self.createFrame(frame, modName)
        return modName

    def getFrameByName(self, frameName):
        return data.frames[frameName]

    def delFrameByName(self, frameName):
        data.frames[frameName].destroy()
        del data.frames[frameName]
    
    def deleteModFrame(self):
        for key in list(data.frames):
            if ("Usables" in key):
                del data.frames[key]
       
        for x in reversed(self.activeFrames):
           if ("frame_mod_" in x._name):
                self.activeFrames.remove(x)
    
        
            


    def get_xes_file_list(self):
        list = loadLog.getAllLogs()
        self.getFrameByName("frame_start").updateData(list)

    def import_xes_Log(self, button, name):
        data.log = loadLog.loadLogByName(self,name,button)


    def importModule(self, button):
        data.module_List = loadmodules.loadmodules(self)
        for module in data.module_List:
            print(
                "This Module is called: '"
                + module.getName()
                + "' it´s descibed as: "
                + module.getOneDesc()
            )
        moduleName="frame_start"
        successfull = len(data.module_List) > 0
        if successfull:
            data.frames[moduleName].button_feedback(button, True)
        else:
            data.frames[moduleName].button_feedback(button, False)

    def getModules(self):
        return data.module_List

    def getErrorList(self):
        return data.error_List

    def getLog(self):
        return data.log

    def setLog(self, log, button=None,name=None):
        if(button):
            data.frames["frame_start"].button_feedback(button, True)
            data.frames["frame_start"].updateData(highlight=name)
        data.log = log


# Start of Programm
app = Display()
app.mainloop()
