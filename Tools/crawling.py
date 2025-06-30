import re
from commands import Commands
from files import Files
from globalEnv import GlobalEnv
from general import General


class Crawling:
    def __init__(self):
        pass

    def __Katana(self, url):
        commands = Commands.KatanaCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetKatana(), False, False, True)

    def __Gau(self, url):
        commands = Commands.GauCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetGau(), False, False, True)

    def __GoSpider(self, url):
        commands = Commands.GoSpiderCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetGoSpider(), False, False, True)

    def __Waybackurls(self):
        commands = Commands.WaybackurlsCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetWaybackurls(), False, False, True)

    def __prepare(self):
        if (
            Files.IsFileExists(GlobalEnv.GetEnhancedHttpx())
            and Files.IsFileEmpty(GlobalEnv.GetEnhancedHttpx())
        ) or not Files.IsFileExists(GlobalEnv.GetEnhancedHttpx()):
            Files.WriteToFile(
                GlobalEnv.GetEnhancedHttpx(), "a", GlobalEnv.GetDomain()
            )
        Files.RemoveDuplicateFromFile(GlobalEnv.GetEnhancedHttpx())

    def Execute(self):
        self.__prepare()
        try:
            with open(
                f"{GlobalEnv.GetHttpx()}", "r", encoding="utf-8", errors="ignore"
            ) as f:
                for line in f:
                    url = (((str(line)).split(" ["))[0]).strip()
                    self.__Katana(url)
                    self.__Gau(url)
                    self.__GoSpider(url)
            self.__Waybackurls()
            General.FilterResultFile(GlobalEnv.GetWaybackurls())
        except Exception as e:
            print(f"Error running: {str(e)}")
