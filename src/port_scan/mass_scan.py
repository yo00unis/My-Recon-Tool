
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv

class Masscan:
    
    
    def __init__(self):
        pass
            
    def Execute(self):
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'masscan -iL {GlobalEnv.GetPortScanningTarget()} -p {ports}'
        else:    
            command = f'masscan -p1-65535 -iL {GlobalEnv.GetPortScanningTarget()}'
        return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetMasscan()}', 'w', False, False, False, '', True)