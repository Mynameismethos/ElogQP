import os
import importlib
import inspect
import sys


def loadmodules(controller):
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Modules\\")
    list = []
    for file in dir:
        if file.startswith("__module__"):
            filename, file_extention = os.path.splitext(file)
            print(filename)
            name="Usables.Modules." + filename
            importlib.import_module(name)
            for name, obj in inspect.getmembers(sys.modules[name]):
                if inspect.isclass(obj) and obj.__name__.startswith("module"):
                    t = obj(controller)
                    list.append(t)
            

    return list

def loadFrames():
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Frames\\")
    list = []
    for file in dir:
        if file.startswith("frame__"):
            filename, file_extention = os.path.splitext(file)
            name = "Usables.Frames." + filename
            print(name)
            importlib.import_module(name)
            for name, obj in inspect.getmembers(sys.modules[name]):
                if inspect.isclass(obj) and obj.__name__.startswith("frame"):
                    list.append(obj)
                    break
            
            

    return list
