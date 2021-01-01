


class module_hello():
    def __init__(self, controller):
        self.controller= controller
        self.Settings = "hello"
        self.log = ""
        self.name = "Hello Bot"
        self.oneDes = "this programm says Hello"
        self.desc = "this programm calls print. And gives it the Parameter 'Hello' "
    def getName(self):
        return self.name


    def getOneDesc(self):
        return self.oneDes


    def getDesc(self):
        return self.desc


    def getSettings(self):
        return self.Settings


    def setSettings(self, settings):
        self.Settings


    def getLog(self,log):
        self.log = log

    def createFrames(self):
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        
        frameName=self.controller.createModFrame(0, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())
        
        frameName=self.controller.createModFrame(0, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_1", previous=__name__+"_2",title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())
    
    def leaveMod(self):
        self.controller.showFrame("frame_modules")
        for x in range(1,6):
            if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))

    def exec(self):
        self.createFrames()
        self.controller.showFrame(__name__+"_1")
        print("Hello")

