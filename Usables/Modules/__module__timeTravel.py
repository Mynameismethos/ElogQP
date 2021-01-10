from typing import DefaultDict
import internalModules.logwork as logwork
#import internalModules.compare as compare
import internalModules.objects as objects

class module_timeTravel():
    def __init__(self, controller):
        self.controller= controller
        #TODO change 
        self.settings = {"String Seperator": "//://", "Check Ratio": 0.05}
        self.name = "Inadvertent Time Travel"
        self.oneDes = "this programm checks for the Inadvertent Time Travel Issue"
        self.desc = "The String Sperator musn´t be part of any Event Name"
        self.log = None
        #EXAMPLE FOR LISTS
        self.occurence=DefaultDict(int)
        self.listGroups=[]
        self.currentGroup=int(0)

        #TODO IMPLEMENT 
        # EXAMPLE
    def createFrames(self):
        #Greetings Page
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Settings
        frameName=self.controller.createModFrame(3, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=1)
        #Start Programm
        frameName=self.controller.createModFrame(2, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(modController=self,previous= __name__+"_2",title=self.getName(), button_text="Search for Time Travelers", button_command =0)
        #Display Found 
        frameName=self.controller.createModFrame(3, __name__+"_4")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_5", previous=__name__+"_3",title="List Found Groups",button1_text="Previous Trace", button1_command=80, button2_text="Next Trace", button2_command=81, button3_text="save and reorder", button3_command=1)
        #Show Changes and Run Programm
        frameName=self.controller.createModFrame(2, __name__+"_5")
        self.controller.getFrameByName(frameName).update_Data(modController=self, previous=__name__+"_4",title=self.getName(),button_text="Apply changes to Log", button_command =99)
    
    #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher={
            0: lambda: self.findTimeTravel(),
            1: lambda: self.saveAndReorder(__name__+"_4"),
            80:lambda: self.displayPrev(__name__+"_4"),
            81:lambda: self.displayNext(__name__+"_4"),
            99:lambda: self.changeLog(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()
            

    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.controller.showFrame(__name__+"_1")


    def findTimeTravel(self):
        eventtyp="concept:name"
        self.occurence=DefaultDict(int)
        for x in range(len(self.log)):
            for y in range(0,len(self.log[x])-1):
                elOne= self.log[x][y][eventtyp]
                elTwo= self.log[x][y+1][eventtyp]
                self.occurence[elOne+self.getSettings()["String Seperator"]+elTwo]+=1
        tupellist=self.createTupels()
        
        for t in tupellist:
            self.listGroups.extend(self.findTraceOfTupel(t))
        
        if(self.listGroups):
            self.displayGroup(__name__+"_4")
            self.controller.showFrame(__name__+"_4")
        else:
            #TODO update Nothing Found
            self.controller.showFrame(__name__+"_1")
        

    def createTupels(self):
        allAct= logwork.getAllActivityAsList(self.log)
        tupellist=[]
        for x in range(len(allAct)):
            for y in range(len(allAct)-1):
                elOne=allAct[x]
                elTwo=allAct[y]
                if(self.occurence[elOne+self.getSettings()["String Seperator"]+elTwo]!=0 and self.occurence[elTwo+self.getSettings()["String Seperator"]+elOne]!=0):
                    ratio=self.occurence[elOne+self.getSettings()["String Seperator"]+elTwo]/self.occurence[elTwo+self.getSettings()["String Seperator"]+elOne]
                    if(ratio<1):
                        tupellist.append(objects.tupel(elOne, elTwo, ratio))
        return tupellist


    def findTraceOfTupel(self,tupel):
        eventtyp="concept:name"
        list=[]
        for x in range(len(self.log)):
            first=None
            second=None
            for y in range(0,len(self.log[x])-1):
                if(self.log[x][y][eventtyp]==tupel.one):
                    first=y
                if(self.log[x][y][eventtyp]==tupel.two):
                    second=y
                if(first and second and first<second):
                    # see if we can change anything
                    # prepare to display
                    # 
                    g=objects.Group([tupel.one, tupel.two])
                    g.setName(x)
                    g.setTrace(self.log[x]._list)
                    list.append(g)
                    break
        return list


    def saveAndReorder(self, frame):
        canList= self.controller.getFrameByName(frame).getCanvasAsList()
        trace=self.listGroups[self.currentGroup].getTrace()
        for x in range(len(canList)):
            trace[x]["time:timestamp"]=canList[x]
        trace.sort(key= lambda x: x["time:timestamp"])
        self.listGroups[self.currentGroup].setTrace(trace)
        self.displayGroup(frame)


    def displayPrev(self,frame):
        if(self.currentGroup>0):
            self.currentGroup-=1
            self.controller.getFrameByName(frame).set_Widgets_Visible(button2="yes")
            self.displayGroup(frame)
        else:#removebutton
            self.controller.getFrameByName(frame).set_Widgets_Visible(button1="no")
 

    def displayNext(self,frame):
        if(self.currentGroup<len(self.listGroups)-1):
            self.currentGroup+=1
            self.controller.getFrameByName(frame).set_Widgets_Visible(button1="yes")
            self.displayGroup(frame)
        else:  #removebutton
            self.controller.getFrameByName(frame).set_Widgets_Visible(button2="no")
        
        
    def displayGroup(self,frame):
        trace=self.listGroups[self.currentGroup].getTrace()
        highlightList=self.listGroups[self.currentGroup].getList()
        self.controller.getFrameByName(frame).update_Data(canList=trace, highlight=highlightList)
   
    #TODO IMPLEMENT
    def changeLog(self):
        updatedLog= self.log
        for case in self.listGroups:
            updatedLog[case.getName()]._list=case.getTrace()
        self.controller.setLog(updatedLog)
        self.clean()
        self.leaveMod()

    def clean(self):
        self.occurence=DefaultDict(int)
        self.currentGroup=0
        self.listGroups=[]
        self.log=None

    def getSettings(self):
        return self.settings


    def setSettings(self, settings):
        self.settings=settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getFrameByName(__name__+"_2").getCanvasAsDict()

    def leaveMod(self):
       self.controller.showFrame("frame_modules")
       self.currentGroup=0
       for x in range(1,6):
           if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))


    def getName(self):
        return self.name


    def getOneDesc(self):
        return self.oneDes


    def getDesc(self):
        return self.desc

    def getLog(self,log):
        self.log = log