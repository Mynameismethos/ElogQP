import os
import importlib
import inspect
import sys
import internalModules.ModuleFiles as ModuleFiles

"""
A collection of functions to load Modules and Frames
"""
def loadmodules(controller):
    """
     function to load Modules stored in '\Usables\Modules' into the persistent Storage
    """
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Modules\\")
    list = []
    for file in dir:
        filename, file_extention = os.path.splitext(file)
        print(filename)
        name = "Usables.Modules." + filename
        importlib.import_module(name)
        for name, obj in inspect.getmembers(sys.modules[name]):
            if inspect.isclass(obj) and issubclass(obj , ModuleFiles.ModuleFiles) and (name != "ModuleFiles"):
                t = obj(controller)
                list.append(t)

    return list


def loadFrames():
    """
    function to load Frames stored in '\Usables\Frames\'  into the persistent storage
    """
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
