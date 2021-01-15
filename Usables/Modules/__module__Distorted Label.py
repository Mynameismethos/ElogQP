import threading
import internalModules.logwork as logwork
import internalModules.compare as compare
import internalModules.objects as objects

class module_distoredLabel():
    def __init__(self, controller):
        self.controller= controller
        self.settings = {"LevLower": 90}
        self.log = ""
        self.name = "Distorted Label"
        self.oneDes = "this programm checks The Event Names for similar but unequal Names "
        #TODO change 
        self.visible=False
        self.desc = ""
        self.listGroups=[]
        self.currentGroup=int(0)

    def createFrames(self):
        #Start Programm
        frameName=self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Search for Distored Labels", button1_command =99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        frameName=self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= True,title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        frameName=self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

    #Callback der Mod_Frames
    def callBack(self, actionNumer):
        switcher={
            80: lambda: self.getSettingsFromFrame(),
            90: lambda: self.goToNext(),
            99: lambda: self.startSearch(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()
            
    #Einstiegspunkt des Modules
    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.visible=True
        self.controller.showModFrame(__class__,next=True)

    def startSearch(self):
        thread = threading.Thread(target=self.findSimilarNames, args=())
        thread.daemon = True
        thread.start()
        self.controller.getActiveModFrame(__class__).set_Widgets_Visible(button2="yes")


    def findSimilarNames(self):
        tupelListAc=compare.levinRatio(logwork.getAllActivityAsList(self.log),int(self.getSettings().get("LevLower")))
        groupListAc= compare.createGroups(tupelListAc,"concept:name")

        tupelListRe=compare.tokenRatio(logwork.getAllResourcesAsList(self.log),int(self.getSettings().get("LevLower")))
        groupListRe= compare.createGroups(tupelListRe,"org:resource")
        self.listGroups=groupListAc+groupListRe
        self.addToErrorList(self.listGroups)
        self.leaveMod()


    def addToErrorList(self, list):
        modErrorList= []
        for group in list:
            error = objects.error()
            error.set(trace="Global",dictVal=[group.getList()],dictkey=group.getTyp(), classInfo=0,errorModul=self)
            modErrorList.append(error)
        self.controller.addToErrorList(modErrorList)

    def getSettings(self):
        return self.settings


    def setSettings(self, settings):
        self.settings=settings

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
       

    def clean(self):
        self.currentGroup=0
        self.log = None
        self.visible=False
        self.listGroups=[]


    def getName(self):
        return self.name


    def getOneDesc(self):
        return self.oneDes


    def getDesc(self):
        return self.desc

    def getLog(self,log):
        self.log = log

 

    # def displayPrev(self):
    #     frame=__class__+"_4"
    #     selected= self.controller.getFrameByName(frame).getSelected()
    #     if(selected):
    #         name=self.listGroups[self.currentGroup].getList()[selected[0]]
    #         self.listGroups[self.currentGroup].setName(name)
    #     if(self.currentGroup>0):
    #         self.currentGroup-=1
    #         self.controller.getFrameByName(frame).set_Button_Visible(button2="yes")
    #     else:#removebutton
    #         self.controller.getFrameByName(frame).set_Button_Visible(button1="no")
    #     self.displayGroup()
        
    #     # not Main
    # def displayNext(self):
    #     frame=__class__+"_4"
    #     selected= self.controller.getFrameByName(frame).getSelected()
    #     if(selected):
    #         name=self.listGroups[self.currentGroup].getList()[selected[0]]
    #         self.listGroups[self.currentGroup].setName(name)
    #     if(self.currentGroup<len(self.listGroups)-1):
    #         self.currentGroup+=1
    #         self.controller.getFrameByName(frame).set_Button_Visible(button1="yes")
    #     else:  #removebutton
    #         self.controller.getFrameByName(frame).set_Button_Visible(button2="no")
    #     self.displayGroup()
        
    #     # not Main
    # def displayGroup(self):
    #     item=self.listGroups[self.currentGroup]
    #     indexOfName=None
    #     if(item.getName() in item.getList()):
    #         indexOfName= item.getList().index(item.getName())
    #     self.controller.getFrameByName(__class__+"_4").update_Data(list=item.getList(), selected=indexOfName)


    #     # not Main
    # def changeLog(self):
    #     for group in self.listGroups:
    #         name= group.getName()
    #         if(name):
    #             namelist= group.getList()
    #             for x in range(len(self.log)):
    #                 for y in range(len(self.log[x])):
    #                     logelement= self.log[x][y][group.getTyp()]
    #                     if logelement in namelist:
    #                         self.log[x][y][group.getTyp()]=name


    #     self.controller.setLog(self.log)
    #     self.leaveMod()