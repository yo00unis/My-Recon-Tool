
from  general.requests import Requests
from globalEnv.globalEnv import GlobalEnv

class CrtSH:
    
    def __init__(self):
        from  files.files import Files
        self.__crtSHsiteUrl = f'https://crt.sh/json?q='
        self.__f = Files()
    
    def Execute(self):
        response = Requests.Get(url=f"{self.__crtSHsiteUrl}{GlobalEnv.GetDomain()}")
        self.__f.SaveTextToFile(response.text, f"{GlobalEnv.GetCrtSH()}")
        self.__f.SaveTextToFile(response.text, f"{GlobalEnv.GetLogFile()}")
        return True
    
    
        