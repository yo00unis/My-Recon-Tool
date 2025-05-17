from commands import Commands
from files import Files
from general import General
from globalEnv import GlobalEnv


class PortScanning:
    def __init__(self):
        pass

    def __ExportHttpxResultsToTargetFile(self):
        try:
            httpxlines = Files.GetNumberOfLines(GlobalEnv.GetHttpx())
            if httpxlines == 0 or httpxlines == 1:
                if Files.IsFileExists(GlobalEnv.GetSubDomainsPath()):
                    Files.CopyFromTo(GlobalEnv.GetSubDomainsPath(), GlobalEnv.GetHttpx())
            Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx())
            with open(
                f"{GlobalEnv.GetHttpx()}", "r", encoding="utf-8", errors="ignore"
            ) as f:
                for line in f:
                    url = (((str(line)).split(" ["))[0]).strip()
                    domain = General.GetDomainFromUrl(url)
                    Files.WriteToFile(
                        GlobalEnv.GetPortScanningTarget(),
                        "a",
                        General.getIPfromDomain(domain),
                    )
                    Files.WriteToFile(
                        GlobalEnv.GetPortScanningTargetDomains(),
                        "a",
                        domain,
                    )
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
        self.__Masscan()
        self.__Nmap()
        self.__Naabu()
