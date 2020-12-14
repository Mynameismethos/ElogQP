import os
import pm4py


def loadLogByName(name):
    filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
    log = pm4py.read_xes(filePath)
    return log