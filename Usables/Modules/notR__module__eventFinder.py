import internalModules.logwork as logwork


class module_eventFinder():
    def __init__(self, controller):
        self.controller = controller
        self.settings = "hello"
        self.log = ""
        self.name = "Event Names"
        self.oneDes = "this programm finds and Lists all Event Names"
        self.desc = "Dont want to fill this Out Right now"

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getLog(self, log):
        self.log = log

    def createFrames(self):
        frameName = self.controller.createModFrame(0)
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=False,previous=True, title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())
        
        frameName = self.controller.createModFrame(1)
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=True, previous=True, title=self.getName(), list={})

        frameName = self.controller.createModFrame(0)
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=True, previous=False, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

    def leaveMod(self):
        self.controller.deleteModFrame()
        self.controller.getFrameByName("frame_modules").showNextMod()

    def exec(self):
        self.createFrames()
        self.log = self.controller.getLog()
        self.controller.showModFrame(next=True)
        self.findEvents()

    def findEvents(self):
        activities = logwork.getAllActivityAsList(self.log)
        self.controller.getActiveModFrame().update_Data(list=activities)
