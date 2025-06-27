from commands import Commands
from files import Files
from general import General
from globalEnv import GlobalEnv


class ScreenShot:
    def __init__(self):
        pass

    def __prepareOperation(self):
        Files.WriteToFile(GlobalEnv.GetTempFile(), "w", "")
        if GlobalEnv.GetDoSubdomainEnumeration() or Files.IsFileExists(GlobalEnv.GetEnhancedHttpx()):
            Files.CopyFromTo(GlobalEnv.GetEnhancedHttpx(), GlobalEnv.GetTempFile())
        else:
            Files.WriteToFile(GlobalEnv.GetTempFile(), 'a', GlobalEnv.GetDomain())
        
        Files.RemoveDuplicateFromFile(GlobalEnv.GetTempFile())

    def __TakeSubdomainsScreenshot(self):
        commands = Commands.GowitnessCommands()
        for c in commands:
            General.ExecuteCommand(c)

    def Execute(self):
        self.__prepareOperation()
        self.__TakeSubdomainsScreenshot()
