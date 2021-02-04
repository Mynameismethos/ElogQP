import internalModules.objects as objects
import internalModules.compare as compare
import internalModules.logwork as logwork
import threading

#TODO change name
#TODO Change Desc

class module_Polluted_Labels():
    def __init__(self, controller):
        self.controller = controller
        #TODO change
        self.name = "Polluted Labels"
        self.oneDes = "this programm checks The Event Names for Attributes in the Event name "
        self.desc = ""
        self.log = None
        self.visible=False
        self.started=False
        #EXAMPLE FOR LISTS
        self.listGroups = []
        ## Settings
        self.settings = {"minEventNamelength": 6,"MinRes" : 95,"min Occurence": 10, "eventTyp":"concept:name"}


        #TODO IMPLEMENT
        # EXAMPLE
    def createFrames(self):
 #Start Programm
        self.controller.createModFrame(2,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self,next=False, previous= True,title=self.getName(), button1_text="Search for Polluted Labels", button1_command =99, button2_text="Go To Next Module", button2_command =90)
        self.controller.getNextModFrame(__class__).set_Widgets_Visible(button2="no")
        #Settings
        self.controller.createModFrame(3,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= True,title=self.getName(), canDict=self.getSettings(), button3_text="Save", button3_command=80)
        #Greetings Page
        self.controller.createModFrame(0,__class__)
        self.controller.getNextModFrame(__class__).update_Data(modController=self, next=True,previous= False,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())

    #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher = {
            80: lambda: self.getSettingsFromFrame(),
            90: lambda: self.goToNext(),
            99: lambda: self.startSearch(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()

    def exec(self):
        self.createFrames()
        self.log=self.controller.getLog()
        self.visible=True
        self.controller.showModFrame(__class__,next=True)

    def startSearch(self):
        if(not self.started):
            self.started=True
            thread = threading.Thread(target=self.search, args=())
            thread.daemon = True
            thread.start()
            self.controller.getActiveModFrame(__class__).set_Widgets_Visible(button2="yes")

    def search(self):
        eventNames=logwork.getAllActivityAsList(self.log)
        subGroups=compare.all_Subgroups(eventNames,2,maxlen=2)
        popped=subGroups.pop()
        while(popped):
            sub=compare.largestSubstring(popped)
            if(len(sub)>int(self.settings["minEventNamelength"])):
                print(sub)
                g=objects.Group([])
                g.value=sub
                value=0
                for eName in reversed(eventNames):
                    if(sub in eName):
                        value+=1
                if(value>int(self.settings["min Occurence"])):
                    for eName in reversed(eventNames):
                        if(sub in eName):
                            eventNames.remove(eName)
                    self.listGroups.append(g)
                    subGroups=compare.all_Subgroups(eventNames,2,maxlen=2)
            popped=None
            if(subGroups):
                popped=subGroups.pop()
                   


        modErrorList=self.createErrorList(self.listGroups)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

   #TODO IMPLEMENT Create Error Objects
    def createErrorList(self, list):
        modErrorList = []
        for element in list:
            p_error = objects.error()
            p_error.set(trace="global",dictVal=element.getValue(), dictkey=self.settings["eventTyp"], classInfo=0,errorModul=self)
            modErrorList.append(p_error)
            for x in range(len(self.log)):
                eventlist= [u[self.settings["eventTyp"]] for u in self.log[x]]
                for eName in eventlist:
                    if(element.getValue() in eName):
                        c_error= objects.error()
                        c_error.set(trace=x,parent=p_error,dictVal=eName, dictkey=self.settings["eventTyp"], classInfo=0,errorModul=self)
                        modErrorList.append(c_error) 
        return modErrorList

 
  
    #TODO IMPLEMENT set Parameter to  start
    def clean(self): 
        self.log = None
        self.listGroups=[]
        self.started=False


    ##STOP IMPLEMENTING
    def leaveMod(self):
       print(__name__+": Module finished")
       self.controller.deleteModFrame(__class__)
       if(self.visible):
            self.controller.getFrameByName("frame_modules").showNextMod()
       self.clean()

    def goToNext(self):
        self.controller.getFrameByName("frame_modules").showNextMod()
        self.visible=False

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self):
        self.settings=self.controller.getActiveModFrame(__class__).getCanvasAsDict()

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getLog(self, log):
        self.log = log
