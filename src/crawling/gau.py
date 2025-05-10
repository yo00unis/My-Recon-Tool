
from  globalEnv.globalEnv import GlobalEnv
from  general.general import General


class Gau:
    
    def __init__(self):
        pass
    
    def Execute(self, url):
        command = f'gau {url} --subs --threads 15 --providers wayback,otx,commoncrawl --verbose --o {GlobalEnv.GetGau()}'
        General.ExecuteCommand(command, GlobalEnv.GetGau(), False, False, True)
        #return General.ExecuteRealTimeCommand(command, False, True)
    