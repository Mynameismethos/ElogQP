from internalModules.ModuleFiles import ModuleFiles
from internalModules.logwork import *
from internalModules.compare import *
from internalModules.objects import *
 

class module_Polluted_Labels(ModuleFiles):
    """
    Module to find Polluted Label in a set Eventlog
    """
    def __init__(self, controller):
        super().__init__(__class__,controller)
        self.name = "Polluted Label"
        self.oneDes = "this module checks The Event Names for Attributes in the Event name "
        self.desc = "Polluted Label describes Events whos name Attribute is a composite of a fixed and variable part."
        self.listGroups = []
        ## Settings
        self.settings = {"minEventNamelength": 6,"MinRes" : 95,"min Occurence": 6, "eventTyp":"concept:name"}

    def clean(self): 
        """ 
        Function to reset the Variables changed during the runtime
        
        Specific Variables in this Module:
            listGroups
        """
        self.baseClean()
        self.listGroups=[]
     
     
    def createFrames(self):
        """ konfiguring the frames in reversed order"""
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
        """ 
        starting point for the main algorithm of the module
        """
        eventNames=getAllActivityAsList(self.log)
        """ create all pairwise differen permutations"""
        subGroups=all_Subgroups(eventNames,2,maxlen=2)
        popped=subGroups.pop()
        while(popped):
            sub=largestSubstring(popped)
            """ check length of substring"""
            if(len(sub)>int(self.settings["minEventNamelength"])):
                print(sub)
                g=Group([])
                g.value=sub
                value=0
                """ count how often the substring appears in the list of Activitys"""
                for eName in reversed(eventNames):
                    if(sub in eName):
                        value+=1
                if(value>int(self.settings["min Occurence"])):
                    """ remove Activtys that contain the substring"""
                    for eName in reversed(eventNames):
                        if(sub in eName):
                            eventNames.remove(eName)
                    self.listGroups.append(g)
                    subGroups=all_Subgroups(eventNames,2,maxlen=2)
            popped=None
            if(subGroups):
                popped=subGroups.pop()
            """ contine until subGroups is empty"""
                   

        """ create errors with the substrings that have been removed"""
        modErrorList=self.createErrorList(self.listGroups)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()


    def createErrorList(self, list):
        """
        function to turn a list of found issues into valid error codes
        """
        modErrorList = []
        for element in list:
            p_error = error()
            p_error.set(trace="global",dictVal=element.getValue(), desc= "Polluted Labels",dictkey=self.settings["eventTyp"], classInfo=0,errorModul=self)
            modErrorList.append(p_error)
            for x in range(len(self.log)):
                eventlist= [u[self.settings["eventTyp"]] for u in self.log[x]]
                for eName in eventlist:
                    if(element.getValue() in eName):
                        c_error= error()
                        c_error.set(trace=x,parent=p_error,dictVal=eName, desc= "Polluted Labels", dictkey=self.settings["eventTyp"], classInfo=0,errorModul=self)
                        modErrorList.append(c_error) 
        return modErrorList
