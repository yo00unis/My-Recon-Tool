
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv


class Waybackurls:
    def __init__(self):
        pass
    
    def Execute(self):
        command = f'waybackurls {GlobalEnv.GetDomain()} > {GlobalEnv.GetWaybackurls()}'
        General.ExecuteCommand(command, GlobalEnv.GetWaybackurls(), False, False, True)
        #return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetWaybackurls()}', 'a', False, True)
    