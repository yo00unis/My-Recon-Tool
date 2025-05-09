
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv


class Waybackurls:
    def __init__(self):
        pass
    
    def Execute(self):
        command = f'waybackurls {GlobalEnv.GetDomain()}'
        return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetWaybackurls()}', 'a', False, True)
    