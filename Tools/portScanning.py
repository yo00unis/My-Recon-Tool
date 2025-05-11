
from commands import Commands
from files import Files
from general import General
from globalEnv import GlobalEnv


class PortScanning:
    def __init__(self):
        pass
    
    def __ExportHttpxResultsToTargetFile(self):
        try:
            with open(f'{GlobalEnv.GetHttpx()}', 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    url = (((str(line)).split(' ['))[0]).strip()
                    domain = General.GetDomainFromUrl(url)
                    Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'w', General.getIPfromDomain(domain))
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    def __Masscan(self):
        commands = Commands.MasscanCommands()
        for c in commands:        
            General.ExecuteCommand(c, GlobalEnv.GetMasscan(), False, True)
    
    def __Nmap(self):
        commands = Commands.NmapCommands()
        for c in commands:        
            General.ExecuteCommand(c, GlobalEnv.GetMasscan(), False, True)
    
    def Execute(self):
        self.__ExportHttpxResultsToTargetFile()
        self.__Masscan()
        self.__Nmap()