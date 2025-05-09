
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv
from shared.shared import Shared

class Nmap:
    
    
    def __init__(self):
        pass
    
    def Execute(self, domain:str):
        command = f'nmap {General.GetStrippedString(domain)}-oN {GlobalEnv.GetNmap()}'
        return General.ExecuteRealTimeCommand(command, False, False, False, '', True)