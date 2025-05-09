
from  globalEnv.globalEnv import GlobalEnv
from  general.general import General


class Katana:
    
    
    def __init__(self):
        pass

    def Execute(self, url):
        command = f'katana -u {General.GetStrippedString(url)} -d 100 -jc -delay 1 -c 15 -o {GlobalEnv.GetKatana()}'
        return General.ExecuteRealTimeCommand(command, False, True)
    

        
    
    