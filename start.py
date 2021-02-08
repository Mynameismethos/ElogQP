from internalModules.Frame_Controller import Frame_Controller
import internalModules.loadmodules as loadmodules
import internalModules.loadLog as loadLog
import internalModules.Data as dataBase


#init the Display and load the singular fames
class Display(Frame_Controller):
    def __init__(self, *args, **kwargs):
        self.data=dataBase
        self.data.modFrames = loadmodules.loadFrames()
        Frame_Controller.__init__(self, *args, **kwargs)

        

    def addToErrorList(self, modErrorList):
        #Check if Entrys already Exist
        for x in modErrorList:
            hash_x= hash(x)
            if(hash_x not in self.data.error_Hash_Dict):
                self.data.error_List.append(x)
                self.data.error_Hash_Dict[hash_x]=x


    def get_xes_file_list(self):
        list = loadLog.getAllLogs()
        self.getFrameByName("frame_start").updateData(list)

    def import_xes_Log(self, button, name):
        self.data.log = loadLog.loadLogByName(self,name,button)


    def importModule(self, button):
        self.data.module_List = loadmodules.loadmodules(self)
        for module in self.data.module_List:
            print(
                "This Module is called: '"
                + module.getName()
                + "' it´s descibed as: "
                + module.getOneDesc()
            )
        moduleName="frame_start"
        successfull = len(self.data.module_List) > 0
        if successfull:
            self.data.frames[moduleName].button_feedback(button, True)
        else:
            self.data.frames[moduleName].button_feedback(button, False)

    def getModules(self):
        return self.data.module_List

    def getErrorList(self):
        return self.data.error_List
    def clearErrorList(self):
        self.data.error_List=[]
        self.data.error_Hash_Dict={}

    def getLog(self):
        return self.data.log

    def setLog(self, log, button=None,name=None):
        if(button):
            self.data.frames["frame_start"].button_feedback(button, True)
            self.data.frames["frame_start"].updateData(highlight=name)
        self.data.log = log


# Start of Programm
app = Display()
app.mainloop()
