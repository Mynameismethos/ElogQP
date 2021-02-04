import internalModules.objects as objects
import internalModules.compare as compare
import threading
import datetime
from typing import DefaultDict
#TODO change name
#TODO Change Desc

class module_CollateralEvents():
    def __init__(self, controller):
        self.controller = controller
        #TODO change
        self.name = "Collateral Events"
        self.oneDes = "this programm checks for Collateral Events"
        self.desc = ""
        self.log = None
        #EXAMPLE FOR LISTS
        self.listGroups = []
        self.currentGroup = int(0)
        self.started=False
        ## Settings
        self.settings = {"eventTime": "time:timestamp",
                         "eventTyp": "concept:name",
                         "String Seperator": "//://",
                         "delta Time":300,
                         "minimum appearances" : 20}


        #TODO IMPLEMENT
        # EXAMPLE
    def createFrames(self):
        #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Search for Collateral Events", button1_command =99, button2_text="Go To Next Module", button2_command =90)
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
            thread = threading.Thread(target=self.searchAlg, args=())
            thread.daemon = True
            thread.start()
            self.controller.getActiveModFrame(__class__).set_Widgets_Visible(button2="yes")

    def searchAlg(self):
        eventTime = self.settings["eventTime"]
        groupList = []
        groupDict = DefaultDict (int)
        eventTyp = self.settings["eventTyp"]
        for x in range(len(self.log)):
            traceList = sorted(self.log[x]._list, key=lambda x: x[eventTime])
            g=objects.Group([traceList[0][eventTyp]])
            g.set(trace=x)
            maxtime=datetime.timedelta(seconds=int(self.settings["delta Time"]))
            zeroTime=datetime.timedelta(seconds=0)
            for y in range(len(traceList)-1):
                delta_t=traceList[y+1][eventTime]-traceList[y][eventTime]
                if(delta_t<= maxtime and delta_t > zeroTime):
                    g.getList().append(traceList[y+1][eventTyp]) 
                else:
                    if(len(g.getList())>1):
                        groupList.append(g)
                    g=objects.Group([traceList[y+1][eventTyp]])
                    g.set(trace=x)
            if(len(g.getList())>1):
               groupList.append(g)

        for n in groupList:
            n.listNames.sort()
            n.name= self.settings["String Seperator"].join(n.listNames)

            groupDict[n.name]+=1
    

        for key, value in groupDict.items():
            if(value<int(self.settings["minimum appearances"])):
                liste=key.split(self.settings["String Seperator"])
                for n in reversed(groupList):
                    if (n.listNames==liste):
                        groupList.remove(n)


        #TODO set Group Names
        modErrorList = self.createErrorList(groupList)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

    def preferences(self,dictList):
        groupList = []
        #find larges item and longest
        dictList.sort(key=lambda s : len(s[0]), reverse=True)
        dictList.sort(key=lambda s : s[1], reverse=True)
        while(dictList):
            element = dictList[0][0]
            g= objects.Group(dictList[0][0])
            #TODO fill G
            groupList.append(g)
            
            for i in reversed(range(len(dictList))):
                if (any(el in dictList[i][0] for el in element)):
                        dictList.pop(i)

                

        return groupList

    def createErrorList(self, groupList):
        modErrorList = []
        errorDict={}
        for element in groupList:            
            if(element.getName() not in errorDict):
                error_p=objects.error()
                error_p.set(trace="global", desc="Parent Container Colleteral Event", dictVal=element.getName(), errorModul=self)
                modErrorList.append(error_p)
                errorDict[element.getName()]=error_p
            parent=errorDict[element.getName()]

            error_form = objects.error()
            error_form.set(trace=element.getTrace(),parent=parent, desc="Colleteral Event", dictVal=element.getName(), errorModul=self)
            modErrorList.append(error_form)


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
