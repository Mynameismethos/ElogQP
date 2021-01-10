from tkinter import EventType


class Group():
    def __init__(self, list):
        self.listNames = list
        self.name = None
        self.trace = None
        self.event = None
        self.typ = None
        self.value = None

    def set(self, event=None,
            trace=None,
            value=None,
            typ=None,
            name=None):
        if(event != None):
            self.event = event
        if(trace != None):
            self.trace = trace
        if(value != None):
            self.value = value
        if(typ != None):
            self.typ = typ
        if(name != None):
            self.name = name

    def getEvent(self):
        return self.event

    def getTrace(self):
        return self.trace

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def getTyp(self):
        return self.typ

    def setTyp(self, typ):
        self.typ = typ

    def getTrace(self):
        return self.trace

    def setTrace(self, trace):
        self.trace = trace

    def addToList(self, name):
        if(name not in self.listNames):
            self.listNames.append(name)

    def getList(self):
        return self.listNames

    def isValid(self):
        return not (not self.listNames)

    def setName(self, name):
        self.mainName = name

    def setList(self, list):
        self.listNames = list


class tupel():
    def __init__(self, elOne, elTwo, elRatio):
        self.value = elRatio
        self.one = elOne
        self.two = elTwo

    def __lt__(self, other):
        return self.value < other.value


class error():
    def __init__(self):
        self.trace = None
        self.event = None
        self.desc = None
        self.dictkey = None
        self.dictVal = None
        self.errorModul = None
        self.classInfo = None
        self.autoRepair = None
        self.fixedVal = None

    def set(self, trace=None,
            event=None,
            desc=None,
            dictkey=None,
            dictVal=None,
            errorModul=None,
            classInfo=None,
            autoRepair=None,
            fixedVal=None):
        if(trace != None):
            self.trace = trace
        if(event != None):
            self.event = event
        if(desc != None):
            self.desc = desc
        if(dictkey != None):
            self.dictkey = dictkey
        if(dictVal != None):
            self.dictVal = dictVal
        if(errorModul != None):
            self.errorModul = errorModul
        if(classInfo != None):
            self.classInfo = classInfo
        if(autoRepair != None):
            self.autoRepair = autoRepair
        if(fixedVal != None):
            self.fixedVal = fixedVal
