"""
This internal Module is a composite of function that compare Elements and elements in Lists
"""
from internalModules.logwork import getAllActivityAsDict
from fuzzywuzzy import fuzz
from difflib import SequenceMatcher 
from nltk.corpus import wordnet as wn
from internalModules.objects import *

def levinRatio(dict, lowerBound, maxRatio=0):
    """
    funtion to compare the elements in the dictionary to each other through levinstein

    Keyword arguments:
    maxRatio -- maximal Ratio two similar elements must have to be considert (default: 0)
    
    Return a list of Strings that are similar to each other
    """
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
            closeList.append(tupel(x[0], x[1], ratio))
    closeList.sort()
    return closeList


def tokenRatio(dict, lowerBound, maxRatio=0):
    """
    Function to compare elements in the dict pairwise through Token Ratio and Levinstein

    Keyword arguments:
    maxRatio -- maximal Ratio two similar elements must have to be considert (default: 0)
    
    Return a list of Strings that are similar to each other
    """
    if(not dict): return []

    subGroups = all_Subgroups(list(dict.keys()), 2, maxlen=2)

    for x in reversed(subGroups):
        x.sort(key= lambda l: dict[l])
        occurenceRatio = dict[x[0]] / dict[x[1]]
        if(occurenceRatio > maxRatio):
            subGroups.remove(x)
    closeList = []

    closeList= _tokenRatioTupel(subGroups,lowerBound)

    return closeList

def _tokenRatioTupel(subGroups, lowerBound):
    """
    inner function of tokenRatio
    returns a list of elements that a similiar to each other
    """
    closeList=[]
    for x in subGroups:
        ratio = fuzz.token_set_ratio(
            str.lower(x[0]), str.lower(x[1]))
        if(ratio > lowerBound):
            closeList.append(tupel(x[0], x[1], ratio))
    closeList.sort()
    return closeList

#TODO Comment Function
def isSimilarResources(dict_one, dict_two):
    dict_one=_normDict(dict_one)
    dict_two=_normDict(dict_two)

    res_dif=0
    for key in dict_one:
        if(key in dict_two):
            res_dif+=abs(dict_one[key]-dict_two[key])
        else: res_dif+=dict_one[key]
    for key in dict_two:
        if(key not in dict_one):
            res_dif+=dict_two[key]
    return res_dif

def _normDict(setDict):
    totalRes=0
    for key in setDict:
        totalRes+=setDict[key]
    for key in setDict:
        setDict[key]/=totalRes
    return setDict

def matchWordnet(eventList):
    """
    function to Wordnet macht-elements in the list pairwise to each other
    returns a list of elements that are pairwise similiar to each other  
    """
    if(not eventList): return []

    subGroups = all_Subgroups(list(eventList.keys()), 2, maxlen=2)
    wordNetMatches=[]
    for x in reversed(subGroups):
        if( _isAMatchInWordNet(x[0],x[1])):
            t=[tupel(x[0],x[1],1),tupel(x[1],x[0],1)][eventList[x[0]]>eventList[x[1]]]
            wordNetMatches.append(t)

    return wordNetMatches


def _isAMatchInWordNet(word1, word2):
    """
    inner function of matchWornet 

    returns boolean = if two elements are similiar to each other
    """
    wordmaps= wn.synsets(word1)
    for el in wordmaps:
        pos_names=el.lemma_names()
        for name in pos_names:
            if(name==word2):
                return True
    return False
    

    
def largestSubstring(element):
    """
    function to find the largest Substring in a tuple

    returns larges string included in both elements
    """
    result = SequenceMatcher(None,element[0],element[1]).find_longest_match(0,len(element[0]),0,len(element[1]))
    string=element[0][result.a:result.a+result.size]
    return string

def createGroups(tupelList, typ):
    """ function to turn a tupel list into a larger objects that contatins the variable typ  
    
    returns list of Group object containing the tupels and the typ
    """
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
            g = Group([tupel.one, tupel.two])
            g.setTyp(typ)
            groupeID[tupel.one] = len(groupeList)
            groupeID[tupel.two] = len(groupeList)
            groupeList.append(g)
    return groupeList


def all_Subgroups(list, minlength, maxlen=None):
    """
    function to get all different (unsorted) permutations of the elements in the given list

    Keyword arguments: maxlen is the maximum allowed number of elements in a given List(default : None)

    returns a List of all Permutations
    """
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
        newGroup = _innerSubGroups(newGroup, group_List)
        finalGroup.extend(newGroup)
    x = finalGroup[0]
    while(len(x) < minlength):
        finalGroup.pop(0)
        if(not finalGroup):
            return []
        x = finalGroup[0]
    return finalGroup



def _innerSubGroups(listOfGroup, list):
    #TODO check this out
    """
    function to extend every object in the listOfGroups with one element not yet included in this object


    returns a list of permutations with a depth of one greater than the given list
    """
    newGroup = []
    for element in listOfGroup:
        for value in list[list.index(element[-1])+1:]:
            newGroup.append(element + [value])
    return newGroup

