
from  globalEnv.globalEnv import GlobalEnv
from  general.general import General

class FFUF:
    
    def __init__(self):
        pass
    
    
    def Execute(self, url:str):
        if url.endswith('/'):
            url += 'FUZZ'
        else:
            url += '/FUZZ'
        command = f'ffuf -u {url} -p 2 -r -w {GlobalEnv.GetFuffWordlist()} -rate 20 -recursion -o {GlobalEnv.GetFFUF()}'
        General.ExecuteCommand(command, GlobalEnv.GetFFUF(), False, True, False, True)
        return General.ExecuteRealTimeCommand(command, False, True, True, url)
    