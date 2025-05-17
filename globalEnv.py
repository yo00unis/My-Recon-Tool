class GlobalEnv:

    def __init__():
        pass

    __ResultFolder = f""
    __Domain = f""
    __LogFile = f""
    __SubDomainsFile = f""
    __SubFinder = f""
    __Sublist3r = f""
    __Chaos = f""
    __Httpx = f""
    __Waybackurls = f""
    __Katana = f""
    __Gau = f""
    __GoSpider = f""
    __CrtSH = f""
    __CrtSHText = f""
    __ffuf = f""
    __ffufWordlist = f""
    __crawlingPath = f""
    __fuzzingPath = f""
    __portScanningPath = f""
    __nmap = f""
    __masscan = f""
    __amass = f""
    __theHarvester = f""
    __assetFinder = f""
    __waymore = f""
    __DoSubdomainEnumeration = True
    __doPortScanning = True
    __doCrawling = True
    __doFuzzing = True
    __ports = f""
    __portScanningTarget = f""
    __portScanningTargetDomains = f""
    __tempFile = f""
    __tempJson = f""
    __naabu = f""

    # port scanning tools
    @staticmethod
    def SetNmap(rf):
        from general import General

        GlobalEnv.__nmap = General.GetStrippedString(rf)

    @staticmethod
    def GetNmap():
        return GlobalEnv.__nmap

    @staticmethod
    def SetNaabu(d: str):
        from general import General

        GlobalEnv.__naabu = General.GetStrippedString(d)

    @staticmethod
    def GetNaabu():
        return GlobalEnv.__naabu

    @staticmethod
    def SetMasscan(rf):
        from general import General

        GlobalEnv.__masscan = General.GetStrippedString(rf)

    @staticmethod
    def GetMasscan():
        return GlobalEnv.__masscan

    # subdomain enumeration tools
    @staticmethod
    def SetCrtSH(rf):
        from general import General

        GlobalEnv.__CrtSH = General.GetStrippedString(rf)

    @staticmethod
    def GetCrtSH():
        return GlobalEnv.__CrtSH

    @staticmethod
    def SetCrtShText(d: str):
        from general import General

        GlobalEnv.__CrtSHText = General.GetStrippedString(d)

    @staticmethod
    def GetCrtShText():
        return GlobalEnv.__CrtSHText

    @staticmethod
    def SetAssetFinder(lf):
        from general import General

        GlobalEnv.__assetFinder = General.GetStrippedString(lf)

    @staticmethod
    def GetAssetFinder():
        return GlobalEnv.__assetFinder

    @staticmethod
    def SetSubfinder(rf):
        from general import General

        GlobalEnv.__SubFinder = General.GetStrippedString(rf)

    @staticmethod
    def GetSubfinder():
        return GlobalEnv.__SubFinder

    @staticmethod
    def SetSublist3r(rf):
        from general import General

        GlobalEnv.__Sublist3r = General.GetStrippedString(rf)

    @staticmethod
    def GetSublist3r():
        return GlobalEnv.__Sublist3r

    @staticmethod
    def SetChaos(rf):
        from general import General

        GlobalEnv.__Chaos = General.GetStrippedString(rf)

    @staticmethod
    def GetChaos():
        return GlobalEnv.__Chaos

    @staticmethod
    def SetAmass(rf):
        from general import General

        GlobalEnv.__amass = General.GetStrippedString(rf)

    @staticmethod
    def GetAmass():
        return GlobalEnv.__amass

    @staticmethod
    def SettheHarvester(rf):
        from general import General

        GlobalEnv.__theHarvester = General.GetStrippedString(rf)

    @staticmethod
    def GettheHarvester():
        return GlobalEnv.__theHarvester

    @staticmethod
    def SetHttpx(rf):
        from general import General

        GlobalEnv.__Httpx = General.GetStrippedString(rf)

    @staticmethod
    def GetHttpx():
        return GlobalEnv.__Httpx

    # crawling tools
    @staticmethod
    def SetWaybackurls(rf):
        from general import General

        GlobalEnv.__Waybackurls = General.GetStrippedString(rf)

    @staticmethod
    def SetWaymore(lf):
        from general import General

        GlobalEnv.__waymore = General.GetStrippedString(lf)

    @staticmethod
    def GetWaymore():
        return GlobalEnv.__waymore

    @staticmethod
    def GetWaybackurls():
        return GlobalEnv.__Waybackurls

    @staticmethod
    def SetKatana(rf):
        from general import General

        GlobalEnv.__Katana = General.GetStrippedString(rf)

    @staticmethod
    def GetKatana():
        return GlobalEnv.__Katana

    @staticmethod
    def SetGau(rf):
        from general import General

        GlobalEnv.__Gau = General.GetStrippedString(rf)

    @staticmethod
    def GetGau():
        return GlobalEnv.__Gau

    @staticmethod
    def SetGoSpider(rf):
        from general import General

        GlobalEnv.__GoSpider = General.GetStrippedString(rf)

    @staticmethod
    def GetGoSpider():
        return GlobalEnv.__GoSpider

    # fuzzing tools
    @staticmethod
    def SetFFUF(rf):
        from general import General

        GlobalEnv.__ffuf = General.GetStrippedString(rf)

    @staticmethod
    def GetFFUF():
        return GlobalEnv.__ffuf

    # log file
    @staticmethod
    def SetLogFile(lf):
        from general import General

        GlobalEnv.__LogFile = General.GetStrippedString(lf)

    @staticmethod
    def GetLogFile():
        return GlobalEnv.__LogFile

    # temp files
    @staticmethod
    def SetTempFile(d: str):
        from general import General

        GlobalEnv.__tempFile = General.GetStrippedString(d)

    @staticmethod
    def GetTempFile():
        return GlobalEnv.__tempFile

    @staticmethod
    def SetTempJson(d: str):
        from general import General

        GlobalEnv.__tempJson = General.GetStrippedString(d)

    @staticmethod
    def GetTempJson():
        return GlobalEnv.__tempJson

    # config
    @staticmethod
    def SetResultFolder(rf):
        if not rf.endswith("/"):
            rf += "/"
        from general import General

        GlobalEnv.__ResultFolder = General.GetStrippedString(rf)

    @staticmethod
    def GetResultFolder():
        return GlobalEnv.__ResultFolder

    @staticmethod
    def SetDomain(d: str):
        from general import General

        GlobalEnv.__Domain = General.GetStrippedString(d)

    @staticmethod
    def GetDomain():
        return GlobalEnv.__Domain

    @staticmethod
    def SetPortScanningTargetDomains(d: str):
        from general import General

        GlobalEnv.__portScanningTargetDomains = General.GetStrippedString(d)

    @staticmethod
    def GetPortScanningTargetDomains():
        return GlobalEnv.__portScanningTargetDomains

    @staticmethod
    def SetPortScanningTarget(lf):
        from general import General

        GlobalEnv.__portScanningTarget = General.GetStrippedString(lf)

    @staticmethod
    def GetPortScanningTarget():
        return GlobalEnv.__portScanningTarget

    @staticmethod
    def SetPorts(lf):
        from general import General

        GlobalEnv.__ports = General.GetStrippedString(lf)

    @staticmethod
    def GetPorts():
        return GlobalEnv.__ports

    @staticmethod
    def SetDoSubdomainEnumeration(lf):
        from general import General

        if General.GetStrippedString(lf) == "1":
            GlobalEnv.__DoSubdomainEnumeration = True
        else:
            GlobalEnv.__DoSubdomainEnumeration = False

    @staticmethod
    def GetDoSubdomainEnumeration():
        return GlobalEnv.__DoSubdomainEnumeration

    @staticmethod
    def SetDoPortScanning(rf):
        from general import General

        if General.GetStrippedString(rf) == "0":
            GlobalEnv.__doPortScanning = False
        else:
            GlobalEnv.__doPortScanning = True

    @staticmethod
    def GetDoPortScanning():
        return GlobalEnv.__doPortScanning

    @staticmethod
    def SetDoCrawling(rf):
        from general import General

        if General.GetStrippedString(rf) == "0":
            GlobalEnv.__doCrawling = False
        else:
            GlobalEnv.__doCrawling = True

    @staticmethod
    def GetDoCrawling():
        return GlobalEnv.__doCrawling

    @staticmethod
    def SetDoFuzzing(rf):
        from general import General

        if General.GetStrippedString(rf) == "0":
            GlobalEnv.__doFuzzing = False
        else:
            GlobalEnv.__doFuzzing = True

    @staticmethod
    def GetDoFuzzing():
        return GlobalEnv.__doFuzzing

    @staticmethod
    def SetSubDomainsPath(rf):
        from general import General

        GlobalEnv.__SubDomainsFile = General.GetStrippedString(rf)

    @staticmethod
    def GetSubDomainsPath():
        return GlobalEnv.__SubDomainsFile

    @staticmethod
    def SetCrawlingPath(rf):
        from general import General

        GlobalEnv.__crawlingPath = General.GetStrippedString(rf)

    @staticmethod
    def GetCrawlingPath():
        return GlobalEnv.__crawlingPath

    @staticmethod
    def SetFuzzingPath(rf):
        from general import General

        GlobalEnv.__fuzzingPath = General.GetStrippedString(rf)

    @staticmethod
    def GetFuzzingPath():
        return GlobalEnv.__fuzzingPath

    @staticmethod
    def SetFuffWordlist(rf):
        from general import General

        GlobalEnv.__ffufWordlist = General.GetStrippedString(rf)

    @staticmethod
    def GetFuffWordlist():
        return GlobalEnv.__ffufWordlist

    @staticmethod
    def SetPortScanningPath(rf):
        from general import General

        GlobalEnv.__portScanningPath = General.GetStrippedString(rf)

    @staticmethod
    def GetPortScanningPath():
        return GlobalEnv.__portScanningPath
