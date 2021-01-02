import pm4py
from pm4py.algo.filtering.log.attributes import attributes_filter
def getAllActivityAsDict(log):
    return attributes_filter.get_attribute_values(log, "concept:name")
       

def getAllActivityAsList(log):
    events=[]
    for key in getAllActivityAsDict(log):
        events.append(key)
    return events



