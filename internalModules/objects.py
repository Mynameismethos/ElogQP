class Group():
    def __init__(self, list):
        self.typ=None
        self.mainName=None
        self.listNames=list
        self.trace=None

    def getName(self):
         return self.mainName

    def getTyp(self):
        return self.typ

    def setTyp(self,typ):
        self.typ=typ

    def getTrace(self):
        return self.trace

    def setTrace(self,trace):
        self.trace=trace

    def addToList(self, name):
        if(name not in self.listNames):
            self.listNames.append(name)

    def getList(self):
         return self.listNames

    def isValid(self):
        return not (not self.listNames)

    def setName(self, name):
         self.mainName=name

    def setList(self, list):
        self.listNames=list


class tupel():
    def __init__(self,elOne,elTwo,elRatio):
        self.value=elRatio
        self.one=elOne
        self.two=elTwo

    def __lt__(self, other):
        return self.value < other.value
    
class error():
    def __init__(self, trace, event):
        self.trace=trace
        self.event=event
        self.desc=None
        self.dictkey=None
        self.dictVal=None
        self.errorModul=None
        self.classInfo=None
        self.autoRepair=None
        self.fixedVal=None