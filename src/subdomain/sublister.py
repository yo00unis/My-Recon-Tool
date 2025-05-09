
from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class Sublist3r:
    
    def __init__(self):
        pass

    def Execute(self):
        command = f'sublist3r -d {GlobalEnv.GetDomain()} -t 10 -o {GlobalEnv.GetSublist3r()}'
        return General.ExecuteRealTimeCommand(command, True)