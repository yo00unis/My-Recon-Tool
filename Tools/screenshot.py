from commands import Commands
from files import Files
from general import General
from globalEnv import GlobalEnv


class ScreenShot:
    def __init__(self):
        pass

    def __prepareOperation(self):
        Files.WriteToFile(GlobalEnv.GetTempFile(), 'w', '')
        Files.WriteToFile(GlobalEnv.GetTempFile(), 'a', GlobalEnv.GetDomain())
        if Files.IsFileExists(GlobalEnv.GetHttpx()):
            Files.WriteListToFile(GlobalEnv.GetTempFile(), 'a', General.GetDomainsFromHttpxFile())
        if Files.IsFileExists(GlobalEnv.GetSubDomainsPath()) and not GlobalEnv.GetDoSubdomainEnumeration():
            General.FilterResultFile(GlobalEnv.GetSubDomainsPath())
            Files.CopyFromTo(GlobalEnv.GetSubDomainsPath(), GlobalEnv.GetTempFile())

        Files.RemoveDuplicateFromFile(GlobalEnv.GetTempFile())

    def __TakeSubdomainsScreenshot(self):
        commands = Commands.GowitnessCommands()
        for c in commands:
            General.ExecuteCommand(c)

    def Execute(self):
        self.__prepareOperation()
        self.__TakeSubdomainsScreenshot()
