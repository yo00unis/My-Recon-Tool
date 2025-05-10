from  general.general import General
from globalEnv.globalEnv import GlobalEnv

class HTTPx:
    
    def __init__(self):
        pass
    
    def Execute(self):
        command = f'httpx -l {GlobalEnv.GetSubDomainsPath()} -status-code -title -tech-detect -follow-redirects -o {GlobalEnv.GetHttpx()}'
        General.ExecuteCommand(command, GlobalEnv.GetHttpx())
        #return General.ExecuteRealTimeCommand(command)