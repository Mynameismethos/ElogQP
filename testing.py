

import os
import pm4py



class test():
    def __init__(self, *args,):
        pass:

        


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