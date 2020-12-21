Settings = "hello"
log = ""
name = "Hello Bot"
oneDes = "this programm says Hello"
desc = "this programm calls print. And gives it the Parameter 'Hello' "



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
    
    frameName=controller.createModFrame(0, __name__+"_2")
    controller.getFrameByName(frameName).update_Data(__name__+"_3",__name__+"_1",title="Hello Module", intro=oneDes, desc=desc)
    
    frameName=controller.createModFrame(0, __name__+"_3")
    controller.getFrameByName(frameName).update_Data(__name__+"_1",__name__+"_2",title="Hello Module", intro=oneDes, desc=desc)
  

def exec(controller):
    createFrames(controller)
    controller.showFrame(__name__+"_1")
    print("Hello")

