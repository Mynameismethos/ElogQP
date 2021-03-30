import threading

class ModuleFiles():
    """ 
    Super class of all error searching modules
    """

    def __init__(self,classTyp,controller):
        """ init module by creating base variables and objects """
        self.visible=False
        self.started=False
        self.log = None
        self.controller=controller
        self.classTyp=classTyp


    def baseClean(self):
        """ function to reset varibales set in init """
        self.log = None
        self.visible=False
        self.started=False

    
    def exec(self):
        """
        execution point of the module
        create and show modularframes
        
        """
        self.createFrames()
        self.log=self.controller.getLog()
        self.visible=True
        self.controller.showModFrame(self.classTyp,next=True)

        
    def callBack(self, actionNumer):
        """ function to allow buttons from the gui to interact with functions of the module """
        switcher={
            80: lambda: self.getSettingsFromFrame(),
            90: lambda: self.goToNext(),
            99: lambda: self.startSearch(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()


    def startSearch(self):
        """  
        starting point of the search algorithm

        Creates a new thread for the algorithm to run
        """
        if(not self.started):
            self.started=True
            thread = threading.Thread(target=self.searchAlg, args=())
            thread.daemon = True
            thread.start()
            self.controller.getActiveModFrame(self.classTyp).set_Widgets_Visible(button2="yes")


    
    def leaveMod(self):
        """ function to leave Module and remove Module Data from Persistenz """
        print(self.classTyp.__name__+": Module finished")
        self.controller.deleteModFrame(self.classTyp)
        if(self.visible):
                self.controller.getFrameByName("frame_modules").showNextMod()
        self.clean()

    def goToNext(self):
        """ function to call for the next Frame on the stack to be show"""
        self.controller.getFrameByName("frame_modules").showNextMod()
        self.visible=False

    ########## Getter + Setter Functions #############
    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getActiveModFrame(self.classTyp).getCanvasAsDict()

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getLog(self, log):
        self.log = log


