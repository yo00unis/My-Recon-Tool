
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv
import os

from files.files import Files

class Masscan:
    
    
    def __init__(self):
        pass
            
    def Execute(self):
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'masscan -iL {GlobalEnv.GetPortScanningTarget()} -p {ports} > {GlobalEnv.GetMasscan()}'
        else:    
            command = f'masscan -p1-65535 -iL {GlobalEnv.GetPortScanningTarget()} > {GlobalEnv.GetMasscan()}'
        
        General.ExecuteCommand(command, GlobalEnv.GetMasscan(), False, True)
        #return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetMasscan()}', 'w', False, False, False, '', True)