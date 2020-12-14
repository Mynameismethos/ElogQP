import os
import importlib


def loadmodules():
    dir = os.listdir(os.path.abspath(os.curdir) + "\\Usables\\Modules\\")
    list = []
    for file in dir:
        if file.startswith("__module__"):
            filename, file_extention = os.path.splitext(file)
            print(filename)
            mod = importlib.import_module("Usables.Modules." + filename)
            list.append(mod)

    return list