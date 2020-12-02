from internalModules.Frame_Controller import Frame_Controller
from internalModules.loadmodules import *
from internalModules.loadLog import *
import internalModules.Data as dataBase


class Controll(Frame_Controller):
    """
    The Class is the starting Point for ElogQP and the main controlling point
    """
    def __init__(self, *args, **kwargs):
        self.data=dataBase
        self.data.modFrames = loadFrames()
        Frame_Controller.__init__(self, *args, **kwargs)

        

    def addToErrorList(self, modErrorList):
        """
        Function to control which Erros get added to the Persistenz

        The function hashes each Error code, and checks if the Error already exists in the database
        """

        if(self.data.errorRate>3):self.data.errorRate=3
        #Check if Entrys already Exist
        for x in modErrorList:
            hash_x= hash(x)
            if(hash_x not in self.data.error_Hash_Dict):
                self.data.error_List.append(x)
                self.data.error_Hash_Dict[hash_x]=len(self.data.error_List)


    def get_xes_file_list(self):
        """
        Function to list all XES Files in the directory
        """
        list = getAllLogs()
        self.getFrameByName("frame_start").updateData(list)

    def import_xes_Log(self, button, name):
        """
        Function to start import of XES by a given name
        
        a button can be provided to get feedback about the import

        """
        self.data.log = loadLogByName(self,name,button)


    def importModule(self, button):
        """
        function to import all Errormodules in the set directory
        """
        self.data.module_List = loadmodules(self)
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

        
    def clearErrorList(self):
        """
        Function to reset the error List and all corresponding values
        """
        self.data.errorRate=4
        self.data.error_List=[]
        self.data.error_Hash_Dict={}

    #############  Getter + Setter Functions ##############

    def getLog(self):
        return self.data.log

    def getModules(self):
        return self.data.module_List

    def getErrorList(self):
        return self.data.error_List
    
    def setLog(self, log, button=None,name=None):
        if(button):
            self.data.frames["frame_start"].button_feedback(button, True)
            self.data.frames["frame_start"].updateData(highlight=name)
        self.data.log = log


# Start of Programm
app = Controll()
app.mainloop()
