import os
import importlib


def loadmodules():
    dir = os.listdir(os.path.abspath(os.curdir) + "\\modules")
    list = []
    for file in dir:
        print(file)
        if file.startswith("__module__"):
            filename, file_extention = os.path.splitext(file)
            print(filename)
            mod = importlib.import_module("modules." + filename)
            print(mod.getOneDesc())
            list.append(mod)

    return list