from commands import Commands
from files import Files
from general import General
from globalEnv import GlobalEnv


class PortScanning:
    def __init__(self):
        pass
    
    def __ReadSubdomains(self):
        if not GlobalEnv.GetDoSubdomainEnumeration():
            if Files.IsFileExists(GlobalEnv.GetSubDomainsPath()):
                    Files.CopyFromTo(GlobalEnv.GetSubDomainsPath(), GlobalEnv.GetHttpx())
        Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx())
                    
    def __ExportHttpxResultsToTargetFile(self):
        try:
            self.__ReadSubdomains()
            Files.WriteToPortScanningTargetFile()
            Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTarget())
            Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTargetDomains())
        except Exception as e:
            print(f"Error running: {str(e)}")

    def __Masscan(self):
        commands = Commands.MasscanCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetMasscan(), False, True)

    def __Nmap(self):
        commands = Commands.NmapCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetNmap(), False, True)

    def __Naabu(self):
        commands = Commands.NaabuCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetNaabu(), False, True)


    def Execute(self):
        self.__ExportHttpxResultsToTargetFile()
        # self.__Masscan()
        # self.__Nmap()
        # self.__Naabu()
