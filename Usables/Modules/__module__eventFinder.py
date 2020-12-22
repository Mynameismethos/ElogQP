#import pm4py.algo.filtering.log.attributes as attFilter
from pm4py.algo.filtering.log.attributes import attributes_filter



class module_eventFinder():
    def __init__(self, controller):
        self.controller= controller
        self.Settings = "hello"
        self.log = ""
        self.name = "Event Names"
        self.oneDes = "this programm finds and Lists all Event Names"
        self.desc = "Dont want to fill this Out Right now"

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

    def createFrames(self):
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(next=__name__+"_2",previous = None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        
        frameName=self.controller.createModFrame(1, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(next=__name__+"_3",previous=__name__+"_1",title=self.getName(),list={"hello","blue","I","enough,Wollen ","Sie ","in ","Excel ","eine ","Datei ","als ",".csv ","speichern, ","so ","gibt ","es ","keine ","Option ","zur ","Auswahl ","zwischen ","Komma ","oder ","ein ","Semikolon ","als ","Trennzeichen"})
        
        frameName=self.controller.createModFrame(0, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(next=__name__+"_1",previous=__name__+"_2",title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())
    

    def exec(self):
        self.createFrames()
        self.controller.showFrame(__name__+"_1")
        self.log=self.controller.getLog()
        self.findEvents()

    def findEvents(self):
        activities = attributes_filter.get_attribute_values(self.log, "concept:name")
    # activities = attFilter.get_attribute_values(log, "concept:name")
        self.controller.getFrameByName(__name__+"_2").update_Data(list=activities)

        

