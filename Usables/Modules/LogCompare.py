from collections import defaultdict
import datetime
from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *
from internalModules.loadLog import *

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
        self.settings = {"Check Empty Fields" : 1, "Check Missing Events" : 1, "Check Skipping Events" : 1, "earliest Date": "2000-01-01","latest Date":"2030-01-01"}
        #self.settings["latest Date"]=datetime.datetime.now().strftime("%Y-%m-%d")
        self.correctedLog =None
        self.LogNames=getAllLogs()


        #TODO IMPLEMENT set Parameter to  start
    def clean(self):
        self.baseClean()

    def createFrames(self):
        #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Compare Logs", button1_command =99, button2_text="Go To Next Module", button2_command =90)
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
            self.setTime()
            for counter in range(len(self.log)):
                trace=self.log[counter]
                for pos in range(len(trace)):
                    event=trace[pos]
                    if(event[name] ==""):
                        surround=[]
                        surround.append(trace[pos-1][name]) if(pos>0) else surround.append("")
                        surround.append(trace[pos+1][name]) if(pos<len(trace)-1) else surround.append("")
                        g= Group(surround)
                        g.set(name="Missing Event Name",typ=name,trace=counter,value=10)
                        modErrorList.append(g)
                    if(event["org:resource"] ==""):
                        g= Group([event[name]])
                        g.set(name="Missing Event Res",trace=counter,typ="org:resource",value=11)
                        modErrorList.append(g)
                    if(not self.validateDate(event["time:timestamp"])):
                        g= Group([event[name]])
                        g.set(name="Wrong Timestamp",trace=counter,typ="time:timestamp",value=12)
                        modErrorList.append(g)


        if(self.correctedLog):
            # find EventNames
            if(int(self.settings["Check Missing Events"])==1):
                Events_BL=getAllActivityAsList(self.log)
                Events_GL=getAllActivityAsList(self.correctedLog)
                for event in Events_BL:
                    if(event not in Events_GL):
                        g= Group([event])
                        g.set(name="New Event in Log",typ=name,trace="Global",value=20)
                        modErrorList.append(g)

                for event in Events_GL:
                    if(event not in Events_BL):
                        g= Group([event])
                        g.set(name="Missing Event in Log",typ=name,trace="Global",value=21)
                        modErrorList.append(g)

        
            #check if skipping EVents
            if(int(self.settings["Check Skipping Events"])==1):
                ordering=self.getEventOrdering()
                for index in range(len(self.log)):
                    trace= self.log[index]
                    for count in range(len(trace)-1):
                        if(trace[count][name]!="" and trace[count+1][name]!=""):
                            if(trace[count][name] in ordering):
                                if(trace[count+1][name] not in ordering[(trace[count][name])]):

                                    surround=[]
                                    surround.append(trace[count][name]) if(count>0) else surround.append("start")
                                    surround.append(trace[count+1][name]) if(count<len(trace)-1) else surround.append("end")
                                    g= Group(surround)
                                    g.set(name="Missing Event",typ=name,trace=index,value=30)
                                    modErrorList.append(g)
                            else:
                                g= Group([trace[count][name]])
                                g.set(name="Missing Sources",typ=name,trace=index,value=31)
                                modErrorList.append(g)




        modErrorList = self.createErrorList(modErrorList)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()


    def callBack(self, actionNumber):
        super().callBack(actionNumber)
        if(actionNumber != 80,90,99):
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
        error_pEmpty=error()
        error_pEmptyEvents=error()
        error_pEmptyRes=error()
        error_pEmptyTime=error()
        error_pMissing=error()
        error_pSkipping=error()
        error_pEmpty.set(trace="Global",desc="Empty Fields",errorModul=self)
        error_pEmptyEvents.set(trace="Global",desc="Missing Event Name",parent=error_pEmpty,errorModul=self)
        error_pEmptyRes.set(trace="Global",desc="Missing Ressources",parent=error_pEmpty,errorModul=self)
        error_pEmptyTime.set(trace="Global",desc="Missing Time Data",parent=error_pEmpty,errorModul=self)
        error_pMissing.set(trace="Global",desc="Missing Events",errorModul=self)
        error_pSkipping.set(trace="Global",desc="Skipping Events",errorModul=self)

        if(int(self.settings["Check Empty Fields"])==1):
            modErrorList.append(error_pEmpty)
            modErrorList.append(error_pEmptyEvents)
            modErrorList.append(error_pEmptyRes)
            modErrorList.append(error_pEmptyTime)
        if(int(self.settings["Check Missing Events"])==1):
            modErrorList.append(error_pMissing)
        if(int(self.settings["Check Skipping Events"])==1):
            modErrorList.append(error_pSkipping)

        for element in list:
            error_el = error()
            switcher={
                10: error_pEmptyEvents,
                11: error_pEmptyRes,
                12: error_pEmptyTime,
                20: error_pMissing,
                21: error_pMissing,
                30: error_pSkipping,
                31: error_pSkipping,
                }
            parent=switcher.get(element.value,None)
            val= "---".join(element.getList())
            error_el.set(trace=element.getTrace(),desc=element.getName(),parent= parent, dictVal=val, dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_el)
            #TODO REMOVE
        if(modErrorList):self.controller.data.errorRate=2
        return modErrorList

    #@Override
    def setLog(self,log, button=None, name=None):
        self.correctedLog =log

    def setTime(self):
        self.startTime=datetime.datetime.strptime(self.settings["earliest Date"],"%Y-%m-%d")
        self.latestTime=datetime.datetime.strptime(self.settings["latest Date"],"%Y-%m-%d")

    def validateDate(self, date):
        if(not date): return False
        date=date.replace(tzinfo=None)
        if(self.startTime>date): return False
        if(self.latestTime<date): return False

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

            



    
  

