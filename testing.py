import os
import pm4py
import internalModules.objects as objects


class test():
    def __init__(self, *args):
        g1= objects.Group([1,2,3])
        g2= objects.Group([7,2,3])
        g3= objects.Group([4,2,3])
        liste=[g1,g2,g3]
        for x in liste:
            x.listNames.sort()
       
        print(liste)


       

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


