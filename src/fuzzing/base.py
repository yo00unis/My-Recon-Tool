
from fuzzing.ffuf import FFUF
from globalEnv.globalEnv import GlobalEnv


class FuzzingBase:
    def __init__(self):
        self.__CreateObjects()
    
    def __CreateObjects(self):
        self.__ffuf = FFUF()
    
    def __DoFuzzing(self):
        try:
            with open(f'{GlobalEnv.GetHttpx()}', 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    url = (((str(line)).split(' ['))[0]).strip()
                    self.__ffuf.Execute(url)
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    def Exexute(self):
        self.__DoFuzzing()