
from internalModules.objects import *
import tkinter as tk
import Frames.frame_start
import Frames.frame_modules
import Frames.frame_showError


class Frame_Controller(tk.Tk):
    """
    The Frame controller controlls the GUI
    """
    def __init__(self,*args, **kwargs):
        """
        init the Gui
        load the frames of the Framework
        show the first Frame
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("ElogQP")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.activeFrames = []
        for F in (Frames.frame_start.frame_start, Frames.frame_modules.frame_modules, Frames.frame_showError.frame_showError):
            self.createFrame(F, F.__name__)
        
        self.showFrame("frame_start")  
  

    def showFrame(self, position):
        """
        function to display the frame specified by the postion
        """
        display = self.data.frames[position]
        self.activeFrames.append(display)
        display.tkraise()
        display.showMe()


    def showPrevFrame(self):
        """
        function to pop frames from the Previous stack and show the previous Framework Frame
        """
        if(self.hasPrevFrame()):
            self.activeFrames.pop()
            self.activeFrames[-1].tkraise()
        else:
            self.showFrame("frame_start")

    def hasPrevFrame(self):
        """
        function to check if a previous Framework Frame exists

        returns boolean
        """
        self.deleteDouble()
        return (len(self.activeFrames) > 1)

    def deleteDouble(self):
        """
        function to clean up the frame Stack
        """
        prev=None
        for x in reversed(self.activeFrames):
            if(prev):
                if(isinstance(x ,prev.__class__)):
                    del self.activeFrames[self.activeFrames.index(prev)]
            prev=x

    def createFrame(self, module, name):
        """
        #TODO check if we still use this
        """
        if name not in self.data.frames:
            display = module(self.container, self)
            display.grid(row=0, column=0, sticky="nsew")
            self.data.frames[name] = display

    def getFrameByName(self, frameName):
        """ return the frame specified by the name"""
        return self.data.frames[frameName]

    def delFrameByName(self, frameName):
        """" delete frame specified by the name"""
        self.data.frames[frameName].destroy()
        del self.data.frames[frameName]

    ###Controlling Modular Frames######

    def showModFrame(self, name,next=False, prev=False):
        """
        function to display a Modular Frame
        """
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
        """
        function to delete modframe Stack
        """
        del self.data.activeMod[name]


    def createModFrame(self, number,name):
        """
        function to create mod Frames
        creates modframe Stack and loads the first Frame of the stack

        """
        frame = self.data.modFrames[number]
        display = frame(self.container, self)
        display.grid(row=0, column=0, sticky="nsew")
        if(name not in self.data.activeMod):self.data.activeMod[name]= module()
        self.data.activeMod[name].modFramesNext.append(display)

    def getActiveModFrame(self,name):
        """returns the Modframe that is currently visible"""
        return self.data.activeMod[name].modFramesPrev[-1]

    def getNextModFrame(self,name):
        """returns the modframe that is next on the modframe stack"""
        return self.data.activeMod[name].modFramesNext[-1]