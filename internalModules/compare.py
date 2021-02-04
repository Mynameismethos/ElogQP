from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from difflib import SequenceMatcher 
import internalModules.objects as objects


def levinRatio(dict, lowerBound, maxRatio=None):
    if(not dict): return []
    subGroups = all_Subgroups(list(dict.keys()), 2, maxlen=2)

    for x in reversed(subGroups):
        x.sort(key= lambda l: dict[l])
        occurenceRatio = dict[x[0]] / dict[x[1]]
        if(occurenceRatio > maxRatio):
            subGroups.remove(x)

    closeList = []
    for x in subGroups:
        ratio = fuzz.ratio(str.lower(x[0]), str.lower(x[1]))
        if(ratio > lowerBound):
            closeList.append(objects.tupel(x[0], x[1], ratio))
    closeList.sort()
    return closeList


def tokenRatio(dict, lowerBound, maxRatio=1):
    if(not dict): return []

    subGroups = all_Subgroups(list(dict.keys()), 2, maxlen=2)

    for x in reversed(subGroups):
        x.sort(key= lambda l: dict[l])
        occurenceRatio = dict[x[0]] / dict[x[1]]
        if(occurenceRatio > maxRatio):
            subGroups.remove(x)
    closeList = []

    closeList= tokenRatioTupel(subGroups,lowerBound)

    return closeList

def tokenRatioTupel(subGroups, lowerBound):
    closeList=[]
    for x in subGroups:
        ratio = fuzz.token_set_ratio(
            str.lower(x[0]), str.lower(x[1]))
        if(ratio > lowerBound):
            closeList.append(objects.tupel(x[0], x[1], ratio))
    closeList.sort()
    return closeList

def largestSubstring(element):
    result = SequenceMatcher(None,element[0],element[1]).find_longest_match(0,len(element[0]),0,len(element[1]))
    string=element[0][result.a:result.a+result.size]
    return string

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


def all_Subgroups(list, minlength, maxlen=None):
    group_List = []
    newGroup = []

    if(len(list)<minlength):return[]

    if(not maxlen):
        maxlen = len(list)

    for x in list:
        group_List.append(x)
        newGroup.append([x])

    finalGroup = []
    while(len(newGroup[0]) < maxlen):
        newGroup = inner(newGroup, group_List)
        finalGroup.extend(newGroup)
    x = finalGroup[0]
    while(len(x) < minlength):
        finalGroup.pop(0)
        if(not finalGroup):
            return []
        x = finalGroup[0]
    return finalGroup



def inner(listOfGroup, list):
    newGroup = []
    for element in listOfGroup:
        for value in list[list.index(element[-1])+1:]:
            newGroup.append(element + [value])
    return newGroup

