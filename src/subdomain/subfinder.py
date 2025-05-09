
from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class Subfinder:
    def __init__(self):
        pass

    def Execute(self):
        command = f'subfinder -d {GlobalEnv.GetDomain()} -o {GlobalEnv.GetSubfinder()}'
        return General.ExecuteRealTimeCommand(command, True)