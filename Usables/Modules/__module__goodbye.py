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
    controller.getFrameByName(frameName).update_Data(__name__+"_2",None,title=getName(), intro=getOneDesc(), desc=getDesc())
    
    frameName=controller.createModFrame(1, __name__+"_2")
    controller.getFrameByName(frameName).update_Data(__name__+"_3",__name__+"_1",title=getName(),list={"hello","blue","I","enough,Wollen ","Sie ","in ","Excel ","eine ","Datei ","als ",".csv ","speichern, ","so ","gibt ","es ","keine ","Option ","zur ","Auswahl ","zwischen ","Komma ","oder ","ein ","Semikolon ","als ","Trennzeichen"})
    
    frameName=controller.createModFrame(0, __name__+"_3")
    controller.getFrameByName(frameName).update_Data(__name__+"_1",__name__+"_2",title="Hello Module", intro=oneDes, desc=desc)
  

def exec(controller):
    createFrames(controller)
    controller.showFrame(__name__+"_1")
    print("Hello")

