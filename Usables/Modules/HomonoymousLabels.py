from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *


class module_HomonymousLabels(ModuleFiles):
    def __init__(self, controller):
        super().__init__(__class__,controller)

        self.name = " Homonymous Label"
        self.oneDes = "this programm checks for Homonymous Labels"
        self.desc = ""
        #EXAMPLE FOR LISTS
        ## Settings
        self.settings = {"checkRatio": 0.05,"eventTyp":"concept:name", "eventTime" :"time:timestamp"}

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
        repeatedEvents = self.getMultiShowEvents()
        orderOfEvents={}
        modErrorList=[]
        eventTyp=self.settings["eventTyp"]
        error_pa=error()
        error_pa.set(trace="global",desc="Parent for Homonymous Labels", dictkey=eventTyp, classInfo="", errorModul=self)
        modErrorList.append(error_pa)
        for event in repeatedEvents:
            orderOfEvents[event]=self.getOrderOfEvent(event)

        for eventName in orderOfEvents:
            currentDict=orderOfEvents[eventName]
            for key in currentDict[0]:
                if(currentDict[0][key]>0 and currentDict[1][key]>0):
                    ratio=1
                    if(currentDict[0][key]>currentDict[1][key]):
                        ratio=currentDict[1][key]/currentDict[0][key]
                    elif(currentDict[0][key]<currentDict[1][key]):
                        ratio=currentDict[0][key]/currentDict[1][key]
                    if(ratio<float(self.settings["checkRatio"])):
                        error_el=error()
                        error_el.set(trace="global",desc="possible Homonymous Label: "+eventName,parent=error_pa, dictVal=eventName, dictkey=eventTyp, classInfo="", errorModul=self)
                        modErrorList.append(error_el)
                        break

            
        
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

    def getOrderOfEvent(self, eventName):
        eventTime=self.settings["eventTime"]
        eventTyp=self.settings["eventTyp"]

        globalOrderBefore=getAllActivityAsDict(self.log)
        globalOrderAfter=getAllActivityAsDict(self.log)
        for key in globalOrderBefore:
            globalOrderBefore[key]=0
            globalOrderAfter[key]=0

        for x in range(len(self.log)):
            trace = sorted(self.log[x]._list, key=lambda b: b[eventTime])
            timesOfEvent=[]
            for event in trace:
                if(event[eventTyp]==eventName):
                    timesOfEvent.append(event[eventTime])
            for time in timesOfEvent:
                for event in trace:
                    if(event[eventTime]<time):
                        globalOrderBefore[event[eventTyp]]+=1
                    elif(event[eventTime]>time):
                        globalOrderAfter[event[eventTyp]]+=1

        return [globalOrderBefore,globalOrderAfter]
                    

   
    def getMultiShowEvents(self):
        multiOccurrenceOfEvent=[]
        eventTyp=self.settings["eventTyp"]
        for globalEvent in getAllActivityAsList(self.log):
            for x in range(len(self.log)):
                trace = self.log[x]._list
                counter=0
                for localEvent in trace:
                    if(localEvent[eventTyp]==globalEvent):counter+=1
                if(counter>1):
                    multiOccurrenceOfEvent.append(globalEvent)
                    break
                counter=0
        return multiOccurrenceOfEvent

    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error_el = error()
            error_el.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_el)
        return modErrorList

 
  

