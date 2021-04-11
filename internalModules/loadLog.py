"""
This is a collection of function around working with eventlogs        
"""
import os
import threading
import pm4py


def loadLogByName(controller, name, button):
    """
     Starts a thread in which the log, specified by the name, is loaded into the persistent storage
    """
    thread = threading.Thread(target=_run, args=(controller,name, button))
    thread.daemon = True                            # Daemonize thread
    thread.start()                                  # Start the execution

def _run(controller,name,button):
    """inner function of loadLogByName    """

    try:
        filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
        controller.setLog(pm4py.read_xes(filePath),button=button, name=name)
    except FileNotFoundError:
        controller.setLog([0][0])
    


def getAllLogs():
    """
     function to get a list of all eventlogs stored under \\Usables\\Log

     returns a list of strings
    """
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Log\\")
    list = []
    for file in dir:
        filename, file_extention = os.path.splitext(file)
        if(file_extention == ".xes"):
            list.append(file)
    return list


    

   