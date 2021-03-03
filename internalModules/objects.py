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
        self.parent= ""
        self.desc = None
        self.dictkey = None
        self.dictVal = None
        self.errorModul = None
        self.classInfo = None
        self.autoRepair = False
        self.fixedVal = None

    def set(self, trace=None,
            event=None,
            parent=None,
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
        if(parent != None):
            self.parent = parent
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

    def __eq__(self, other):
        if(not self or not other): return False
        return (self.trace == other.trace and 
        self.event == other.event  and 
        self.parent== other.parent and 
        self.desc == other.desc  and 
        self.dictkey == other.dictkey  and 
        self.dictVal == other.dictVal  and 
        self.errorModul == other.errorModul  and 
        self.classInfo == other.classInfo  and 
        self.autoRepair == other.autoRepair  and 
        self.fixedVal == other.fixedVal  )

    def __hash__(self):
        dictVal= self.dictVal
        if(isinstance(self.dictVal, list)):
            dictVal= "".join(*self.dictVal)

        return hash((self.trace,
        self.desc,
        self.event,
        self.parent,
        self.dictkey,
        dictVal,
        #self.errorModul,
        self.classInfo,
        self.autoRepair,
        self.fixedVal))
        
class module():
    def __init__(self):
        self.modFramesNext =[]
        self.modFramesPrev =[]