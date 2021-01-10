import internalModules.logwork as logwork
#import internalModules.compare as compare
import internalModules.objects as objects


class module_synonymousLabels():
    def __init__(self, controller):
        self.controller = controller
        self.settings = "hello"
        self.log = ""
        self.name = "Synonymous Labels"
        self.oneDes = "Example"
        self.listGroups = []
        self.currentGroup = int(0)
        self.events = []
        #TODO change
        self.desc = "Example"

    def createFrames(self):
        #startSeite
        frameName = self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=__name__+"_2", previous=None, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Starten des Modules
        frameName = self.controller.createModFrame(2, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, previous=__name__+"_1", title=self.getName(), button_text="Start", button_command=0)
        #anzeigen aller Events
        frameName = self.controller.createModFrame(1, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self,  previous=__name__+"_2", next=__name__+"_4",
                                                              title=self.getName(), button1_text="Reset", button1_command=2, button2_text="Add as Group", button2_command=1)
        self.controller.getFrameByName(frameName).setMultiselect(True)
        #Anzeigen der gruppen
        frameName = self.controller.createModFrame(1, __name__+"_4")
        self.controller.getFrameByName(frameName).update_Data(modController=self,  previous=__name__+"_3", next=__name__+"_5",
                                                              title="List Groups", button1_text="Previous Group", button1_command=3, button2_text="Next Group", button2_command=4)
        self.controller.getFrameByName(frameName).setMultiselect(False)
        #Beenden
        frameName = self.controller.createModFrame(2, __name__+"_5")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, previous=__name__+"_4", title="Ende", button_text="Ausführen", button_command=99)

    def callBack(self, actionNumer):
        switcher = {
            0: lambda: self.listEvents(),
            1: lambda: self.addGroup(),
            2: lambda: self.reset(),
            3: lambda: self.displayPrev(),
            4: lambda: self.displayNext(),
            99: lambda: self.addToErrorList(),
        }
        switcher.get(actionNumer.get(), lambda: print("Wrong Action"))()

    def exec(self):
        self.createFrames()
        self.log = self.controller.getLog()
        self.controller.showFrame(__name__+"_1")

    def addGroup(self):

        selected = self.controller.getFrameByName(__name__+"_3").getSelected()
        namelist = []
        for x in selected:
            namelist.append(self.events[x])
        group = objects.Group(namelist)
        group.setTyp("concept:name")
        if(group.isValid()):
            self.listGroups.append(group)
            self.displayGroup()

    def listEvents(self):
        self.events = logwork.getAllActivityAsList(self.log)
        self.controller.getFrameByName(
            __name__+"_3").update_Data(list=self.events)
        self.controller.showFrame(__name__+"_3")

    def reset(self):
        self.listGroups = []
        print("list is Empty")

    def displayPrev(self):
        frame = __name__+"_4"
        selected = self.controller.getFrameByName(frame).getSelected()
        if(selected):
            name = self.listGroups[self.currentGroup].getList()[selected[0]]
            self.listGroups[self.currentGroup].setName(name)
        if(self.currentGroup > 0):
            self.currentGroup -= 1
            self.controller.getFrameByName(
                frame).set_Widgets_Visible(button2="yes")
        else:  # removebutton
            self.controller.getFrameByName(
                frame).set_Widgets_Visible(button1="no")
        self.displayGroup()

    def displayNext(self):
        frame = __name__+"_4"
        selected = self.controller.getFrameByName(frame).getSelected()
        if(selected):
            name = self.listGroups[self.currentGroup].getList()[selected[0]]
            self.listGroups[self.currentGroup].setName(name)
        if(self.currentGroup < len(self.listGroups)-1):
            self.currentGroup += 1
            self.controller.getFrameByName(
                frame).set_Widgets_Visible(button1="yes")
        else:  # removebutton
            self.controller.getFrameByName(
                frame).set_Widgets_Visible(button2="no")
        self.displayGroup()

    def displayGroup(self):
        item = self.listGroups[self.currentGroup]
        indexOfName = None
        if(item.getName() in item.getList()):
            indexOfName = item.getList().index(item.getName())
        self.controller.getFrameByName(
            __name__+"_4").update_Data(list=item.getList(), selected=indexOfName)

    def addToErrorList(self):
        modErrorList = []
        for group in self.listGroups:
            name = group.getName()
            if(name):
                namelist = group.getList()
                for x in range(len(self.log)):
                    for y in range(len(self.log[x])):
                        logelement = self.log[x][y][group.getTyp()]
                        if logelement in namelist:
                            error = objects.error()
                            error.set(trace=x, event=y, dictkey=group.getTyp(
                            ), dictVal=logelement, fixedVal=name, classInfo=1, autoRepair=True, errorModul=self)
                            modErrorList.append(error)
            else:
                error = objects.error()
                error.set(trace="Global", dictVal=[
                          group.getList()], dictkey=group.getTyp(), classInfo=0, errorModul=self)
                modErrorList.append(error)

        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

    def changeLog(self):
        pass

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getLog(self, log):
        self.log = log

    def leaveMod(self):
        self.controller.deleteModFrame()
        self.controller.getFrameByName("frame_modules").showNextMod()
