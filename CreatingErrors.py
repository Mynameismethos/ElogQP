import os
import pm4py
import random
import string
import datetime


class test():
    def __init__(self, *args,):
        self.log= self.loadLogByName("Kitchen Error_Second.xes")
        self.error_pollutedLabels()
        self.exportLog("Kitchen Error.xes")
     




    def error_pollutedLabels(self):
        event="concept:name"
        triggerEvent="open Fridge"
        ids=["Peter", "Gustav", "Susanne", "Frank", "Herbert", "Julia", "Jeff", "Tobias", "Nicht Jeff", "Manuel"]
        for trace in self.log:
            for case in trace:
                if(case[event]==triggerEvent):
                    bla="".join(random.choices(ids))
                    case[event]=case[event]+"-- ID: "+bla


    def error_collateralEvents(self):
        event="concept:name"
        time="time:timestamp"
        triggerEvent="Recherchieren"
        for trace in self.log:
            for i in range(len(trace)-1):
                if(trace[i][event]==triggerEvent):
                    trace[i+1][time]=trace[i][time]+datetime.timedelta(seconds=180)    

    def loadLogByName(self,name):
        try:
            filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
            log = pm4py.read_xes(filePath)
        except FileNotFoundError:
            log = [0][0]
        return log

    def deleteFields(self, number):
        fields={"time":"time:timestamp","name":"concept:name", "org":"org:resource"}
        for x in range(number):
            trace= self.log[random.randrange(len(self.log))]
            event= trace[random.randrange(len(trace))]
            choice= random.choice(list(fields.keys()))
            event[fields[choice]]=""




    def deleteEvents(self, number):
         for x in range(number):
            trace= self.log[random.randrange(len(self.log))]
            event= trace[random.randrange(len(trace))]
            del event


    def exportLog(self, name):
        filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
        pm4py.write_xes(self.log, filePath)




app = test()


