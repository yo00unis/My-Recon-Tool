
from commands import Commands
from general import General
from globalEnv import GlobalEnv


class Fuzzing:
    def __init__(self):
        pass
    
    def __FFUF(self, url):
        commands = Commands.FFUFCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetFFUF(), False, True, False, True)
    
    def Execute(self):
        try:
            with open(f'{GlobalEnv.GetHttpx()}', 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    url = (((str(line)).split(' ['))[0]).strip()
                    self.__FFUF(url)
        except Exception as e:
            print(f"Error running: {str(e)}")
        