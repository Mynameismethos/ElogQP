from pm4py.algo.filtering.log.attributes import attributes_filter




class module_sameEvent():
    def __init__(self, controller):
        self.controller= controller
        self.Settings = "hello"
        self.log = ""
        self.name = "SameEvent"
        self.oneDes = "Example"
        self.listGroupes=[]
        self.currentGroupe= int(0)
        self.events =[]
        #TODO change 
        self.desc = "Example"

    def createFrames(self):
        #startSeite
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Starten des Modules 
        frameName=self.controller.createModFrame(2, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, previous= __name__+"_1",title="Hello Module", button_text="Start", button_command =0)
        #anzeigen aller Events
        frameName=self.controller.createModFrame(1, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_4", previous=__name__+"_2",title="Hello Module",button1_text="Reset", button1_command=2, button2_text="Add as Groupe", button2_command=1)
        self.controller.getFrameByName(frameName).setMultiselect(True)
        #Anzeigen der gruppen
        frameName=self.controller.createModFrame(1, __name__+"_4")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_5", previous=__name__+"_3",title="List Groups",button1_text="Previous Groupe", button1_command=3, button2_text="Next Groupe", button2_command=4)
        self.controller.getFrameByName(frameName).setMultiselect(False)
        #Beenden 
        frameName=self.controller.createModFrame(2, __name__+"_5")
        self.controller.getFrameByName(frameName).update_Data(modController=self, previous= __name__+"_1",title="Ende", button_text="Ausführen", button_command =5)
       

    def callBack(self, actionNumer):
        switcher={
            0:lambda: self.listEvents(),
            1:lambda: self.addGroupe(),
            2:lambda: self.reset(),
            3:lambda: self.displayPrev(),
            4:lambda: self.displayNext(),
            5:lambda: self.changeLog(),
            99:lambda: self.leaveMod()
        }
        switcher.get(actionNumer.get(), lambda: print("Wrong Action"))()
            

    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.controller.showFrame(__name__+"_1")

   
    def addGroupe(self):

        selected= self.controller.getFrameByName(__name__+"_3").getSelected()
        namelist=[]
        for x in selected:
            namelist.append(self.events[x])
        groupe=EventGroup()
        groupe.setList(namelist)
        self.listGroupes.append(groupe)
        self.displayGroupe()

    def listEvents(self):
        self.toList(attributes_filter.get_attribute_values(self.log, "concept:name"))
        self.controller.getFrameByName(__name__+"_3").update_Data(list=self.events)
        self.controller.showFrame(__name__+"_3")

    def reset(self):
        self.listGroupes=[]
        print("list is Empty")

    def displayPrev(self):
        selected= self.controller.getFrameByName(__name__+"_4").getSelected()
        name=self.listGroupes[self.currentGroupe].getList()[selected[0]]
        self.listGroupes[self.currentGroupe].setName(name)
        if(self.currentGroupe<0):self.currentGroupe-=1
        self.displayGroupe()
    def displayNext(self):
        selected= self.controller.getFrameByName(__name__+"_4").getSelected()
        name=self.listGroupes[self.currentGroupe].getList()[selected[0]]
        self.listGroupes[self.currentGroupe].setName(name)
        if(self.currentGroupe<len(self.listGroupes)-1):self.currentGroupe+=1
        self.displayGroupe()

    def displayGroupe(self):
        list1=self.listGroupes[self.currentGroupe].getList()
        self.controller.getFrameByName(__name__+"_4").update_Data(list=list1)

    def changeLog(self):
        for group in self.listGroupes:
            name= group.getName()
            namelist= group.getList()
            for x in range(len(self.log)):
                for y in range(len(self.log[x])):
                    logname= self.log[x][y]["concept:name"]
                    if logname in namelist:
                        self.log[x][y]["concept:name"]=name


        self.controller.setLog(self.log)
        self.leaveMod()



    def toList(self, dict):
        self.events=[]
        for key in dict:
           self.events.append(key)





    def getName(self):
        return self.name


    def getOneDesc(self):
        return self.oneDes


    def getDesc(self):
        return self.desc


    def getSettings(self):
        json = self.Settings
        return json


    def setSettings(self, Json):
        self.Settings = Json


    def getLog(self,log):
        self.log = log

    def leaveMod(self):
        self.controller.showFrame("frame_modules")
        for x in range(1,6):
            if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))

            

        #deleteFrames

 

class EventGroup():
    def __init__(self):
         self.mainName=""
         self.listNames=[]

    def getName(self):
         return self.mainName

    def getList(self):
         return self.listNames

    def setName(self, name):
         self.mainName=name

    def setList(self, list):
        self.listNames=list

    