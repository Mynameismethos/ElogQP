from fuzzywuzzy import fuzz

class Group():
    def __init__(self, list):
        self.typ=None
        self.mainName=None
        self.listNames=list

    def getName(self):
         return self.mainName

    def getTyp(self):
        return self.typ

    def setTyp(self,typ):
        self.typ=typ

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
    


def levinRatio(list, lowerBound):
    closeList=[]
    for x in range(len(list)):
        for y in range(x+1,len(list)):
            ratio = fuzz.ratio(str.lower(list[x]),str.lower(list[y]))
            if(ratio>lowerBound):
                print("comparing: "+list[x]+" and " +list[y])
                closeList.append(tupel(list[x],list[y],ratio))
    closeList.sort()
    return closeList


def tokenRatio(list, lowerBound):
    closeList=[]
    for x in range(len(list)):
        for y in range(x+1,len(list)):
            ratio = fuzz.token_set_ratio(str.lower(list[x]),str.lower(list[y]))
            if(ratio>lowerBound):
                print("comparing: "+list[x]+" and " +list[y])
                closeList.append(tupel(list[x],list[y],ratio))
    closeList.sort()
    return closeList
                
def createGroups(tupelList,typ):
    groupeID={}
    groupeList=[]

    for tupel in tupelList:
        if (groupeID.get(tupel.one) and groupeID.get(tupel.two)):
            break
        elif (groupeID.get(tupel.one)):
            groupeList[groupeID.get(tupel.one)].addToList(tupel.two)
        elif (groupeID.get(tupel.two)):
            groupeList[groupeID.get(tupel.two)].addToList(tupel.one)
        else: 
            g=Group([tupel.one, tupel.two])
            g.setTyp(typ)
            groupeID[tupel.one]=len(groupeList)
            groupeID[tupel.two]=len(groupeList)
            groupeList.append(g)
    return groupeList
    
