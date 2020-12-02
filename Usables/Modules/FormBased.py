from internalModules.ModuleFiles import ModuleFiles
from internalModules.compare import *
from internalModules.objects import *
from typing import DefaultDict



class module_FormBased(ModuleFiles):
    """
    Module to find Form-based Event Capture in a set Eventlog
    """
    def __init__(self, controller):
        super().__init__(__class__,controller)

        self.name = "Form-based Event Capture"
        self.oneDes = "this module checks For Form-based Event Capture through time data"
        self.desc = "Form-based events describe a cluster of Events, that are recorded together, but as individual Events"
        ## Settings
        self.settings = {"eventTime": "time:timestamp",
                         "eventTyp": "concept:name",
                         "String Seperator": "//://",
                         "minimum appearances" : 20}


    def clean(self):
        """ 
        Function to reset the Variables changed during the runtime
        
        Specific Variables in this Module:
            None
        """
        self.baseClean()

    def createFrames(self):
        """ konfiguring the frames in reversed order"""
        #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(
            modController=self, previous=True, title=self.getName(), button1_text="Search for Events from Forms", button1_command=99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True, previous=True,
                                                      title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(
            modController=self, next=True, previous=None, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

   
    def searchAlg(self):
        """ 
        starting point for the main algorithm of the module
        """
        eventTime = self.settings["eventTime"]
        groupList = []
        groupDict = DefaultDict (int)
        eventTyp = self.settings["eventTyp"]
        
        """ creating lists of events that are called simultaneously """
        for x in range(len(self.log)):
            blue = self.log[x]

            traceList = sorted(blue._list, key=lambda x: x[eventTime])
            x=traceList[0]
            g=[]
            for y in range(len(traceList)-1):
                if(traceList[y][eventTime]!=x[eventTime]):
                    if(len(g)>1):
                        groupList.append(g)
                    g=[]
                    x=traceList[y]
                    g.append(x[eventTyp])
                elif(traceList[y][eventTime]==x[eventTime]):
                    g.append(traceList[y][eventTyp])


        """ sorting list alphabetically"""
        for x in range(len(groupList)):
            groupList[x] = sorted(groupList[x])

        """ creating all Permutations of the groups and weighing those based on appearance"""
        while(groupList):
            element=groupList[0]
            allper=all_Subgroups(element,2)
            f=groupList.count(element)
            for x in allper:
                name= self.settings["String Seperator"].join(x)
                groupDict[name]+=f
            groupList=list(filter((element).__ne__, groupList))
        print("No more elements")
        dictList=[]
        """ filtering rare groups """
        for key, value in groupDict.items():
            if(value>=int(self.settings["minimum appearances"])):
                dictList.append([key.split(self.settings["String Seperator"]),value])
              
        groupList=self.preferences(dictList)

        modErrorList = self.createErrorList(groupList)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

    def preferences(self,dictList):
        """
        function to extract the specific forms
        """
        groupList = []
        #find larges item and longest
        dictList.sort(key=lambda s : len(s[0]), reverse=True)
        dictList.sort(key=lambda s : s[1], reverse=True)
        while(dictList):
            element = dictList[0][0]
            g= Group(dictList[0][0])

            groupList.append(g)
            
            for i in reversed(range(len(dictList))):
                if (any(el in dictList[i][0] for el in element)):
                        dictList.pop(i)

                

        return groupList

    def createErrorList(self, dictList):
        """
        function create an errorstructur of valid errors for the found issues with multible parent containers
        """
        modErrorList = []
        eventTyp = self.settings["eventTyp"]
        for element in dictList:
            #Create Group Error Object
            error_form = error()
            error_form.set(trace="global", desc="FormBased", dictVal=element.getName(
            ), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_form)
            #Create Event Error
            errorDict = {}           
            #Create Instance Error
            elementSet=set(element.getList())
            for x in range(len(self.log)):
                eventlist= [u[eventTyp] for u in self.log[x]]
                elementsinTrace=sorted(list(elementSet.intersection(eventlist)))
                if(elementsinTrace):
                    if(self.settings["String Seperator"].join(elementsinTrace) not in errorDict):
                         error_parent = error()
                         error_parent.set(trace="global", desc="Traces with corresponding Part of Form",
                                parent=error_form, dictVal=self.settings["String Seperator"].join(elementsinTrace), errorModul=self)
                         errorDict[self.settings["String Seperator"].join(elementsinTrace)] = error_parent
                         modErrorList.append(error_parent)

                    parent=errorDict[self.settings["String Seperator"].join(elementsinTrace)]
                    error_child = error()
                    error_child.set(
                        trace=x, parent=parent, dictVal="", dictkey=eventTyp, errorModul=self)
                    modErrorList.append(error_child)


        return modErrorList



