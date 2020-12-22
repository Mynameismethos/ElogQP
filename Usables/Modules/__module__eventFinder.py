#import pm4py.algo.filtering.log.attributes as attFilter
from pm4py.algo.filtering.log.attributes import attributes_filter
Settings = "hello"
log = ""
name = "Event Names"
oneDes = "this programm finds and Lists all Event Names"
desc = "Dont want to fill this Out Right now"



def getName():
    return name


def getOneDesc():
    return oneDes


def getDesc():
    return desc


def getSettings():
    json = Settings
    return json


def setSettings(Json):
    Settings = Json


def giveLog(log):
    log = log

def createFrames(controller):
    frameName=controller.createModFrame(0, __name__+"_1")
    controller.getFrameByName(frameName).update_Data(next=__name__+"_2",previous = None,title=getName(), intro=getOneDesc(), desc=getDesc())
    
    frameName=controller.createModFrame(1, __name__+"_2")
    controller.getFrameByName(frameName).update_Data(next=__name__+"_3",previous=__name__+"_1",title=getName(),list={"hello","blue","I","enough,Wollen ","Sie ","in ","Excel ","eine ","Datei ","als ",".csv ","speichern, ","so ","gibt ","es ","keine ","Option ","zur ","Auswahl ","zwischen ","Komma ","oder ","ein ","Semikolon ","als ","Trennzeichen"})
    
    frameName=controller.createModFrame(0, __name__+"_3")
    controller.getFrameByName(frameName).update_Data(next=__name__+"_1",previous=__name__+"_2",title="Hello Module", intro=oneDes, desc=desc)
  

def exec(controller):
    createFrames(controller)
    controller.showFrame(__name__+"_1")
    global log
    log=controller.getLog()
    findEvents(controller)

def findEvents(controller):
    global log 
    activities = attributes_filter.get_attribute_values(log, "concept:name")
   # activities = attFilter.get_attribute_values(log, "concept:name")
    controller.getFrameByName(__name__+"_2").update_Data(list=activities)
    print("ello")

    

