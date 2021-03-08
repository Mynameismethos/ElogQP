from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *


class module_HomonymousLabels(ModuleFiles):
    def __init__(self, controller):
        super().__init__(__class__,controller)

        self.name = " Not Done Homonymous Label"
        self.oneDes = "this module checks for Homonymous Labels"
        self.desc = ""
        #EXAMPLE FOR LISTS
        self.listGroups = []
        self.currentGroup = int(0)
        ## Settings
        self.settings = {"Setting": 90}

    def clean(self):
        self.baseClean()

    def createFrames(self):
        #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Search for Distored Labels", button1_command =99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= True,title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())



    def searchAlg(self):
        #TODO impl
        modErrorList = self.createErrorList([])
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

   #TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error_el = error()
            error_el.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_el)
        return modErrorList

 
  

