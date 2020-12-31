



class module_Example():
    def __init__(self, controller):
        self.controller= controller
        self.Settings = "hello"
        self.log = ""
        self.name = "Example Name"
        self.oneDes = "Example"
        #TODO change 
        self.desc = "Example"

    def createFrames(self):
        frameName=self.controller.createModFrame(0, __name__+"_1")
        self.controller.getFrameByName(frameName).update_Data(next=__name__+"_2",previous= None,title=self.getName(), intro=self.getOneDesc(), desc=self.getDesc())
        
        frameName=self.controller.createModFrame(2, __name__+"_2")
        self.controller.getFrameByName(frameName).update_Data(modController=self, next=__name__+"_3",previous= __name__+"_1",title="Hello Module", button_text="Run", button_command =0)
        
        frameName=self.controller.createModFrame(0, __name__+"_3")
        self.controller.getFrameByName(frameName).update_Data(next=__name__+"_1", previous=__name__+"_2",title="Hello Module", intro=self.getOneDesc(), desc=self.getDesc())
    
    def callBack(self, actionNumer):
        switcher={
            
        }
        switcher.get(actionNumer.get(), "Wrong Action")
            

    def exec(self):
        self.createFrames()
        self.controller.showFrame(__name__+"_1")
        print("Hello")

   
    def leaveMod(self):
        self.controller.showFrame("frame_modules")
        for x in range(1,6):
            if self.controller.getFrameByName(__name__+"_"+str(x)):
                self.controller.delFrameByName(__name__+"_"+str(x))




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

 

