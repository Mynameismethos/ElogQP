import os
import pm4py


class test():
    def __init__(self, *args,):
       list =["a",2,3,4]
       retrunValue=all_Subgroups(list,5)
       for x in retrunValue:
        print(x)
       

def loadLogByName(name):
    try:
        filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
        log = pm4py.read_xes(filePath)
    except FileNotFoundError:
        log = [0][0]
    return log

    def runthis(self):
        print(self.test)




app = test()


