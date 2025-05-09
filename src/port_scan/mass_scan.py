
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv
import socket

from shared.shared import Shared

class Masscan:
    
    
    def __init__(self):
        pass


    def __get_ip(self, domain):
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.gaierror as e:
            print(f"Error resolving {domain}: {e}")
            return None
            
    def Execute(self, domain:str):
        command = f'masscan {str(self.__get_ip(General.GetStrippedString(domain)))} -p0-65535'
        return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetMasscan()}', 'w', False, False, False, '', True)