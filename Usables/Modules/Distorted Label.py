from nltk.corpus.reader import wordnet
from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *

class module_distoredLabel(ModuleFiles):
    def __init__(self, controller):
        super().__init__(__class__,controller)
        self.settings = {"LevLowerEvents": 90,"LevLowerResources": 90,"occurrenceRatio":0.1,"eventResources":"org:resource", "eventTyp":"concept:name","maxEvents": 100,"maxRes":100}
        self.name = "Distorted Label"
        self.oneDes = "this programm checks The Event Names for similar but unequal Names "
        #TODO change 
        self.desc = "Distorted Labels describes a group of event attributes,that are "+\
        "unequal but similar to one another yet refer to one real live attribute"
        self.listGroups=[]

    def clean(self):
        self.baseClean()
        self.listGroups=[]

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
        eventList=getAllActivityAsDict(self.log)
        if(len(eventList)>int(self.settings["maxEvents"])):
            error_max=error()
            error_max.set(trace="global",desc="More Events than allowed",dictVal=len(eventList),errorModul=self)
            self.controller.addToErrorList([error_max])
            eventList=dict((k, eventList[k]) for k in(list(eventList)[:int(self.settings["maxEvents"])]))
        
        resList=getAllResourcesAsDict(self.log)
        if(len(resList)>int(self.settings["maxEvents"])):
            error_max=error()
            error_max.set(trace="global",desc="More Ressources than allowed",dictVal=len(resList),errorModul=self)
            self.controller.addToErrorList([error_max])
            resList=dict((k, resList[k]) for k in(list(resList)[:int(self.settings["maxRes"])])) 
        
        tupelListAc=levinRatio(eventList,int(self.settings["LevLowerEvents"]), maxRatio=float(self.settings["occurrenceRatio"]))
        tupleListWN= matchWordnet(eventList)
        for el in tupleListWN:
            if (el not in tupelListAc):
                tupelListAc.append(el) 
        groupListAc= createGroups(tupelListAc,self.settings["eventTyp"])
        
        tupelListRe=tokenRatio(getAllResourcesAsDict(self.log),int(self.settings["LevLowerResources"]),maxRatio=float(self.settings["occurrenceRatio"]))
        groupListRe= createGroups(tupelListRe,self.settings["eventResources"])
        self.listGroups=groupListAc+groupListRe
        self.addToErrorList(self.listGroups)
        self.leaveMod()


    def addToErrorList(self, list):
        modErrorList= []
        for group in list:
            error_el = error()
            error_el.set(trace="Global",desc="Distored Label: "+ group.getList()[0],dictVal=group.getList()[0],dictkey=group.getTyp(), classInfo=0,errorModul=self)
            error_fix= error()
            error_fix.set(trace="Global",desc="proposed Correct Label: "+group.getList()[1],dictVal=[group.getList()],parent=error_el,dictkey=group.getTyp(), classInfo=0,errorModul=self, autoRepair=True)
            modErrorList.append(error_el)
            modErrorList.append(error_fix)
        self.controller.addToErrorList(modErrorList)
       
