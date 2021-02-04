import os
import pm4py
import random
import string


class test():
    def __init__(self, *args,):
        self.log= self.loadLogByName("timeTravel.xes")
        self.error_pollutedLabels()
        self.exportLog("pollutedLabels.xes")
     




    def error_pollutedLabels(self):
        event="concept:name"
        triggerEvent="Eingang Anfrage"
        for trace in self.log:
            for case in trace:
                if(case[event]==triggerEvent):
                    bla="".join(random.choices(string.ascii_uppercase, k=5))
                    case[event]=case[event]+": ID: "+bla
    

    def loadLogByName(self,name):
        try:
            filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
            log = pm4py.read_xes(filePath)
        except FileNotFoundError:
            log = [0][0]
        return log

    def exportLog(self, name):
        filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
        pm4py.write_xes(self.log, filePath)




app = test()


