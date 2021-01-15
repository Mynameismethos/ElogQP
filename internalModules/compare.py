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
