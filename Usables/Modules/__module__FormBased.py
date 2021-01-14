from tkinter import EventType
import internalModules.objects as objects

class module_FormBased():
    def __init__(self, controller):
        self.controller = controller
        #TODO change     
        self.name = "Form-based Event Capture"
        self.oneDes = "this programm checks For Form-based Event Capture"
        self.desc = ""
        self.log = None
        ## Settings
        self.settings = {"eventTime":"time:timestamp","eventTyp":"concept:name"}


        #TODO IMPLEMENT
        # EXAMPLE
    def createFrames(self):
        #Greetings Page
        frameName = self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, next=__name__+"_2", previous=None, title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        #Settings
        frameName = self.controller.createModFrame(3, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3", previous=__name__ +
                                                              "_1", title=self.getName(), canDict=self.getSettings(), button1_text="Save", button1_command=1)
        #Start Programm
        frameName = self.controller.createModFrame(2, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(
            modController=self, previous=__name__+"_2", title=self.getName(), button_text="Search for Distored Labels", button_command=99)

    #TODO IMPLEMENT
    def callBack(self, actionNumer):
        switcher = {

            80: lambda: self.displayPrev(__name__+"_4"),
            81: lambda: self.displayNext(__name__+"_4"),
            99: lambda: self.search(),
        }
        switcher.get(int(actionNumer.get()), lambda: print("Wrong Action"))()

    def exec(self):
        self.createFrames()
        self.log = self.controller.getLog()
        self.controller.showFrame(__name__+"_1")

    def search(self):
        eventTime = self.settings["eventTime"]
        groupList=[]
        groupDict={}
        eventTyp=self.settings["eventTyp"]
        for x in range(len(self.log)):
            blue=self.log[x]
            traceList= sorted(blue._list, key= lambda x:x[eventTime])
            for y in range(len(traceList)-1):
                elOne=traceList[y]
                elTwo=traceList[y+1]
                elOneName=elOne._dict[eventTyp]
                elTwoName=elTwo._dict[eventTyp]

                if(elOne[eventTime]==elTwo[eventTime]):
                    #test if already in a group:
                    if(elOneName in groupDict and elTwoName in groupDict):  #elOne in groupDict and elTwo in groupDict
                        #test if the same:
                        gOne=groupDict[elOneName]
                        gTwo=groupDict[elTwoName]
                        if(gOne == gTwo):
                            ##sameGroup, Do Nothing
                            pass
                        else:
                            #Add Group Two to Group One
                            for x in groupList[gTwo].getList():
                                groupDict[x]=gOne
                                groupList[gOne].addToList(x)
                            groupList[gTwo]=None
                    elif(elOneName in groupDict):
                        #Add elTwo to Group One
                        groupList[groupDict[elOneName]].addToList(elTwoName)
                    elif(elTwoName in groupDict):
                        #Add elTwo to Group One
                        groupList[groupDict[elTwoName]].addToList(elOneName)
                    else:
                        #Create New Group and add to Dict And List
                        g=objects.Group([elOneName, elTwoName])
                        index=len(groupList)
                        groupList.append(g)
                        groupDict[elOneName]=index
                        groupDict[elTwoName]=index
        #GroupList is now a comprehensiv List of simultaneous Events
        #Clean GroupList
        groupList= list(filter(None,groupList))


                
    #TODO set Group Names
        modErrorList=self.createErrorList(groupList)
        self.controller.addToErrorList(modErrorList)
        self.leaveMod()

    def createErrorList(self, list):
        modErrorList = []
        eventTyp=self.settings["eventTyp"]
        for element in list:
            #Create Group Error Object
            error_form = objects.error()
            error_form.set(trace="global",desc="FormBased", dictVal=element.getName(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error_form)
            #Create Event Error
            errorDict ={}
            for event in element.getList():
                error_event= objects.error()
                error_event.set(trace="global",desc="TODO",parent=error_form,dictVal=event,errorModul=self)
                errorDict[event]=error_event
                modErrorList.append(error_event)
            #Create Instance Error
            for x in range(len(self.log)):
                for y in range(len(self.log[x])):
                    if(self.log[x][y][eventTyp] in element.getList()):
                        parent=errorDict[self.log[x][y][eventTyp]]
                        error_child = objects.error()
                        error_child.set(trace=x,parent=parent, dictVal=self.log[x][y][eventTyp],dictkey=eventTyp,errorModul=self)
                        modErrorList.append(error_child)

            
           
        return modErrorList

    #TODO IMPLEMENT Create Error Objects and Add TO ERRORLIST
    def addToErrorList(self, list):
        modErrorList = []
        for element in list:
            error = objects.error()
            error.set(trace=element.getTrace(), event=element.getEvent(), dictVal=element.getValue(
            ), dictkey=element.getTyp(), classInfo=element.getName(), errorModul=self)
            modErrorList.append(error)
        self.controller.addToErrorList(modErrorList)
  
    #TODO IMPLEMENT set Parameter to  start
    def clean(self): 
        self.log = None


    ##STOP IMPLEMENTING

    def leaveMod(self):
       self.controller.deleteModFrame()
       self.controller.getFrameByName("frame_modules").showNextMod()

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings

    def getSettingsFromFrame(self,settingPage):
        self.settings = self.controller.getFrameByName(
            __name__+"_"+settingPage).getSettings()

    def getName(self):
        return self.name

    def getOneDesc(self):
        return self.oneDes

    def getDesc(self):
        return self.desc

    def getLog(self, log):
        self.log = log
