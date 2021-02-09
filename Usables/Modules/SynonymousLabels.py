from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *

#TODO change name
#TODO Change Desc

class module_SynonymousLabels(ModuleFiles):
    def __init__(self, controller):
        super().__init__(__class__,controller)
        #TODO change
        self.name = "Not Ready Synonymous Labels"
        self.oneDes = "this programm checks The Event Names for SynonymousLabels"
        self.desc = ""
        ## Settings
        self.settings = {"maxEvents": 50, "eventTyp":"concept:name"}


        #TODO IMPLEMENT set Parameter to  start
    def clean(self):
        self.baseClean()

        # EXAMPLE
    def createFrames(self):
        #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Search for SynonymousLabels", button1_command =99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= True,title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())



    def searchAlg(self):
        eventList=getAllActivityAsList(self.log)
        if(len(eventList)>int(self.settings["maxEvents"])):
            error_max=error()
            error_max.set(trace="global",desc="More Events than allowed",dictVal=len(eventList),errorModul=self)
            self.controller.addToErrorList([error_max])
            eventList=eventList[:int(self.settings["maxEvents"])]

        notConnectedPairs=self.findPairs(eventList)
        for entry in notConnectedPairs:
            pass
            # check if similiar length
            # check if at similiar positions
            # check if uses similiar resources 
            # weighing stuff is gonna suck


        modErrorList = self.createErrorList([])
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()


    def findPairs(self,eventList):
        subT=all_Subgroups(eventList,2,maxlen=2)
        pairList=[]
        eventTyp= self.settings["eventTyp"]
        
        for t in subT:
            found=False
            for trace in self.log:
                traceEvents= [u[eventTyp] for u in trace]
                if(t[0] in traceEvents and t[1] in traceEvents):
                    found=True
                    break
            if(not found):
                pairList.append(t)
        return pairList
        

        

   #TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error = error()
            error.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error)
        return modErrorList

 
  
