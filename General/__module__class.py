import internalModules.objects as objects
#TODO change name
#TODO Change Desc

class module_Example():
    def __init__(self, controller):
        self.controller = controller
        #TODO change
        self.name = "Distorted Label"
        self.oneDes = "this programm checks The Event Names for similar but unequal Names "
        self.desc = ""
        self.log = None
        #EXAMPLE FOR LISTS
        self.listGroups = []
        self.currentGroup = int(0)
        ## Settings
        self.settings = {"Setting": 90}


        #TODO IMPLEMENT
        # EXAMPLE
    def createFrames(self):
        #Greetings Page
        frameName = self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=__name__+"_2", previous=None, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Settings
        frameName = self.controller.createModFrame(3, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3", previous=__name__ +
                                                              "_1", title=self.getName(), canDict=self.getSettings(), button1_text="Save", button1_command=1)
        #Start Programm
        frameName = self.controller.createModFrame(2, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, previous=__name__+"_2", title=self.getName(), button_text="Search for Distored Labels", button_command=99)

    #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher = {

            80: lambda: self.displayPrev(__name__+"_4"),
            81: lambda: self.displayNext(__name__+"_4"),
            99: lambda: self.search(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()

    def exec(self):
        self.createFrames()
        self.log = self.controller.getLog()
        self.controller.showFrame(__name__+"_1")

    def search(self):


        modErrorList=self.createErrorList(self.listGroups)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

   #TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error = objects.error()
            error.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error)
        return modErrorList

 
  
    #TODO IMPLEMENT set Parameter to  start
    def clean(self): 
        self.log = None


    ##STOP IMPLEMENTING
    def leaveMod(self):
       self.controller.deleteModFrame()
       self.controller.getFrameByName("frame_modules").showNextMod()

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self,settingPage):
        self.settings = self.controller.getFrameByName(
            __name__+"_"+settingPage).getSettings()

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getLog(self, log):
        self.log = log
