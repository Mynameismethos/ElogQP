from typing import List
from pm4py.algo.filtering.log.attributes import attributes_filter
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

class module_closeNames():
    def __init__(self, controller):
        self.controller= controller
        self.settings = {"LevLower": 90}
        self.log = ""
        self.name = "Distorted Label"
        self.oneDes = "this programm checks The Event Names for similar but unequal Names "
        #TODO change 
        self.desc = ""

    def createFrames(self):
        #Greetings Page
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Settings
        frameName=self.controller.createModFrame(3, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title=self.getName(), settings=self.getSettings(), button1_text="Save", button1_command=1)
        #Start Programm
        frameName=self.controller.createModFrame(2, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_4",previous= __name__+"_2",title=self.getName(), button_text="Search for Distored Labels", button_command =0)
        #Display Results
        frameName=self.controller.createModFrame(1, __name__+"_4")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_5", previous=__name__+"_3",title=self.getName(),)
        #Show Changes and Run Programm
        frameName=self.controller.createModFrame(2, __name__+"_5")
        self.controller.getFrameByName(frameName).update_Data(modController=self, previous=__name__+"_4",title=self.getName(),)
    
    def callBack(self, actionNumer):
        switcher={
            0: lambda: self.findSimilarNames(),
            1: lambda: self.getSettingsFromFrame()
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()
            

    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.controller.showFrame(__name__+"_1")


    def findSimilarNames(self):
       activities = attributes_filter.get_attribute_values(self.log, "concept:name")
       activitieList=self.toList(activities)
       for x in range(len(activitieList)):
            for y in range(x+1,len(activitieList)):
                one=activitieList[x]
                two=activitieList[y]
                lowercase_equal= str.lower(one) == str.lower(two)
                ratio = fuzz.ratio(str.lower(one),str.lower(two))
                if(lowercase_equal or ratio>70):
                    print("comparing: "+one+" and " +two)
                    print("Lowercase Equal: "+ str(lowercase_equal))
                    print("Similarity: "+str(ratio))

    def getSettings(self):
        return self.Settings


    def setSettings(self, settings):
        self.Settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getFrameByName(__name__+"_2").getSettings()

    def leaveMod(self):
       self.controller.showFrame("frame_modules")
       for x in range(1,6):
           if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))


    def toList(self, dict):
        list =[]
        for key in dict:
            list.append(key)


        return list


    def getName(self):
        return self.name


    def getOneDesc(self):
        return self.oneDes


    def getDesc(self):
        return self.desc

    def getLog(self,log):
        self.log = log

 

