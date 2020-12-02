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
    this.log = log


def exec(callback):
    print("Hello")
