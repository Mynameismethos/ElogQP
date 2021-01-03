import os
import pm4py


def loadLogByName(name):
    try:
        filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
        log = pm4py.read_xes(filePath)
    except FileNotFoundError:
        log = [0][0]
    return log


def getAllLogs():
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Log\\")
    list = []
    for file in dir:
        filename, file_extention = os.path.splitext(file)
        if(file_extention==".xes"):
            list.append(file)
    return list