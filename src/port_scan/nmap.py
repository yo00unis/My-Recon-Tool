
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv

class Nmap:
    
    
    def __init__(self):
        pass
    
    def Execute(self):
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'nmap -sA -sU -p {ports} -A -iL {GlobalEnv.GetPortScanningTarget()} -oN {GlobalEnv.GetNmap()}'
        else:    
            command = f'nmap -sA -sU --top-ports 10000 -A -iL {GlobalEnv.GetPortScanningTarget()} -oN {GlobalEnv.GetNmap()}'
        return General.ExecuteRealTimeCommand(command, False, False, False, '', True)