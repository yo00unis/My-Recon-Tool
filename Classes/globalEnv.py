class GlobalEnv:

    def __init__():
        pass

    __ResultFolder = f""
    __Domain = f""
    __LogFile = f""
    __SubDomainsFile = f""
    __SubDomainsFolder = f""
    __CrawlingFolder = f""
    __PortScanningFolder = f""
    __FuzzingFolder = f""
    __CrtSH = f""
    __CrtSHText = f""
    __ffufWordlist = f""
    __DoSubdomainEnumeration = True
    __doPortScanning = True
    __doCrawling = True
    __doFuzzing = True
    __TakeScreenShots = True
    __ports = f""
    __portScanningARecords = f""
    __gowitness = ""
    __httpx_path = ""
    __dns_path = ""
    __max_threads = 0

    @staticmethod
    def SetMaxThreads(threads:int):
        GlobalEnv.__max_threads = threads

    @staticmethod
    def GetMaxThreads():
        return GlobalEnv.__max_threads

    @staticmethod
    def SetDNSPath(rf:str):
        GlobalEnv.__dns_path = rf.strip()

    @staticmethod
    def GetDNSPath():
        return GlobalEnv.__dns_path

    @staticmethod
    def SetHttpxPath(rf:str):
        GlobalEnv.__httpx_path = rf.strip()

    @staticmethod
    def GetHttpxPath():
        return GlobalEnv.__httpx_path

    # screenshot tools
    @staticmethod
    def SetGowitness(rf:str):
        GlobalEnv.__gowitness = rf.strip()

    @staticmethod
    def GetGowitness():
        return GlobalEnv.__gowitness

    # subdomain enumeration tools
    @staticmethod
    def SetCrtSH(rf:str):
        GlobalEnv.__CrtSH = rf.strip()

    @staticmethod
    def GetCrtSH():
        return GlobalEnv.__CrtSH

    @staticmethod
    def SetCrtShText(d:str):
        GlobalEnv.__CrtSHText = d.strip()

    @staticmethod
    def GetCrtShText():
        return GlobalEnv.__CrtSHText

    # log file
    @staticmethod
    def SetLogFile(rf:str):
        GlobalEnv.__LogFile = rf.strip()

    @staticmethod
    def GetLogFile():
        return GlobalEnv.__LogFile

    # config
    @staticmethod
    def SetResultFolder(rf):
        if not rf.endswith("/"):
            rf += "/"
        GlobalEnv.__ResultFolder = rf.strip()

    @staticmethod
    def GetResultFolder():
        return GlobalEnv.__ResultFolder

    @staticmethod
    def SetDomain(d:str):
        GlobalEnv.__Domain = d.strip()

    @staticmethod
    def GetDomain():
        return GlobalEnv.__Domain

    @staticmethod
    def SetPortScanningARecords(rf:str):
        GlobalEnv.__portScanningARecords = rf.strip()

    @staticmethod
    def GetPortScanningARecords():
        return GlobalEnv.__portScanningARecords

    @staticmethod
    def SetPorts(rf:str):
        GlobalEnv.__ports = rf.strip()

    @staticmethod
    def GetPorts():
        return GlobalEnv.__ports

    @staticmethod
    def SetDoSubdomainEnumeration(flag:bool):
        GlobalEnv.__DoSubdomainEnumeration = flag

    @staticmethod
    def GetDoSubdomainEnumeration():
        return GlobalEnv.__DoSubdomainEnumeration

    @staticmethod
    def SetDoPortScanning(flag:bool):
        GlobalEnv.__doPortScanning = flag

    @staticmethod
    def GetDoPortScanning():
        return GlobalEnv.__doPortScanning

    @staticmethod
    def SetDoCrawling(flag:bool):
        GlobalEnv.__doCrawling = flag

    @staticmethod
    def GetDoCrawling():
        return GlobalEnv.__doCrawling

    @staticmethod
    def SetDoFuzzing(flag:bool):
        GlobalEnv.__doFuzzing = flag

    @staticmethod
    def GetDoFuzzing():
        return GlobalEnv.__doFuzzing

    @staticmethod
    def SetTakeScreenShots(flag:bool):
        GlobalEnv.__TakeScreenShots = flag

    @staticmethod
    def GetTakeScreenShots():
        return GlobalEnv.__TakeScreenShots

    @staticmethod
    def SetSubDomainsFile(rf:str):
        GlobalEnv.__SubDomainsFile = rf.strip()

    @staticmethod
    def GetSubDomainsFile():
        return GlobalEnv.__SubDomainsFile
    
    # Set result folders
    @staticmethod
    def SetCrawlingFolderPath(rf:str):
        GlobalEnv.__CrawlingFolder = rf.strip()

    @staticmethod
    def GetCrawlingFolderPath():
        return GlobalEnv.__CrawlingFolder
    
    @staticmethod
    def SetFuzzingFolderPath(rf:str):
        GlobalEnv.__FuzzingFolder = rf.strip()

    @staticmethod
    def GetFuzzingFolderPath():
        return GlobalEnv.__FuzzingFolder
    
    @staticmethod
    def SetPortScanningFolderPath(rf:str):
        GlobalEnv.__PortScanningFolder = rf.strip()

    @staticmethod
    def GetPortScanningFolderPath():
        return GlobalEnv.__PortScanningFolder
    
    @staticmethod
    def SetSubDomainsFolderPath(rf:str):
        GlobalEnv.__SubDomainsFolder = rf.strip()

    @staticmethod
    def GetSubDomainsFolderPath():
        return GlobalEnv.__SubDomainsFolder

    @staticmethod
    def SetFuffWordlist(rf:str):
        GlobalEnv.__ffufWordlist = rf.strip()

    @staticmethod
    def GetFuffWordlist():
        return GlobalEnv.__ffufWordlist
