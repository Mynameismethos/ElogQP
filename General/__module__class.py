import internalModules.objects as objects
import threading
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
        self.started=False
        ## Settings
        self.settings = {"Setting": 90}


        #TODO IMPLEMENT
        # EXAMPLE
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

    #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher={
            80: lambda: self.getSettingsFromFrame(),
            90: lambda: self.goToNext(),
            99: lambda: self.startSearch(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()

    def exec(self):
        self.createFrames()
        self.log = self.controller.getLog()
        self.visible=True
        self.controller.showModFrame(__class__,next=True)

    def startSearch(self):
        if(not self.started):
            self.started=True
            thread = threading.Thread(target=self.findSimilarNames, args=())
            thread.daemon = True
            thread.start()
            self.controller.getActiveModFrame(__class__).set_Widgets_Visible(button2="yes")

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
        self.visible=False
        self.started=False


    ##STOP IMPLEMENTING
    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getActiveModFrame(__class__).getCanvasAsDict()

    def leaveMod(self):
       print(__name__+": Module finished")
       self.controller.deleteModFrame(__class__)
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
