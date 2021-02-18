from typing import DefaultDict
from pm4py.algo.filtering.log.attributes import attributes_filter
import datetime


def getAllActivityAsDict(log):
    return attributes_filter.get_attribute_values(log, "concept:name")


def getAllActivityAsList(log):
    events = []
    for key in getAllActivityAsDict(log):
        events.append(key)
    return events


def getAllResourcesAsDict(log):
    resources = attributes_filter.get_attribute_values(log, "org:resource")
    return resources

def getAllResourcesAsList(log):
    resources =[]
    for key in getAllResourcesAsDict(log):
        resources.append(key)
    return resources

def getAveragePosition(log,event_name):
    counter=0
    position=0
    for trace in log:
        for index in range(len(trace)):
            if(trace[index]["concept:name"]==event_name):
                counter+=1
                position+=index
    if(counter):
        return position/counter
    return -1 

def getAvereageLength(log,event_name):
    counter=0
    total_length=0
    for trace in log:
        for index in range(len(trace)-1):
            if(trace[index]["concept:name"]==event_name):
                d_time= abs(trace[index]["time:timestamp"]-trace[index+1]["time:timestamp"])
                length=d_time.total_seconds()
                total_length+=length
                counter+=1
    if(counter):
        return total_length/counter
    return -1 

def getUsedResources(log,event_name):
    res_dict=DefaultDict (int)
    for trace in log:
        for index in range(len(trace)):
            if(trace[index]["concept:name"]==event_name):
                res= trace[index]["org:resource"]
                split_res=res.split(",")
                for el in split_res:
                    res_dict[el]+=1
    return res_dict