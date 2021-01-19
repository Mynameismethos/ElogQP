from typing import DefaultDict
import threading
import internalModules.logwork as logwork
#import internalModules.compare as compare
import internalModules.objects as objects
import uuid


class module_timeTravel():
    def __init__(self, controller):
        self.controller = controller
        #TODO change
        self.settings = {"String Seperator": "//://", "checkRatio": 0.05,"eventTyp":"concept:name", "eventTime" :"time:timestamp"}
        self.name = "Inadvertent Time Travel"
        self.oneDes = "this programm checks for the Inadvertent Time Travel Issue"
        self.desc = "The String Sperator musn´t be part of any Event Name"
        self.log = None
        self.visible=False
        #EXAMPLE FOR LISTS
        self.occurence = DefaultDict(int)
        self.listGroups = []
        self.currentGroup = int(0)

        #TODO IMPLEMENT
        # EXAMPLE
    def createFrames(self):
        #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(
            modController=self, previous=True, title=self.getName(), button1_text="Search for Time Travelers", button1_command=99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True, previous=True, title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(
            modController=self, next=True, previous=None, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

    #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher = {
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
        thread = threading.Thread(target=self.findTimeTravel, args=())
        thread.daemon = True
        thread.start()
        self.controller.getActiveModFrame(__class__).set_Widgets_Visible(button2="yes")

    def findTimeTravel(self):
        eventTyp = self.settings["eventTyp"]
        self.occurence = DefaultDict(int)
        for x in range(len(self.log)):
            for y in range(0, len(self.log[x])-1):
                elOne = self.log[x][y][eventTyp]
                elTwo = self.log[x][y+1][eventTyp]
                self.occurence[elOne+self.getSettings()
                               ["String Seperator"]+elTwo] += 1
        #Tupellist with pair with very rare Ordering
        tupellist = self.createTupels()
        
        for t in tupellist:
            #find Occurence of this Tupel
            self.listGroups.extend(self.findTraceOfTupel(t))
        #Create ErrorGroups 
        self.createErrorList(self.listGroups)
        self.leaveMod()

    def createTupels(self):

        tupellist = []
        ratio= float(self.settings["checkRatio"])
        while self.occurence :
            key=list(self.occurence)[0]
            elOne,elTwo=key.split(self.settings["String Seperator"])
            key_opposite=elTwo+self.settings["String Seperator"]+elOne
            if key_opposite in self.occurence:
                if(self.occurence[key]/ self.occurence[key_opposite] < ratio):
                    tupellist.append(objects.tupel(elOne, elTwo, self.occurence[key]/ self.occurence[key_opposite]))
                elif(self.occurence[key_opposite]/ self.occurence[key] < ratio):
                    tupellist.append(objects.tupel(elTwo, elOne, self.occurence[key_opposite]/ self.occurence[key]))
            
            self.occurence.pop(key,None)
            self.occurence.pop(key_opposite,None)

        return tupellist

    def findTraceOfTupel(self, tupel):
        eventTyp = self.settings["eventTyp"]
        eventTime = self.settings["eventTime"]
        list = []
        for x in range(len(self.log)):
            first = None
            second = None
            for y in range(0, len(self.log[x])):
                #not first only for Performance
                if(not first and self.log[x][y][eventTyp] == tupel.one):
                    first = y
                elif(first and self.log[x][y][eventTyp] == tupel.two):
                    second = y
                    #id = uuid.uuid4()
                    gOne = objects.Group(tupel.one)
                    #TODO One Error
                    #TODO make Tupel The Error Parent
                    gOne.set(event=first, trace=x, value=self.log[x][first][eventTime],
                             typ=eventTime)

                    gTwo = objects.Group(tupel.two)
                    gTwo.set(event=second, trace=x, value=self.log[x][second][eventTime],
                             typ=eventTime)
                    list.append(gOne)
                    list.append(gTwo)
        return list

    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error = objects.error()
            error.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error)
        self.controller.addToErrorList(modErrorList)

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
        self.log = None
        self.visible=False
    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self):
        self.settings = self.controller.getActiveModFrame(__class__).getCanvasAsDict()


    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getLog(self, log):
        self.log = log

    # def changeLog(self):
    #     updatedLog = self.log
    #     for case in self.listGroups:
    #         updatedLog[case.getName()]._list = case.getTrace()
    #     self.controller.setLog(updatedLog)
    #     self.clean()
    #     self.leaveMod()

    # def saveAndReorder(self, frame):
    #     canList = self.controller.getFrameByName(frame).getCanvasAsList()
    #     trace = self.listGroups[self.currentGroup].getTrace()
    #     for x in range(len(canList)):
    #         trace[x]["time:timestamp"] = canList[x]
    #     trace.sort(key=lambda x: x["time:timestamp"])
    #     self.listGroups[self.currentGroup].setTrace(trace)
    #     self.displayGroup(frame)

    # def displayPrev(self, frame):
    #     if(self.currentGroup > 0):
    #         self.currentGroup -= 1
    #         self.controller.getFrameByName(
    #             frame).set_Widgets_Visible(button2="yes")
    #         self.displayGroup(frame)
    #     else:  # removebutton
    #         self.controller.getFrameByName(
    #             frame).set_Widgets_Visible(button1="no")

    # def displayNext(self, frame):
    #     if(self.currentGroup < len(self.listGroups)-1):
    #         self.currentGroup += 1
    #         self.controller.getFrameByName(
    #             frame).set_Widgets_Visible(button1="yes")
    #         self.displayGroup(frame)
    #     else:  # removebutton
    #         self.controller.getFrameByName(
    #             frame).set_Widgets_Visible(button2="no")

    # def displayGroup(self, frame):
    #     trace = self.listGroups[self.currentGroup].getTrace()
    #     highlightList = self.listGroups[self.currentGroup].getList()
    #     self.controller.getFrameByName(frame).update_Data(
    #         canList=trace, highlight=highlightList)
