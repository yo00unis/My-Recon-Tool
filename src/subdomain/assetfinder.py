
from globalEnv.globalEnv import GlobalEnv
from  general.general import General

class AssetFinder:
    
    
    def __init__(self):
        pass
    
    
    def Execute(self):
        command = f'assetfinder {GlobalEnv.GetDomain()} > {GlobalEnv.GetAssetFinder()}'
        General.ExecuteCommand(command, GlobalEnv.GetAssetFinder(), True)
        #return General.ExecuteRealTimeCommandAndSaveToFile(command, f'{GlobalEnv.GetAssetFinder()}', 'w', True)