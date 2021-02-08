from internalModules.objects import *
import tkinter as tk
import Frames.frame_start
import Frames.frame_modules
import Frames.frame_showError

class Frame_Controller(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Lennart Brandt")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.activeFrames = []
        for F in (Frames.frame_start.frame_start, Frames.frame_modules.frame_modules, Frames.frame_showError.frame_showError):
            self.createFrame(F, F.__name__)
        
        self.showFrame("frame_start")  
  

    def showFrame(self, cont):
        display = self.data.frames[cont]
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
        if name not in self.data.frames:
            display = module(self.container, self)
            display.grid(row=0, column=0, sticky="nsew")
            self.data.frames[name] = display

    def getFrameByName(self, frameName):
        return self.data.frames[frameName]

    def delFrameByName(self, frameName):
        self.data.frames[frameName].destroy()
        del self.data.frames[frameName]

    ###Controlling Modular Frames######

    def showModFrame(self, name,next=False, prev=False):
        display=None
        if(next):
            if(self.data.activeMod[name].modFramesNext):
                self.data.activeMod[name].modFramesPrev.append(self.data.activeMod[name].modFramesNext.pop())
            else:
                self.getFrameByName("frame_modules").showNextMod()
        elif(prev):
            if(len(self.data.activeMod[name].modFramesPrev)>1):
                self.data.activeMod[name].modFramesNext.append(self.data.activeMod[name].modFramesPrev.pop())
            else: self.showPrevFrame()
        else: 
            pass

        display = self.data.activeMod[name].modFramesPrev[-1]
        display.tkraise()
        display.showMe()

    def deleteModFrame(self,name):
        del self.data.activeMod[name]


    def createModFrame(self, number,name):
        frame = self.data.modFrames[number]
        display = frame(self.container, self)
        display.grid(row=0, column=0, sticky="nsew")
        if(name not in self.data.activeMod):self.data.activeMod[name]= module()
        self.data.activeMod[name].modFramesNext.append(display)

    def getActiveModFrame(self,name):
        return self.data.activeMod[name].modFramesPrev[-1]

    def getNextModFrame(self,name):
        return self.data.activeMod[name].modFramesNext[-1]