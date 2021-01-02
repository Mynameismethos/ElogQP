import internalModules.logwork as logwork
import internalModules.compare as compare
from fuzzywuzzy import fuzz

class module_distoredLabel():
    def __init__(self, controller):
        self.controller= controller
        self.settings = {"LevLower": 90}
        self.log = ""
        self.name = "Distorted Label"
        self.oneDes = "this programm checks The Event Names for similar but unequal Names "
        #TODO change 
        self.desc = ""

    def createFrames(self):
        #Greetings Page
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Settings
        frameName=self.controller.createModFrame(3, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title=self.getName(), settings=self.getSettings(), button1_text="Save", button1_command=1)
        #Start Programm
        frameName=self.controller.createModFrame(2, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_4",previous= __name__+"_2",title=self.getName(), button_text="Search for Distored Labels", button_command =0)
        #Display Results
        frameName=self.controller.createModFrame(1, __name__+"_4")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_5", previous=__name__+"_3",title=self.getName(),)
        #Show Changes and Run Programm
        frameName=self.controller.createModFrame(2, __name__+"_5")
        self.controller.getFrameByName(frameName).update_Data(modController=self, previous=__name__+"_4",title=self.getName(),)
    
    def callBack(self, actionNumer):
        switcher={
            0: lambda: self.findSimilarNames(),
            1: lambda: self.getSettingsFromFrame()
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()
            

    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.controller.showFrame(__name__+"_1")

    def findSimilarNames(self):
        tupelListAc=compare.levinRatio(logwork.getAllActivityAsList(self.log),int(self.getSettings().get("LevLower")))
        groupeListAc= compare.createGroups(tupelList=tupelListAc)

        tupelListRe=compare.levinRatio(logwork.getAllResources(self.log),int(self.getSettings().get("LevLower")))
        groupeListRe= compare.createGroups(tupelList=tupelListRe)
        
        print("break")



    def getSettings(self):
        return self.settings


    def setSettings(self, settings):
        self.settings=settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getFrameByName(__name__+"_2").getSettings()

    def leaveMod(self):
       self.controller.showFrame("frame_modules")
       for x in range(1,6):
           if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))


    def getName(self):
        return self.name


    def getOneDesc(self):
        return self.oneDes


    def getDesc(self):
        return self.desc

    def getLog(self,log):
        self.log = log

 

