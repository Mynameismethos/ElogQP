from internalModules.ModuleFiles import ModuleFiles
import internalModules.objects as objects
import internalModules.compare as compare
import internalModules.logwork as logwork
import threading


class module_Polluted_Labels(ModuleFiles):
    def __init__(self, controller):
        self.setup(__class__,controller)
        #TODO change
        self.name = "Polluted Labels"
        self.oneDes = "this programm checks The Event Names for Attributes in the Event name "
        self.desc = ""
        self.listGroups = []
        ## Settings
        self.settings = {"minEventNamelength": 6,"MinRes" : 95,"min Occurence": 10, "eventTyp":"concept:name"}

    def clean(self): 
        self.baseClean()
        self.listGroups=[]
     
     
    def createFrames(self):
 #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Search for Polluted Labels", button1_command =99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= True,title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

 
    def searchAlg(self):
        eventNames=logwork.getAllActivityAsList(self.log)
        subGroups=compare.all_Subgroups(eventNames,2,maxlen=2)
        popped=subGroups.pop()
        while(popped):
            sub=compare.largestSubstring(popped)
            if(len(sub)>int(self.settings["minEventNamelength"])):
                print(sub)
                g=objects.Group([])
                g.value=sub
                value=0
                for eName in reversed(eventNames):
                    if(sub in eName):
                        value+=1
                if(value>int(self.settings["min Occurence"])):
                    for eName in reversed(eventNames):
                        if(sub in eName):
                            eventNames.remove(eName)
                    self.listGroups.append(g)
                    subGroups=compare.all_Subgroups(eventNames,2,maxlen=2)
            popped=None
            if(subGroups):
                popped=subGroups.pop()
                   


        modErrorList=self.createErrorList(self.listGroups)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

   #TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            p_error = objects.error()
            p_error.set(trace="global",dictVal=element.getValue(), dictkey=self.settings["eventTyp"], classInfo=0,errorModul=self)
            modErrorList.append(p_error)
            for x in range(len(self.log)):
                eventlist= [u[self.settings["eventTyp"]] for u in self.log[x]]
                for eName in eventlist:
                    if(element.getValue() in eName):
                        c_error= objects.error()
                        c_error.set(trace=x,parent=p_error,dictVal=eName, dictkey=self.settings["eventTyp"], classInfo=0,errorModul=self)
                        modErrorList.append(c_error) 
        return modErrorList
