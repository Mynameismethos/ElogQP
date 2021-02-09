import os
import threading
import pm4py


def loadLogByName(controller, name, button):
        thread = threading.Thread(target=_run, args=(controller,name, button))
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

def _run(controller,name,button):
    try:
        filePath = os.path.abspath(os.curdir) + "\\Usables\\Log\\"+name
        controller.setLog(pm4py.read_xes(filePath),button=button, name=name)
    except FileNotFoundError:
        controller.log = [0][0]
    


def getAllLogs():
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Log\\")
    list = []
    for file in dir:
        filename, file_extention = os.path.splitext(file)
        if(file_extention == ".xes"):
            list.append(file)
    return list


    

   