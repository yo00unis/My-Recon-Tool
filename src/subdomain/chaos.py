from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class Chaos:
    
    def __init__(self):
        pass
    
    
    def Execute(self):
        command = f'chaos -d {GlobalEnv.GetDomain()} -o {GlobalEnv.GetChaos()}'
        General.ExecuteCommand(command, GlobalEnv.GetChaos(), True)
        #return General.ExecuteRealTimeCommand(command, True)