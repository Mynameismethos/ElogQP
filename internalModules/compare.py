from fuzzywuzzy import fuzz

class Group():
    def __init__(self):
         self.mainName=""
         self.listNames=[]

    def getName(self):
         return self.mainName

    def addToList(self, name):
        if(name not in self.listNames):
            self.listNames.append(name)

    def getList(self):
         return self.listNames

    def setName(self, name):
         self.mainName=name

    def setList(self, list):
        self.listNames=list

class customTupel():
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
                closeList.append(customTupel(list[x],list[y],ratio))
    closeList.sort()
    return closeList


def tokenRatio(list, lowerBound):
    closeList=[customTupel]
    for x in range(len(list)):
        for y in range(x+1,len(list)):
            ratio = fuzz.token_set_ratio(str.lower(list[x]),str.lower(list[y]))
            if(ratio>lowerBound):
                print("comparing: "+list[x]+" and " +list[y])
                closeList.append(customTupel(list[x],list[y],ratio))
    closeList.sort()
    return closeList
                
def createGroups(tupelList=[customTupel]):
    groupeID={}
    groupeList=[Group]

    for tupel in tupelList:
        if (groupeID.get(tupel.one) and groupeID.get(tupel.two)):
            break
        elif (groupeID.get(tupel.one)):
            groupeList[groupeID.get(tupel.one)].addToList(tupel.two)
        elif (groupeID.get(tupel.two)):
            groupeList[groupeID.get(tupel.two)].addToList(tupel.one)
        else: 
            g=Group()
            g.setList([tupel.one, tupel.two])
            groupeID[tupel.one]=len(groupeList)
            groupeID[tupel.two]=len(groupeList)
            groupeList.append(g)
    return groupeList
    
