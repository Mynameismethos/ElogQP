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
        self.listGroups=[]
        self.currentGroup=int(0)

    def createFrames(self):
        #Greetings Page
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Settings
        frameName=self.controller.createModFrame(3, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title=self.getName(), settings=self.getSettings(), button1_text="Save", button1_command=1)
        #Start Programm
        frameName=self.controller.createModFrame(2, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self,previous= __name__+"_2",title=self.getName(), button_text="Search for Distored Labels", button_command =0)
        #Display Found 
        frameName=self.controller.createModFrame(1, __name__+"_4")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_5", previous=__name__+"_3",title="List Found Groups",button1_text="Previous Group", button1_command=3, button2_text="Next Group", button2_command=4)
        self.controller.getFrameByName(frameName).setMultiselect(False)
        #Show Changes and Run Programm
        frameName=self.controller.createModFrame(2, __name__+"_5")
        self.controller.getFrameByName(frameName).update_Data(modController=self, previous=__name__+"_4",title=self.getName(),button_text="Apply changes to Log", button_command =99)
    
    #Callback der Mod_Frames
    def callBack(self, actionNumer):
        switcher={
            0: lambda: self.findSimilarNames(),
            1: lambda: self.getSettingsFromFrame(),
            3: lambda: self.displayPrev(),
            4: lambda: self.displayNext(),
            99:lambda: self.changeLog(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()
            
    #Einstiegspunkt des Modules
    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.controller.showFrame(__name__+"_1")

    def findSimilarNames(self):
        tupelListAc=compare.levinRatio(logwork.getAllActivityAsList(self.log),int(self.getSettings().get("LevLower")))
        groupListAc= compare.createGroups(tupelListAc,"concept:name")

        tupelListRe=compare.levinRatio(logwork.getAllResources(self.log),int(self.getSettings().get("LevLower")))
        groupListRe= compare.createGroups(tupelListRe,"org:resource")
        self.listGroups=groupListAc+groupListRe
        self.displayGroup()
        self.controller.showFrame(__name__+"_4")

    def displayPrev(self):
        frame=__name__+"_4"
        selected= self.controller.getFrameByName(frame).getSelected()
        if(selected):
            name=self.listGroups[self.currentGroup].getList()[selected[0]]
            self.listGroups[self.currentGroup].setName(name)
        if(self.currentGroup>0):
            self.currentGroup-=1
            self.controller.getFrameByName(frame).set_Button_Visible(button2="yes")
        else:#removebutton
            self.controller.getFrameByName(frame).set_Button_Visible(button1="no")
        self.displayGroup()
        
    def displayNext(self):
        frame=__name__+"_4"
        selected= self.controller.getFrameByName(frame).getSelected()
        if(selected):
            name=self.listGroups[self.currentGroup].getList()[selected[0]]
            self.listGroups[self.currentGroup].setName(name)
        if(self.currentGroup<len(self.listGroups)-1):
            self.currentGroup+=1
            self.controller.getFrameByName(frame).set_Button_Visible(button1="yes")
        else:  #removebutton
            self.controller.getFrameByName(frame).set_Button_Visible(button2="no")
        self.displayGroup()
        

    def displayGroup(self):
        item=self.listGroups[self.currentGroup]
        indexOfName=None
        if(item.getName() in item.getList()):
            indexOfName= item.getList().index(item.getName())
        self.controller.getFrameByName(__name__+"_4").update_Data(list=item.getList(), selected=indexOfName)



    def changeLog(self):
        for group in self.listGroups:
            name= group.getName()
            if(name):
                namelist= group.getList()
                for x in range(len(self.log)):
                    for y in range(len(self.log[x])):
                        logelement= self.log[x][y][group.getTyp()]
                        if logelement in namelist:
                            self.log[x][y][group.getTyp()]=name


        self.controller.setLog(self.log)
        self.leaveMod()


    def getSettings(self):
        return self.settings


    def setSettings(self, settings):
        self.settings=settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getFrameByName(__name__+"_2").getSettings()

    def leaveMod(self):
       self.controller.showFrame("frame_modules")
       self.currentGroup=0
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

 

