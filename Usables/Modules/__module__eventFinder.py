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
        frameName = self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=__name__+"_2", previous=None, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

        frameName = self.controller.createModFrame(1, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=__name__+"_3", previous=__name__+"_1", title=self.getName(), list={})

        frameName = self.controller.createModFrame(0, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_1",
                                                              previous=__name__+"_2", title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())

    def leaveMod(self):
        self.controller.getFrameByName("frame_modules").showNextMod()
        for x in range(1, 4):
            if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))

    def exec(self):
        self.createFrames()
        self.controller.showFrame(__name__+"_1")
        self.log = self.controller.getLog()
        self.findEvents()

    def findEvents(self):
        activities = logwork.getAllActivityAsList(self.log)
        self.controller.getFrameByName(
            __name__+"_2").update_Data(list=activities)
