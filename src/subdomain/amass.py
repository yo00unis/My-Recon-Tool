


from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class Amass:
    
    def __init__(self):
        
        pass
    
    def Execute(self):
        command = f'amass enum -passive -d {GlobalEnv.GetDomain()} -o {GlobalEnv.GetAmass()}'
        return General.ExecuteRealTimeCommand(command, True)