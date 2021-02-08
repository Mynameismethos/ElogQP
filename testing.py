import os
import pm4py
import internalModules.compare as compare


class test():
    def __init__(self, *args):
        liste=[1,2,3,4]
        reListe=list(reversed(liste))
        sub=compare.all_Subgroups(liste,2,maxlen=2)+compare.all_Subgroups(list(reversed(liste)),2,maxlen=2)
        sub.sort()
        print(sub)


       

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


