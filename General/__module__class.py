from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *
#Impl TODO change name
#Impl TODO Change Desc


class module_Example(ModuleFiles):
    """
    Example Class of an Errormodule

    This Class can be used as a template for further Modules

    #Impl TODO indicates areas that need to be adjusted for a new Modul
    """
    def __init__(self, controller):
        super().__init__(__class__,controller)
        """ 
        initializing the Error Modul 

        The global Variables are created here

        """
        #Impl TODO change
        self.name = "Module name"
        self.oneDes = "One line description"
        self.desc = "Longer descriptoion"
        #EXAMPLE FOR LISTS
        self.listGroups = []
        self.currentGroup = int(0)
        ## Settings
        self.settings = {"Setting": 90}


        #Impl TODO IMPLEMENT set Parameter to  start
    def clean(self):
        """ Function to reset all Modul Data"""
        self.baseClean()

    def createFrames(self):
        """ function to create all necessary Frames for the Module"""
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
        """ example function for the starting point of the Algorithm"""
        #Impl  TODO impl
        modErrorList = self.createErrorList([])
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

   #Impl  TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        """ example functions to create valid Error Codes"""
        modErrorList = []
        for element in list:
            error_el = error()
            error_el.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_el)
        return modErrorList

 
  

