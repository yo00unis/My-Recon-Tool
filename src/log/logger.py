



class Logger:
    def __init__(self):
        pass
    
    @staticmethod
    def log(line):
        from globalEnv.globalEnv import GlobalEnv
        from files.files import Files
        
        s = f'{(str(line)).strip()}\n'
        Files().WriteToFile(GlobalEnv.GetLogFile(), 'a', s)
    
    @staticmethod        
    def logAndPrintToConsole(line):
        from globalEnv.globalEnv import GlobalEnv
        from general.general import General
        from files.files import Files
        
        s = f'{General().GetStrippedString(str(line))}\n'
        Files().WriteToFile(GlobalEnv.GetLogFile(), 'a', s)
        print(s, end='')
    
    @staticmethod
    def logPrintToConsoleAndSaveToFile(line:str):
        from general.general import General
        from globalEnv.globalEnv import GlobalEnv
        from files.files import Files
        
        s = f'{General().GetStrippedString(str(line))}\n'
        Files().WriteToFile(GlobalEnv.GetLogFile(), 'a', s)
        Files().WriteToFile(GlobalEnv.GetLogFile(), 'a', s)
        print(s, end='')