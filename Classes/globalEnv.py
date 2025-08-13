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
    __portScanningTarget = f""
    __portScanningTargetDomains = f""
    __tempFile = f""
    __tempJson = f""
    __dnsRecords = f""
    __gowitness = ""
    __httpx_path = ""
    __dns_path = ""

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

    @staticmethod
    def SetDnsRecords(rf:str):
        GlobalEnv.__dnsRecords = rf.strip()

    @staticmethod
    def GetDnsRecords():
        return GlobalEnv.__dnsRecords

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

    # temp files
    @staticmethod
    def SetTempFile(d:str):
        GlobalEnv.__tempFile = d.strip()

    @staticmethod
    def GetTempFile():
        return GlobalEnv.__tempFile

    @staticmethod
    def SetTempJson(d:str):
        GlobalEnv.__tempJson = d.strip()

    @staticmethod
    def GetTempJson():
        return GlobalEnv.__tempJson

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
    def SetPortScanningTargetDomains(d:str):
        GlobalEnv.__portScanningTargetDomains = d.strip()

    @staticmethod
    def GetPortScanningTargetDomains():
        return GlobalEnv.__portScanningTargetDomains

    @staticmethod
    def SetPortScanningTarget(rf:str):
        GlobalEnv.__portScanningTarget = rf.strip()

    @staticmethod
    def GetPortScanningTarget():
        return GlobalEnv.__portScanningTarget

    @staticmethod
    def SetPorts(rf:str):
        GlobalEnv.__ports = rf.strip()

    @staticmethod
    def GetPorts():
        return GlobalEnv.__ports

    @staticmethod
    def SetDoSubdomainEnumeration(rf:str):
        if rf.strip() == "1":
            GlobalEnv.__DoSubdomainEnumeration = True
        else:
            GlobalEnv.__DoSubdomainEnumeration = False

    @staticmethod
    def GetDoSubdomainEnumeration():
        return GlobalEnv.__DoSubdomainEnumeration

    @staticmethod
    def SetDoPortScanning(rf:str):
        if rf.strip() == "0":
            GlobalEnv.__doPortScanning = False
        else:
            GlobalEnv.__doPortScanning = True

    @staticmethod
    def GetDoPortScanning():
        return GlobalEnv.__doPortScanning

    @staticmethod
    def SetDoCrawling(rf:str):
        if rf.strip() == "0":
            GlobalEnv.__doCrawling = False
        else:
            GlobalEnv.__doCrawling = True

    @staticmethod
    def GetDoCrawling():
        return GlobalEnv.__doCrawling

    @staticmethod
    def SetDoFuzzing(rf:str):
        if rf.strip() == "0":
            GlobalEnv.__doFuzzing = False
        else:
            GlobalEnv.__doFuzzing = True

    @staticmethod
    def GetDoFuzzing():
        return GlobalEnv.__doFuzzing

    @staticmethod
    def SetTakeScreenShots(rf:str):
        if rf.strip() == "0":
            GlobalEnv.__TakeScreenShots = False
        else:
            GlobalEnv.__TakeScreenShots = True

    @staticmethod
    def GetTakeScreenShots():
        return GlobalEnv.__TakeScreenShots

    @staticmethod
    def SetSubDomainsPath(rf:str):
        GlobalEnv.__SubDomainsFile = rf.strip()

    @staticmethod
    def GetSubDomainsPath():
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
