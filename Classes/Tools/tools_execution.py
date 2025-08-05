
import os
import dns
from Classes.commands import Commands
from Classes.files import Files
from Classes.request import Requests
from Classes.general import General
from Classes.globalEnv import GlobalEnv

###################### SUBDOMAIN ENUMERATION ######################
class SubdomainEnumeration:
    def __init__(self):
        self.__crtSHsiteUrl = f'https://crt.sh/json?q='

    def __CrtSh(self):
        response = Requests.Get(url=f"{self.__crtSHsiteUrl}{GlobalEnv.GetDomain()}")
        Files.SaveTextToFile(response.text, f"{GlobalEnv.GetCrtSH()}", 'w')
        Files.SaveTextToFile(response.text, f"{GlobalEnv.GetLogFile()}")
        if response.status_code == 200:
            domains = General.ExtractDomainsFromJsonFile(GlobalEnv.GetCrtSH())
            Files.WriteListToFile(GlobalEnv.GetSubDomainsPath(), 'a', domains)
            Files.WriteListToFile(GlobalEnv.GetCrtShText(), 'w', domains)
            General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetCrtShText())

    def __Httpx(self):
        General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetSubDomainsPath())
        Files.RemoveDuplicateFromFile(GlobalEnv.GetSubDomainsPath())
        commands = Commands.HttpxCommands()
        i = 1
        for c in commands:
            if i == 1:
                General.ExecuteCommand(c, GlobalEnv.GetHttpx())
                Files.CopyFromTo(GlobalEnv.GetTempFile(), GlobalEnv.GetHttpx())
            elif i == 2:
                General.ExecuteCommand(c, GlobalEnv.GetHttpx2xx())
                Files.CopyFromTo(GlobalEnv.GetTempFile(), GlobalEnv.GetHttpx2xx())
                Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx2xx())
            elif i == 3:
                General.ExecuteCommand(c, GlobalEnv.GetHttpx3xx())
                Files.CopyFromTo(GlobalEnv.GetTempFile(), GlobalEnv.GetHttpx3xx())
                Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx3xx())
            elif i == 4:
                General.ExecuteCommand(c, GlobalEnv.GetHttpx4xx())
                Files.CopyFromTo(GlobalEnv.GetTempFile(), GlobalEnv.GetHttpx4xx())
                Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx4xx())
            elif i == 5:
                General.ExecuteCommand(c, GlobalEnv.GetHttpx5xx())
                Files.CopyFromTo(GlobalEnv.GetTempFile(), GlobalEnv.GetHttpx5xx())
                Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx5xx())
            i += 1
        urls = Files.ExtractUrlsFromFile(GlobalEnv.GetHttpx())
        Files.WriteListToFile(GlobalEnv.GetEnhancedHttpx(), 'a', urls)
        Files.RemoveDuplicateFromFile(GlobalEnv.GetEnhancedHttpx())
    
    def __compine_subdomain_enumeration_result(self):
        for filename in os.listdir(GlobalEnv.GetSubDomainsFolderPath()):
            file_path = os.path.join(GlobalEnv.GetSubDomainsFolderPath(), filename)

            if os.path.isfile(file_path) and "httpx" not in file_path and "json" not in file_path:
                Files.CopyFromTo(file_path, GlobalEnv.GetSubDomainsPath())

    def Execute(self):
        if GlobalEnv.GetDoSubdomainEnumeration():
            Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), 'a', GlobalEnv.GetDomain())
            # self.__CrtSh()
            # General.commandsExecuter(Commands.SubfinderCommands(), GlobalEnv.GetSubDomainsFolderPath(), "subfinder")
            # General.commandsExecuter(Commands.Sublist3rCommands(), GlobalEnv.GetSubDomainsFolderPath(), "sublist3r")
            # General.commandsExecuter(Commands.AssetFinderCommands(), GlobalEnv.GetSubDomainsFolderPath(), "assetfinder")
            # General.commandsExecuter(Commands.ChaosCommands(), GlobalEnv.GetSubDomainsFolderPath(), "chaos")
            self.__compine_subdomain_enumeration_result()
            Files.RemoveDuplicateFromFile(GlobalEnv.GetSubDomainsPath())
            General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetSubDomainsPath())
            # self.__Httpx()

###################### CRAWLING ######################
class Crawling:
    def __init__(self):
        pass

    def __prepare(self):
        Files.RemoveDuplicateFromFile(GlobalEnv.GetSubDomainsPath())

    def Execute(self):
        if GlobalEnv.GetDoCrawling():
            self.__prepare()
            try:
                with open(
                    f"{GlobalEnv.GetHttpx()}", "r", encoding="utf-8", errors="ignore"
                ) as f:
                    for line in f:
                        url = (((str(line)).split(" ["))[0]).strip()
                        General.commandsExecuter(Commands.KatanaCommands(url), GlobalEnv.GetCrawlingFolderPath(), "katana")
                        General.commandsExecuter(Commands.GauCommands(url), GlobalEnv.GetCrawlingFolderPath(), "gau")
                        General.commandsExecuter(Commands.GoSpiderCommands(url), GlobalEnv.GetCrawlingFolderPath(), "gospider", "json")
                General.commandsExecuter(Commands.WaybackurlsCommands(url), GlobalEnv.GetCrawlingFolderPath(), "waybackurls")
                General.FilterResultFile(GlobalEnv.GetWaybackurls())
            except Exception as e:
                print(f"Error running: {str(e)}")

###################### PORT SCANNING ######################
class PortScanning:
    def __init__(self):
        pass

    __record_types = [
        "A",
        "AAAA",
        "CNAME",
        "MX",
        "NS",
        "TXT",
        "SOA",
        "PTR",
        "SRV",
        "CAA",
        "NAPTR",
        "DNSKEY",
        "RRSIG",
        "DS",
        "HINFO",
        "SPF",
        "TLSA",
    ]

    def __prepare(self):
        Files.WriteToFile(GlobalEnv.GetPortScanningTargetDomains(), "a", GlobalEnv.GetDomain())
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTargetDomains())

    def __dnsRecords(self):
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTargetDomains())
        with open(GlobalEnv.GetPortScanningTargetDomains())as f:
            for d in f:
                domain = d.strip()
                flagForArecord = True
                for record_type in self.__record_types:
                    try:
                        answers = dns.resolver.resolve(domain, record_type)
                        line = f"\n{record_type} Records for {domain}"
                        print(line)
                        Files.WriteToFile(GlobalEnv.GetDnsRecords(), 'a', line)
                        Files.WriteToFile(GlobalEnv.GetLogFile(), 'a', line)
                        for rdata in answers:
                            line = rdata.to_text()
                            print(line)
                            Files.WriteToFile(GlobalEnv.GetDnsRecords(), "a", line)
                            Files.WriteToFile(GlobalEnv.GetLogFile(), "a", line)
                            if flagForArecord:
                                Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'a', line)
                        flagForArecord = False
                    except Exception as e:
                        line = f"Error fetching {record_type} records: {e}"
                        print(line)
                        Files.WriteToFile(GlobalEnv.GetLogFile(), "a", line)
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTarget())

    def Execute(self):
        if GlobalEnv.GetDoPortScanning():
            self.__prepare()
            self.__dnsRecords()
            General.commandsExecuter(Commands.MasscanCommands(), GlobalEnv.GetPortScanningFolderPath(), "masscan")
            General.commandsExecuter(Commands.NmapCommands(), GlobalEnv.GetPortScanningFolderPath(), "nmap")
            General.commandsExecuter(Commands.NaabuCommands(), GlobalEnv.GetPortScanningFolderPath(), "naabu")

###################### SCREENSHOT ######################
class ScreenShot:
    def __init__(self):
        pass

    def __prepareOperation(self):
        Files.WriteToFile(GlobalEnv.GetTempFile(), "w", "")
        if GlobalEnv.GetDoSubdomainEnumeration() or Files.IsFileExists(GlobalEnv.GetEnhancedHttpx()):
            Files.CopyFromTo(GlobalEnv.GetEnhancedHttpx(), GlobalEnv.GetTempFile())
        else:
            Files.WriteToFile(GlobalEnv.GetTempFile(), 'a', GlobalEnv.GetDomain())
        
        Files.RemoveDuplicateFromFile(GlobalEnv.GetTempFile())

    def __TakeSubdomainsScreenshot(self):
        commands = Commands.GowitnessCommands()
        for c in commands:
            General.ExecuteCommand(c)

    def Execute(self):
        if GlobalEnv.GetTakeScreenShots():
            self.__prepareOperation()
            self.__TakeSubdomainsScreenshot()

###################### FUZZING ######################
class Fuzzing:
    def __init__(self):
        pass
    
    def Execute(self):
        if GlobalEnv.GetDoFuzzing():
            try:
                with open(f'{GlobalEnv.GetHttpx()}', 'r', encoding="utf-8", errors='ignore') as f:
                    for line in f:
                        url = (((str(line)).split(' ['))[0]).strip()
                        General.commandsExecuter(Commands.FFUFCommands(url), GlobalEnv.GetFuzzingFolderPath(), "ffuf", "json")
            except Exception as e:
                print(f"Error running: {str(e)}")
        