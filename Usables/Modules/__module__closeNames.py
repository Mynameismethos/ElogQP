from typing import List
from pm4py.algo.filtering.log.attributes import attributes_filter
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

class module_closeNames():
    def __init__(self, controller):
        self.controller= controller
        self.Settings = "hello"
        self.log = ""
        self.name = "Close Event Names"
        self.oneDes = "this programm checks The Event Names for similar but unequal Names "
        #TODO change 
        self.desc = "this programm calls print. And gives it the Parameter 'Hello' "

    def createFrames(self):
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        
        frameName=self.controller.createModFrame(2, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title="Hello Module", button_text="Run", button_command =0)
        
        frameName=self.controller.createModFrame(0, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_1", previous=__name__+"_2",title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())
    
    def callBack(self, actionNumer):
        switcher={
            0:self.findSimilarNames()
        }
        switcher.get(int(actionNumer.get()), "Wrong Action")
            

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


    def getSettings(self):
        json = self.Settings
        return json


    def setSettings(self, Json):
        self.Settings = Json


    def getLog(self,log):
        self.log = log

 

