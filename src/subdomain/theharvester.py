
from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class TheHarvester:

    def __init__(self):
        pass
    
    def Execute(self):
        #command = f'python F:\\Hacking\\theHarvester-master\\theHarvester.py -d {GlobalEnv.GetGlobalEnv.GetDomain()().strip()} -s --screenshot {GlobalEnv.GetResultFolder().strip()} -t -n -c -b all -f {GlobalEnv.GetResultFolder().strip()}theHarvester'
        command = f'python F:\\Hacking\\theHarvester-master\\theHarvester.py -d {GlobalEnv.GetDomain()} -b all -f {GlobalEnv.GettheHarvester()}'
        return General.ExecuteRealTimeCommand(command, True)