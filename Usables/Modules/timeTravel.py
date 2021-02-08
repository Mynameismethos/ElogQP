from internalModules.ModuleFiles import ModuleFiles
from internalModules.objects import *

from typing import DefaultDict


class module_timeTravel(ModuleFiles):
    def __init__(self, controller):
        self.setup(__class__,controller)
        self.settings = {"String Seperator": "//://", "checkRatio": 0.05,"eventTyp":"concept:name", "eventTime" :"time:timestamp"}
        self.name = "Inadvertent Time Travel"
        self.oneDes = "this programm checks for the Inadvertent Time Travel Issue"
        self.desc = "The String Sperator musn´t be part of any Event Name"
        
        #EXAMPLE FOR LISTS
        self.occurence = DefaultDict(int)
        self.listGroups = []


    def clean(self):
       self.baseClean()
       self.listGroups = []

    def createFrames(self):
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
        eventTyp = self.settings["eventTyp"]
        self.occurence = DefaultDict(int)
        for x in range(len(self.log)):
            for y in range(0, len(self.log[x])-1):
                elOne = self.log[x][y][eventTyp]
                elTwo = self.log[x][y+1][eventTyp]
                self.occurence[elOne+self.getSettings()
                               ["String Seperator"]+elTwo] += 1
        #Tupellist with pair with very rare Ordering
        tupellist = self.findRare()
        
        for t in tupellist:
            #find Occurence of this Tupel
            self.listGroups.extend(self.findTraceOfTupel(t))
        #Create ErrorGroups 
        self.createErrorList(self.listGroups)
        self.leaveMod()

    def findRare(self):

        tupellist = []
        ratio= float(self.settings["checkRatio"])
        while self.occurence :
            key=list(self.occurence)[0]
            elOne,elTwo=key.split(self.settings["String Seperator"])
            key_opposite=elTwo+self.settings["String Seperator"]+elOne
            if key_opposite in self.occurence:
                if(self.occurence[key]/ self.occurence[key_opposite] < ratio):
                    tupellist.append(tupel(elOne, elTwo, self.occurence[key]/ self.occurence[key_opposite]))
                elif(self.occurence[key_opposite]/ self.occurence[key] < ratio):
                    tupellist.append(tupel(elTwo, elOne, self.occurence[key_opposite]/ self.occurence[key]))
            
            self.occurence.pop(key,None)
            self.occurence.pop(key_opposite,None)

        return tupellist

    def findTraceOfTupel(self, tupel):
        eventTyp = self.settings["eventTyp"]
        eventTime = self.settings["eventTime"]
        list = []
        for x in range(len(self.log)):
            first = None
            second = None
            for y in range(0, len(self.log[x])):
                #not first only for Performance
                if(not first and self.log[x][y][eventTyp] == tupel.one):
                    first = y
                elif(first and self.log[x][y][eventTyp] == tupel.two):
                    second = y
                    #id = uuid.uuid4()
                    gOne = Group(tupel.one)
                    #TODO One Error
                    #TODO make Tupel The Error Parent
                    gOne.set(event=first, trace=x, value=self.log[x][first][eventTime],
                             typ=eventTime)

                    gTwo = Group(tupel.two)
                    gTwo.set(event=second, trace=x, value=self.log[x][second][eventTime],
                             typ=eventTime)
                    list.append(gOne)
                    list.append(gTwo)
        return list

    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            error = error()
            error.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error)
        self.controller.addToErrorList(modErrorList)
