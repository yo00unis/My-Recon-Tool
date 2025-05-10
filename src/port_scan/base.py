
from general.general import General
from globalEnv.globalEnv import GlobalEnv
from port_scan.mass_scan import Masscan
from port_scan.nmap import Nmap
from files.files import Files


class PortScanningBase:
    def __init__(self):
        self.__CreateObjects()
    
    def __CreateObjects(self):
        self.__masscan = Masscan()
        self.__nmap = Nmap()
    
    
    def __ExportHttpxResultsToTargetFile(self):
        try:
            with open(f'{GlobalEnv.GetHttpx()}', 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    url = (((str(line)).split(' ['))[0]).strip()
                    domain = General.GetDomainFromUrl(url)
                    Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'w', General.getIPfromDomain(domain))
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    def __DoPortScanning(self):
        try:
            self.__ExportHttpxResultsToTargetFile()
            self.__masscan.Execute()
            self.__nmap.Execute()
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    def Exexute(self):
        self.__DoPortScanning()