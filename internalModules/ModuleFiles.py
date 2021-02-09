import threading

class ModuleFiles():

    def __init__(self,classTyp,controller):
        self.visible=False
        self.started=False
        self.log = None
        self.controller=controller
        self.classTyp=classTyp


    def baseClean(self):
        self.log = None
        self.visible=False
        self.started=False

    
    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.visible=True
        self.controller.showModFrame(self.classTyp,next=True)

        #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher={
            80: lambda: self.getSettingsFromFrame(),
            90: lambda: self.goToNext(),
            99: lambda: self.startSearch(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()


    def startSearch(self):
        if(not self.started):
            self.started=True
            thread = threading.Thread(target=self.searchAlg, args=())
            thread.daemon = True
            thread.start()
            self.controller.getActiveModFrame(self.classTyp).set_Widgets_Visible(button2="yes")

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getActiveModFrame(self.classTyp).getCanvasAsDict()

    def leaveMod(self):
       print(self.classTyp.__name__+": Module finished")
       self.controller.deleteModFrame(self.classTyp)
       if(self.visible):
            self.controller.getFrameByName("frame_modules").showNextMod()
       self.clean()

    def goToNext(self):
        self.controller.getFrameByName("frame_modules").showNextMod()
        self.visible=False
    

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getLog(self, log):
        self.log = log


