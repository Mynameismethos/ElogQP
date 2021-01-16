from fuzzywuzzy import fuzz
import internalModules.objects as objects


def levinRatio(list, lowerBound):
    closeList = []
    for x in range(len(list)-1):
        for y in range(x+1, len(list)):
                 ratio = fuzz.ratio(str.lower(list[x]), str.lower(list[y]))
                 if(ratio > lowerBound):
                     closeList.append(objects.tupel(list[x], list[y], ratio))
    closeList.sort()
    return closeList


def tokenRatio(list, lowerBound):
    closeList = []
    for x in range(len(list)-1):
        for y in range(x+1, len(list)):
            ratio = fuzz.token_set_ratio(
                str.lower(list[x]), str.lower(list[y]))
            if(ratio > lowerBound):
                print("comparing: "+list[x]+" and " + list[y])
                closeList.append(objects.tupel(list[x], list[y], ratio))
    closeList.sort()
    return closeList


def createGroups(tupelList, typ):
    groupeID = {}
    groupeList = []

    for tupel in tupelList:
        if (groupeID.get(tupel.one) and groupeID.get(tupel.two)):
            break
        elif (groupeID.get(tupel.one)):
            groupeList[groupeID.get(tupel.one)].addToList(tupel.two)
        elif (groupeID.get(tupel.two)):
            groupeList[groupeID.get(tupel.two)].addToList(tupel.one)
        else:
            g = objects.Group([tupel.one, tupel.two])
            g.setTyp(typ)
            groupeID[tupel.one] = len(groupeList)
            groupeID[tupel.two] = len(groupeList)
            groupeList.append(g)
    return groupeList


def all_Subgroups(list, minlength):
    group_List=[]
    newGroup=[]
    for x in list:
        group_List.append(x)
        newGroup.append([x])

    finalGroup=[]
    while(len(newGroup[0])<len(list)):
        newGroup=inner(newGroup,group_List)
        finalGroup.extend(newGroup)
    x=finalGroup[0]
    while(len(x)<minlength):
        finalGroup.pop(0)
        if(not finalGroup): return []
        x=finalGroup[0]
    return finalGroup

def inner(listOfGroup, list):
    newGroup=[]
    for element in listOfGroup:
        for value in list[list.index(element[-1])+1:]:
            newGroup.append(element + [value])
    return newGroup
