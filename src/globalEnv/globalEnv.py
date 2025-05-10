
 



class GlobalEnv:
    
    def __init__( ):
        pass
    
    __ResultFolder = f''
    __Domain = f''
    __LogFile = f''
    __SubDomainsFile = f''
    __SubFinder = f''
    __Sublist3r = f''
    __Chaos = f''
    __Httpx = f''
    __Waybackurls = f''
    __Katana = f''
    __Gau = f''
    __GoSpider = f''
    __CrtSH = f''
    __ffuf = f''
    __ffufWordlist = f''
    __crawlingPath = f''
    __fuzzingPath = f''
    __portScanningPath = f''
    __nmap = f''
    __masscan = f''
    __amass = f''
    __theHarvester = f''
    __assetFinder = f''
    __waymore = f''
    __isWildCard = True
    __ports = f''
    
    @staticmethod
    def SetResultFolder(   rf):
        if not rf.endswith('/'): 
            rf += '/'
        from general.general import General
         
        GlobalEnv.__ResultFolder = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetResultFolder( ):
        return GlobalEnv.__ResultFolder
    
    @staticmethod
    def SetDomain(   d:str):
        from general.general import General
         
        GlobalEnv.__Domain = General.GetStrippedString(d)
        
    @staticmethod
    def GetDomain( ):
        return GlobalEnv.__Domain
    
    @staticmethod
    def SetLogFile(   lf):
        from general.general import General
         
        GlobalEnv.__LogFile = General.GetStrippedString(lf) 
    
    @staticmethod
    def GetLogFile( ):
        return GlobalEnv.__LogFile
    
    @staticmethod
    def SetPorts(lf):
        from general.general import General
        GlobalEnv.__ports = General.GetStrippedString(lf) 
    
    @staticmethod
    def GetPorts( ):
        return GlobalEnv.__ports
    
    @staticmethod
    def SetIsWildCard(lf):
        from general.general import General
        if General.GetStrippedString(lf) == "1":
            GlobalEnv.__isWildCard = True
        else:
            GlobalEnv.__isWildCard = False
    
    @staticmethod
    def GetIsWildcard():
        return GlobalEnv.__isWildCard
    
    
    @staticmethod 
    def SetAssetFinder(   lf):
        from general.general import General
         
        GlobalEnv.__assetFinder = General.GetStrippedString(lf) 
    
    @staticmethod  
    def GetAssetFinder( ):
        return GlobalEnv.__assetFinder
    
    @staticmethod
    def SetWaymore(   lf):
        from general.general import General
          
        GlobalEnv.__waymore = General.GetStrippedString(lf) 
    
    @staticmethod
    def GetWaymore( ):
        return GlobalEnv.__waymore
    
    @staticmethod
    def SetSubDomainsPath(   rf):
        from general.general import General
         
        GlobalEnv.__SubDomainsFile = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetSubDomainsPath( ):
        return GlobalEnv.__SubDomainsFile
    
    @staticmethod 
    def SetCrtSH(   rf):
        from general.general import General
          
        GlobalEnv.__CrtSH = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetCrtSH( ):
        return GlobalEnv.__CrtSH
    
    @staticmethod 
    def SetSubfinder(   rf):
        from general.general import General
         
        GlobalEnv.__SubFinder = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetSubfinder( ):
        return GlobalEnv.__SubFinder
    
    @staticmethod 
    def SetSublist3r(   rf):
        from general.general import General
        GlobalEnv.__Sublist3r = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetSublist3r( ):
        return GlobalEnv.__Sublist3r
    
    @staticmethod
    def SetChaos(   rf):
        from general.general import General
          
        GlobalEnv.__Chaos = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetChaos( ):
        return GlobalEnv.__Chaos
    
    @staticmethod 
    def SetWaybackurls(   rf):
        from general.general import General
          
        GlobalEnv.__Waybackurls = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetWaybackurls( ):
        return GlobalEnv.__Waybackurls
    
    @staticmethod 
    def SetKatana(   rf):
        from general.general import General
         
        GlobalEnv.__Katana = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetKatana( ):
        return GlobalEnv.__Katana
    
    @staticmethod 
    def SetGau(   rf):
        from general.general import General
          
        GlobalEnv.__Gau = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetGau( ):
        return GlobalEnv.__Gau
    
    @staticmethod 
    def SetGoSpider(   rf):
        from general.general import General
          
        GlobalEnv.__GoSpider = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetGoSpider( ):
        return GlobalEnv.__GoSpider
    
    @staticmethod 
    def SetHttpx(   rf):
        from general.general import General
          
        GlobalEnv.__Httpx = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetHttpx( ):
        return GlobalEnv.__Httpx
    
    @staticmethod 
    def SetFFUF(   rf):
        from general.general import General
          
        GlobalEnv.__ffuf = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetFFUF( ):
        return GlobalEnv.__ffuf
    
    @staticmethod
    def SetCrawlingPath(   rf):
        from general.general import General
         
        GlobalEnv.__crawlingPath = General.GetStrippedString(rf) 
    
    @staticmethod
    def GetCrawlingPath( ):
        return GlobalEnv.__crawlingPath
    
    @staticmethod 
    def SetFuzzingPath(   rf):
        from general.general import General
          
        GlobalEnv.__fuzzingPath = General.GetStrippedString(rf) 
    
    @staticmethod  
    def GetFuzzingPath( ):
        return GlobalEnv.__fuzzingPath
    
    @staticmethod 
    def SetFuffWordlist(   rf):
        from general.general import General
          
        GlobalEnv.__ffufWordlist = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetFuffWordlist( ):
        return GlobalEnv.__ffufWordlist
    
    @staticmethod 
    def SetNmap(   rf):
        from general.general import General
         
        GlobalEnv.__nmap = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetNmap( ):
        return GlobalEnv.__nmap
    
    @staticmethod 
    def SetPortScanningPath(   rf):
        from general.general import General
          
        GlobalEnv.__portScanningPath = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetPortScanningPath( ):
        return GlobalEnv.__portScanningPath
    
    @staticmethod 
    def SetMasscan(   rf):
        from general.general import General
          
        GlobalEnv.__masscan = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetMasscan( ):
        return GlobalEnv.__masscan
    
    @staticmethod 
    def SetAmass(   rf):
        from general.general import General
         
        GlobalEnv.__amass = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GetAmass( ):
        return GlobalEnv.__amass
    
    @staticmethod 
    def SettheHarvester(rf):
        from general.general import General
          
        GlobalEnv.__theHarvester = General.GetStrippedString(rf) 
    
    @staticmethod 
    def GettheHarvester():
        return GlobalEnv.__theHarvester