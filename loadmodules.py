import os
import importlib


def loadmodules():
    dir = os.listdir(os.path.abspath(os.curdir) + "\\modules")
    list = []
    for file in dir:
        if file.startswith("__module__"):
            filename, file_extention = os.path.splitext(file)
            mod = importlib.import_module("modules." + filename)
            list.append(mod)

    return list