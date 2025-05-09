
from general.general import General
from globalEnv.globalEnv import GlobalEnv
from port_scan.mass_scan import Masscan
from port_scan.nmap import Nmap


class PortScanningBase:
    def __init__(self):
        self.__CreateObjects()
    
    def __CreateObjects(self):
        self.__masscan = Masscan()
        self.__nmap = Nmap()
    
    def __DoPortScanning(self):
        try:
            with open(f'{GlobalEnv.GetHttpx()}', 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    url = (((str(line)).split(' ['))[0]).strip()
                    domain = General.GetDomainFromUrl(url)
                    self.__nmap.Execute(domain=domain)
                    self.__masscan.Execute(domain=domain)
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    def Exexute(self):
        self.__DoPortScanning()