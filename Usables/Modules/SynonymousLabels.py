from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *


#TODO Comment Module
class module_SynonymousLabels(ModuleFiles):
    def __init__(self, controller):
        super().__init__(__class__,controller)

        self.name = "Synonymous Labels"
        self.oneDes = "this module checks The Event Names for SynonymousLabels"
        self.desc = "Synonymous Labels describes a pair of Events that describe the same process, though have a different name attribute"
        ## Settings
        self.settings = {"maxEvents": 50, "eventTyp":"concept:name", "position Delta": 3, "time (min) Delta": 10,"time (sec) Delta": 0}



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
        weightedPairs = self.filterWithWeight(notConnectedPairs)
        


        modErrorList = self.createErrorList(weightedPairs)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()


    def filterWithWeight(self, pairList):
        filteredList=[]
        for entry in pairList:
            # check if at similiar positions
            avr_pos_one= getAveragePosition(self.log,entry[0])
            avr_pos_two= getAveragePosition(self.log,entry[1])
            #compare if within bounds continue
            if(abs(avr_pos_one-avr_pos_two)<float(self.settings["position Delta"])):
                # check if similiar length
                avr_time_one= getAvereageLength(self.log,entry[0])
                avr_time_two= getAvereageLength(self.log,entry[1])
                #compare if within bounds
                if(abs(avr_time_one-avr_time_two)<int(self.settings["time (min) Delta"])*60+int(self.settings["time (sec) Delta"])):    
                    # check if uses similiar resources 
                    used_res_one=getUsedResources(self.log,entry[0])
                    used_res_two=getUsedResources(self.log,entry[1])
                    if(isSimilarResources(used_res_one,used_res_two)):
                        filteredList.append(entry)

        return filteredList


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
        

        

    def createErrorList(self, liste):
        modErrorList = []
        for element in liste:
            error_el = error()
            error_el.set(trace="global", desc="possible Synonymous Labels", dictVal= [element], errorModul=self)
            modErrorList.append(error_el)
        return modErrorList

 
  
