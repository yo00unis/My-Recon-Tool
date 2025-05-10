
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv

class Nmap:
    
    
    def __init__(self):
        pass
    
    def Execute(self, domain:str):
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'nmap -p {ports} -A {General.GetStrippedString(domain)} -oN {GlobalEnv.GetNmap()}'
        else:    
            command = f'nmap --top-ports 1000 {General.GetStrippedString(domain)} -oN {GlobalEnv.GetNmap()}'
        return General.ExecuteRealTimeCommand(command, False, False, False, '', True)