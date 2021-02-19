from collections import defaultdict
import datetime
from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *
from internalModules.loadLog import *
#TODO change name
#TODO Change Desc

class module_LogCompare(ModuleFiles):
    def __init__(self, controller):
        super().__init__(__class__,controller)
        #TODO change
        self.name = "Log Compare"
        self.oneDes = "this programm compares an uncleaned event log to an processed Event log"
        self.desc = ""
        #EXAMPLE FOR LISTS
        self.listGroups = []
        self.currentGroup = int(0)
        ## Settings
        self.settings = {"Check Empty Fields" : 1, "Check Missing Events" : 1, "Check Skipping Events" : 1, "Date Format": "%Y-%m-%d'"}
        self.correctedLog =None
        self.LogNames=getAllLogs()


        #TODO IMPLEMENT set Parameter to  start
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
        #Import Eventlog
        self.controller.createModFrame(1,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), list=self.LogNames, button1_text="Load corrected Log", button1_command=70)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())



    def searchAlg(self):
        modErrorList=[]
        time="time:timestamp"
        name="concept:name"

          # check Empty fields 
        if(int(self.settings["Check Empty Fields"])==1):
            for counter in range(len(self.log)):
                test1=self.log[counter]._list
                if(self.log[counter]._list[name] ==""):
                    error_el=error()
                    error_el.set(trace=counter,desc="missing Event Name", dictkey=name, errorModul=self)
                    modErrorList.append(error_el)
                if(self.log[counter]._list["org:resource"] ==""):
                    error_el=error()
                    error_el.set(trace=counter,desc="missing Resources", dictkey="org:resource", errorModul=self)
                    modErrorList.append(error_el)
                if(not self.validateDate(self.log[counter]._list["time:timestamp"])):
                    error_el=error()
                    error_el.set(trace=counter,desc="Wrong Timestamp", dictkey="time:timestamp", errorModul=self)
                    modErrorList.append(error_el)


        if(self.correctedLog):
            # find EventNames
            if(int(self.settings["Check Missing Events"])==1):
                Events_BL=getAllActivityAsList(self.log)
                Events_GL=getAllActivityAsList(self.correctedLog)
                for event in Events_BL:
                    if(event not in Events_GL):
                        error_el=error()
                        error_el.set(trace="Global",desc="New Event in Log",dictVal=event, dictkey=name, errorModul=self)
                        modErrorList.append(error_el)

                for event in Events_GL:
                    if(event not in Events_BL):
                        error_el=error()
                        error_el.set(trace="Global",desc="Missing Event in Log",dictVal=event, dictkey=name, errorModul=self)
                        modErrorList.append(error_el)
                        
        
            #check if skipping EVents
            if(int(self.settings["Check Skipping Events"])==1):
                ordering=self.getEventOrdering()
                for trace in self.log:
                    for count in range(len(trace)-1):
                        if(trace[count][name] in ordering):
                            e1 = trace[count+1][name]
                            e2= ordering[(trace[count][name])]
                            if(trace[count+1][name] not in ordering[(trace[count][name])]):
                                error_el=error()
                                error_el.set(trace="TODO",desc="Missing Event between Events",dictVal=trace[count][name]+"---"+trace[count+1][name], dictkey=name, errorModul=self)
                                modErrorList.append(error_el)
                        else:
                            error_el=error()
                            error_el.set(trace="TODO",desc="Missing Sources",dictVal=trace[count][name], dictkey=name, errorModul=self)
                            modErrorList.append(error_el)



        #modErrorList = self.createErrorList([])
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()


    def callBack(self, actionNumber):
        super().callBack(actionNumber)
        #NOT 80,90,99
        switcher={
            70: lambda: self.importLog(),
                }
        switcher.get(int(actionNumber.get()), lambda: print("Wrong Action"))()

    def importLog(self):
        pos=self.controller.getActiveModFrame(__class__).getSelected()
        logName= self.LogNames[pos[0]] #get name from Screen
        loadLogByName(self, logName, None)
        pass

   #TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error_el = error()
            error_el.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_el)
        return modErrorList

    def setLog(self,log, button=None, name=None):
        self.correctedLog =log

    def validateDate(self, date):
        try:
            datetime.strptime(date, self.settings["Date Format"])
        except ValueError:
            return False
        return True

    def getEventOrdering(self):
        orderdDict=defaultdict (set)
        time="time:timestamp"
        name="concept:name"
        
        for trace in self.correctedLog:
            prevTime=None
            count=0
            target=[]
            source=[]
            for count in range(len(trace)):
                if(source):
                    if(prevTime != trace[count][time]):
                        if(target):
                            for so in source:
                                for ta in target:
                                    orderdDict[so[name]].add(ta[name])
                            if(len(target)>1):
                                for ta in target:
                                    for ta_in in target:
                                        orderdDict[ta[name]].add(ta_in[name])
                            source=target
                            target=[]
                    target.append(trace[count])

                else:
                    source=[trace[count]]
                prevTime=trace[count][time]
            for so in source:
                for ta in target:
                    orderdDict[so[name]].add(ta[name])
            if(len(target)>1):
                for ta in target:
                    for ta_in in target:
                        orderdDict[ta[name]].add(ta_in[name])
                
        return orderdDict

            



    
  

