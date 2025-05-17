
from commands import Commands
from files import Files
from request import Requests
from general import General
from globalEnv import GlobalEnv


class SubdomainEnumeration:
    def __init__(self):
        from  files import Files
        self.__crtSHsiteUrl = f'https://crt.sh/json?q='
        self.__f = Files()
    
    def __CrtSh(self):
        response = Requests.Get(url=f"{self.__crtSHsiteUrl}{GlobalEnv.GetDomain()}")
        Files.SaveTextToFile(response.text, f"{GlobalEnv.GetCrtSH()}", 'w')
        Files.SaveTextToFile(response.text, f"{GlobalEnv.GetLogFile()}")
        if response.status_code == 200:
            domains = General.ExtractDomainsFromJsonFile(GlobalEnv.GetCrtSH())
            Files.WriteListToFile(GlobalEnv.GetSubDomainsPath(), 'a', domains)
            Files.WriteListToFile(GlobalEnv.GetCrtShText(), 'w', domains)
    
    def __Subfinder(self):
        commands = Commands.SubfinderCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetSubfinder(), True)
    
    def __Sublist3r(self):
        commands = Commands.Sublist3rCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetSublist3r(), True)
    
    def __Amass(self):
        commands = Commands.AmassCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetAmass())
    
    def __AssetFinder(self):
        commands = Commands.AssetFinderCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetAssetFinder(), True)
    
    def __Chaos(self):
        commands = Commands.ChaosCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetChaos(), True)
    
    def __Httpx(self):
        General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetSubDomainsPath())
        commands = Commands.HttpxCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetHttpx())
    
    
    def Execute(self):
        self.__CrtSh()
        self.__Subfinder()
        self.__Sublist3r()
        self.__AssetFinder()
        self.__Chaos()
        self.__Amass()
        self.__Httpx()