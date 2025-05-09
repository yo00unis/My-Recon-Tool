
from general.general import General
from globalEnv.globalEnv import GlobalEnv

class Waymore:
    
    def __init__(self):
        pass
    
    def Execute(self):
        command = f'waymore -i {GlobalEnv.GetDomain()} -l 5 -mode U -t 15 -oU {GlobalEnv.GetWaymore()}'
        return General.ExecuteRealTimeCommand(command)
    