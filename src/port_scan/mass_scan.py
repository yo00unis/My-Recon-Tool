
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv
import socket

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
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'masscan {str(self.__get_ip(General.GetStrippedString(domain)))} -p {ports}'
        else:    
            command = f'masscan {str(self.__get_ip(General.GetStrippedString(domain)))} --top-ports 100'
        return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetMasscan()}', 'w', False, False, False, '', True)