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

def createFrame(controller, example=0, name=__name__):
    controller.createModFrame(example, name)
    print(name)
  

def exec(controller):
    mod_name="hello_1"
    createFrame(controller,example=0, name=mod_name)
    controller.showFrame(mod_name)
    print("Hello")

