
import json
import os
import dns.resolver
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
        response = Requests.send("GET", url=f"{self.__crtSHsiteUrl}{GlobalEnv.GetDomain()}")
        Files.SaveTextToFile(response.text, f"{GlobalEnv.GetCrtSH()}", 'w')
        General.reformat_json_in_file(GlobalEnv.GetCrtSH(), GlobalEnv.GetCrtSH())
        Files.SaveTextToFile(response.text, f"{GlobalEnv.GetLogFile()}")
        if response.status_code == 200:
            domains = General.ExtractDomainsFromJsonFile(GlobalEnv.GetCrtSH())
            Files.WriteListToFile(GlobalEnv.GetSubDomainsPath(), 'a', domains)
            Files.WriteListToFile(GlobalEnv.GetCrtShText(), 'w', domains)
            General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetCrtShText())
        else:
            self.__CrtSh()

    def __compine_subdomain_enumeration_result(self):
        for filename in os.listdir(GlobalEnv.GetSubDomainsFolderPath()):
            file_path = os.path.join(GlobalEnv.GetSubDomainsFolderPath(), filename)

            if os.path.isfile(file_path) and "httpx" not in file_path and "json" not in file_path:
                Files.CopyFromTo(file_path, GlobalEnv.GetSubDomainsPath())

    # get valid urls from httpx result
    def __extract_urls_from_httpx_result(self):
        path = f"{GlobalEnv.GetHttpxPath()}/httpx1.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), 'w', '')
        for item in data:
            if 'www' in item['input']:
                continue
            if "input" in item:
                Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), 'a', item['input'])
    
    def __execute_httpx_filter_command(self, c:str):
        f = (c.split('>')[-1]).strip()
        Files.CreateFile(f)
        f = os.path.abspath(f)
        c = '>'.join(c.split('>')[:-1])
        c = c.strip()
        c = f'{c} > "{f}"' 
        General.ExecuteCommandNotmp(c, f)

    def __filter_httpx_results(self):
        f = os.path.abspath(f"{GlobalEnv.GetHttpxPath()}/httpx1.json")
        httpx_path = f'{GlobalEnv.GetHttpxPath()}'
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.status_code >= 200 and .status_code < 300)]" "{f}" > {httpx_path}/2xx_responses.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.status_code >= 300 and .status_code < 400)]" "{f}" > {httpx_path}/3xx_responses.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.status_code >= 400 and .status_code < 500)]" "{f}" > {httpx_path}/4xx_responses.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.status_code >= 500 and .status_code < 600)]" "{f}" > {httpx_path}/5xx_responses.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.cdn_name == \\"cloudflare\\")]" "{f}" > {httpx_path}/cloudflare_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"algolia\\"))]" "{f}" > {httpx_path}/algolia_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"hsts\\"))]" "{f}" > {httpx_path}/hsts_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"jsdelivr\\"))]" "{f}" > {httpx_path}/jsdelivr_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"drupal\\"))]" "{f}" > {httpx_path}/drupal_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"fastly\\"))]" "{f}" > {httpx_path}/fastly_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"Google Tag Manager\\"))]" "{f}" > {httpx_path}/GoogleTagManager_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"mariadb\\"))]" "{f}" > {httpx_path}/MariaDB_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"PHP\\"))]" "{f}" > {httpx_path}/php_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"Pantheon\\"))]" "{f}" > {httpx_path}/pantheon_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.tech[] | contains(\\"Varnish\\"))]" "{f}" > {httpx_path}/varnish_tech.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.webserver == \\"cloudflare\\")]" "{f}" > {httpx_path}/cloudflare_webserver.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.webserver == \\"nginx\\")]" "{f}" > {httpx_path}/nginx_webserver.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.webserver == \\"iis\\")]" "{f}" > {httpx_path}/iis_webserver.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.webserver == \\"apache\\")]" "{f}" > {httpx_path}/apache_webserver.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.webserver == \\"litespeed\\")]" "{f}" > {httpx_path}/litespeed_webserver.json')
        self.__execute_httpx_filter_command(f'jq "[.[] | select(.webserver == \\"caddy\\")]" "{f}" > {httpx_path}/caddy_webserver.json')
    
    def Execute(self):
        Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), 'a', GlobalEnv.GetDomain())
        self.__CrtSh()
        if General.is_tool_installed('subfinder'):
            General.commandsExecuter(Commands.SubfinderCommands(), GlobalEnv.GetSubDomainsFolderPath(), "subfinder")
        if General.is_tool_installed('sublist3r'):
            General.commandsExecuter(Commands.Sublist3rCommands(), GlobalEnv.GetSubDomainsFolderPath(), "sublist3r")
        if General.is_tool_installed('assetfinder'):
            General.commandsExecuter(Commands.AssetFinderCommands(), GlobalEnv.GetSubDomainsFolderPath(), "assetfinder")
        # General.commandsExecuter(Commands.ChaosCommands(), GlobalEnv.GetSubDomainsFolderPath(), "chaos")
        self.__compine_subdomain_enumeration_result()
        Files.RemoveDuplicateFromFile(GlobalEnv.GetSubDomainsPath())
        General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetSubDomainsPath())
        if General.is_tool_installed('httpx'):
            General.commandsExecuter(Commands.HttpxCommands(), GlobalEnv.GetHttpxPath(), "httpx", 'json', GlobalEnv.GetTempJson())
        self.__extract_urls_from_httpx_result()
        if General.is_tool_installed('jq'):
            self.__filter_httpx_results()
        

###################### CRAWLING ######################
class Crawling:
    def __init__(self):
        pass

    def __prepare(self):
        Files.RemoveDuplicateFromFile(GlobalEnv.GetSubDomainsPath())

    def Execute(self):
        self.__prepare()
        try:
            with open(
                f"{GlobalEnv.GetHttpx()}", "r", encoding="utf-8", errors="ignore"
            ) as f:
                for line in f:
                    url = (((str(line)).split(" ["))[0]).strip()
                    if General.is_tool_installed('katana'):
                        General.commandsExecuter(Commands.KatanaCommands(url), GlobalEnv.GetCrawlingFolderPath(), "katana")
                    if General.is_tool_installed('gau'):
                        General.commandsExecuter(Commands.GauCommands(url), GlobalEnv.GetCrawlingFolderPath(), "gau")
                    if General.is_tool_installed('gospider'):
                        General.commandsExecuter(Commands.GoSpiderCommands(url), GlobalEnv.GetCrawlingFolderPath(), "gospider", "json")
            if General.is_tool_installed('waybackurls'):
                General.commandsExecuter(Commands.WaybackurlsCommands(url), GlobalEnv.GetCrawlingFolderPath(), "waybackurls")
            # General.FilterResultFile(GlobalEnv.GetWaybackurls())
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

    def __dnsRecords(self):
        results = [] 

        with open(GlobalEnv.GetPortScanningTargetDomains()) as f:
            for d in f:
                domain = d.strip()
                flagForArecord = True
                domain_result = {"domain": domain, "records": {}}  # dict للـ domain

                for record_type in self.__record_types:
                    try:
                        answers = dns.resolver.resolve(domain, record_type)
                        domain_result["records"][record_type] = []

                        for rdata in answers:
                            record_value = rdata.to_text()
                            domain_result["records"][record_type].append(record_value)

                            if flagForArecord:
                                Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'a', record_value)

                        flagForArecord = False

                    except Exception as e:
                        domain_result["records"][record_type] = f"Error: {str(e)}"

                results.append(domain_result)
        # save json to file
        with open(GlobalEnv.GetDNSPath(), "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTarget())

    def Execute(self):
        self.__prepare()
        self.__dnsRecords()
        if General.is_tool_installed('masscan'):
            General.commandsExecuter(Commands.MasscanCommands(), GlobalEnv.GetPortScanningFolderPath(), "masscan")
        if General.is_tool_installed('nmap'):
            General.commandsExecuter(Commands.NmapCommands(), GlobalEnv.GetPortScanningFolderPath(), "nmap")
        if General.is_tool_installed('naabu'):
            General.commandsExecuter(Commands.NaabuCommands(), GlobalEnv.GetPortScanningFolderPath(), "naabu")

###################### SCREENSHOT ######################
class ScreenShot:
    def __init__(self):
        pass

    def __prepare(self):
        Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), "a", GlobalEnv.GetDomain())

    def __TakeSubdomainsScreenshot(self):
        commands = Commands.GowitnessCommands()
        for c in commands:
            General.ExecuteCommand(c)

    def Execute(self):
        self.__prepare()
        self.__TakeSubdomainsScreenshot()

###################### FUZZING ######################
class Fuzzing:
    def __init__(self):
        pass

    def __prepare(self):
        Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), "a", GlobalEnv.GetDomain())
    
    def Execute(self):
        self.__prepare()
        try:
            with open(f'{GlobalEnv.GetSubDomainsPath()}', 'r', encoding="utf-8", errors='ignore') as f:
                for line in f:
                    url = (((str(line)).split(' ['))[0]).strip()
                    if General.is_tool_installed('ffuf'):
                        General.commandsExecuter(Commands.FFUFCommands(url), GlobalEnv.GetFuzzingFolderPath(), "ffuf", "json")
        except Exception as e:
            print(f"Error running: {str(e)}")
        