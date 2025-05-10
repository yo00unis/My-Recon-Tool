
from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class Subfinder:
    def __init__(self):
        pass

    def Execute(self):
        command = f'subfinder -d {GlobalEnv.GetDomain()} -o {GlobalEnv.GetSubfinder()}'
        General.ExecuteCommand(command, GlobalEnv.GetSubfinder(), True)
        #return General.ExecuteRealTimeCommand(command, True)