from internalModules.ModuleFiles import ModuleFiles
from internalModules.objects import *

from typing import DefaultDict


class module_timeTravel(ModuleFiles):
    """
    Module to find Inadvertent Time Travel in a set Eventlog
    """
    def __init__(self, controller):
        super().__init__(__class__,controller)
        self.settings = {"String Seperator": "//://", "checkRatio": 0.05,"eventTyp":"concept:name", "eventTime" :"time:timestamp"}
        self.name = "Inadvertent Time Travel"
        self.oneDes = "this module checks for the Inadvertent Time Travel Issue"
        self.desc = "Inadvertent time travel describes a case in which an event that has a strong temporal ordering" +\
        ", breaks this order. Thereby creating paths that do not exist in the underlying process"
        
        #EXAMPLE FOR LISTS
        self.occurence = DefaultDict(int)
        self.listGroups = []


    def clean(self):
        """ 
        Function to reset the Variables changed during the runtime
        
        Specific Variables in this Module:
            listGroups
        """
        self.baseClean()
        self.listGroups = []

    def createFrames(self):
        """ konfiguring the frames in reversed order"""
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


    def searchAlg(self):
        """ 
        starting point for the main algorithm of the module
        """
        eventTyp = self.settings["eventTyp"]
        eventTime = self.settings["eventTime"]
        self.occurence = DefaultDict(int)
        """ create Ordering of Events"""
        for x in range(len(self.log)):
            trace = sorted(self.log[x]._list, key=lambda b: b[eventTime])
            for y in range(0, len(trace)-1):
                elOne = trace[y][eventTyp]
                elTwo = trace[y+1][eventTyp]
                self.occurence[elOne+self.getSettings()
                               ["String Seperator"]+elTwo] += 1
        """find orderings that appear rarely """
        tupellist = self.findRare()
        
        for t in tupellist:
            """find Occurence of this Tupel"""
            self.listGroups.extend(self.findTraceOfTupel(t))
        """Create ErrorGroups""" 
        self.createErrorList(self.listGroups)
        self.leaveMod()

    def findRare(self):
        """ function to find rare Orderings"""
        tupellist = []
        ratio= float(self.settings["checkRatio"])
        while self.occurence :
            """ 
            1) get an ordering of Activitys
            2) get the oppsosite order of Activitys
            """
            key=list(self.occurence)[0]
            elOne,elTwo=key.split(self.settings["String Seperator"])
            key_opposite=elTwo+self.settings["String Seperator"]+elOne
            if key_opposite in self.occurence:
                """ mark as possible error if both orderings exist but one is very rare"""
                if(self.occurence[key]/ self.occurence[key_opposite] < ratio):
                    tupellist.append(tupel(elOne, elTwo, self.occurence[key]/ self.occurence[key_opposite]))
                elif(self.occurence[key_opposite]/ self.occurence[key] < ratio):
                    tupellist.append(tupel(elTwo, elOne, self.occurence[key_opposite]/ self.occurence[key]))
            """ remove both elements from list""" 
            self.occurence.pop(key,None)
            self.occurence.pop(key_opposite,None)

        return tupellist

    def findTraceOfTupel(self, tupel):
        """ function to find all traces in which a specific ordering of Events exist"""
        eventTyp = self.settings["eventTyp"]
        eventTime = self.settings["eventTime"]
        list = []
        for x in range(len(self.log)):
            trace = sorted(self.log[x]._list, key=lambda b: b[eventTime])
            for y in range(0, len(trace)-1):
                if(trace[y][eventTyp] == tupel.one):
                    if(trace[y+1][eventTyp] == tupel.two):
                        gOne = Group([tupel.one,tupel.two])
                        gOne.set(trace=x, value=str(trace[y][eventTime])+"----"+str(trace[y+1][eventTime]), typ=eventTime)
                        list.append(gOne)


                    
        return list

    def createErrorList(self, list):
        """
        function to turn a list of found issues into valid error codes
        """
        modErrorList = []
        for element in list:
            c_error = error()
            c_error.set(trace=element.getTrace(),desc="Time Travel:"+element.getList()[0]+" and "+element.getList()[1], dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(c_error)
        self.controller.addToErrorList(modErrorList)
