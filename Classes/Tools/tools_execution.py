
import json
import os
import dns.resolver
from Classes.commands import Commands
from Classes.files import Files
from Classes.request import Requests
from Classes.general import General
from Classes.globalEnv import GlobalEnv
from concurrent.futures import ThreadPoolExecutor


###################### SUBDOMAIN ENUMERATION ######################
class SubdomainEnumeration:
    def __init__(self):
        self.__crtSHsiteUrl = f'https://crt.sh/json?q='
        self.__f = os.path.abspath(f"{GlobalEnv.GetHttpxPath()}/httpx.json")
        self.__httpx_path = f'{GlobalEnv.GetHttpxPath()}'
        self.__httpx_filters = [
            f'jq "[.[] | select(.status_code >= 200 and .status_code < 300)]" "{self.__f}" > {self.__httpx_path}/2xx_responses.json',
            f'jq "[.[] | select(.status_code >= 300 and .status_code < 400)]" "{self.__f}" > {self.__httpx_path}/3xx_responses.json',
            f'jq "[.[] | select(.status_code >= 400 and .status_code < 500)]" "{self.__f}" > {self.__httpx_path}/4xx_responses.json',
            f'jq "[.[] | select(.status_code >= 500 and .status_code < 600)]" "{self.__f}" > {self.__httpx_path}/5xx_responses.json',
            f'jq "[.[] | select(.cdn_name == \\"cloudflare\\")]" "{self.__f}" > {self.__httpx_path}/cloudflare_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"algolia\\"))]" "{self.__f}" > {self.__httpx_path}/algolia_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"hsts\\"))]" "{self.__f}" > {self.__httpx_path}/hsts_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"jsdelivr\\"))]" "{self.__f}" > {self.__httpx_path}/jsdelivr_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"drupal\\"))]" "{self.__f}" > {self.__httpx_path}/drupal_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"fastly\\"))]" "{self.__f}" > {self.__httpx_path}/fastly_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"Google Tag Manager\\"))]" "{self.__f}" > {self.__httpx_path}/GoogleTagManager_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"mariadb\\"))]" "{self.__f}" > {self.__httpx_path}/MariaDB_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"PHP\\"))]" "{self.__f}" > {self.__httpx_path}/php_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"Pantheon\\"))]" "{self.__f}" > {self.__httpx_path}/pantheon_tech.json',
            f'jq "[.[] | select(.tech[] | contains(\\"Varnish\\"))]" "{self.__f}" > {self.__httpx_path}/varnish_tech.json',
            f'jq "[.[] | select(.webserver == \\"cloudflare\\")]" "{self.__f}" > {self.__httpx_path}/cloudflare_webserver.json',
            f'jq "[.[] | select(.webserver == \\"nginx\\")]" "{self.__f}" > {self.__httpx_path}/nginx_webserver.json',
            f'jq "[.[] | select(.webserver == \\"iis\\")]" "{self.__f}" > {self.__httpx_path}/iis_webserver.json',
            f'jq "[.[] | select(.webserver == \\"apache\\")]" "{self.__f}" > {self.__httpx_path}/apache_webserver.json',
            f'jq "[.[] | select(.webserver == \\"litespeed\\")]" "{self.__f}" > {self.__httpx_path}/litespeed_webserver.json',
            f'jq "[.[] | select(.webserver == \\"caddy\\")]" "{self.__f}" > {self.__httpx_path}/caddy_webserver.json'
        ]   

    def __commands(self):
        return [
            ('subfinder', f'subfinder -d {GlobalEnv.GetDomain()} -all -o {GlobalEnv.GetSubDomainsFolderPath()}/subfinder.txt'),
            ('sublist3r', f"sublist3r -d {GlobalEnv.GetDomain()} -t 10 -o {GlobalEnv.GetSubDomainsFolderPath()}/sublist3r.txt"),
            ('assetfinder', f'assetfinder {GlobalEnv.GetDomain()} > {GlobalEnv.GetSubDomainsFolderPath()}/assetfinder.txt')
        ]

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
        path = f"{GlobalEnv.GetHttpxPath()}/httpx.json"
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
        with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executer:
            executer.map(self.__execute_httpx_filter_command, self.__httpx_filters)
    
    def Execute(self):
        
        commands_to_run = [
            cmd for tool, cmd in self.__commands()
            if General.is_tool_installed(tool)
        ]

        with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executer:
            executer.submit(self.__CrtSh)
            executer.map(General.ExecuteCommandNotmp, commands_to_run)

        self.__compine_subdomain_enumeration_result()
        Files.RemoveDuplicateFromFile(GlobalEnv.GetSubDomainsPath())
        General.RemoveOutOfScopeFromSubdomains(GlobalEnv.GetSubDomainsPath())

        if General.is_tool_installed('httpx'):
            outputFile = f"{self.__httpx_path}/httpx.json"
            cmd = f"httpx -l {GlobalEnv.GetSubDomainsPath()} -status-code -fc 404 -title -tech-detect -follow-redirects -json -o {outputFile}"
            General.ExecuteCommandNotmp(cmd)
            General.reformat_json_in_file(outputFile, outputFile)

        self.__extract_urls_from_httpx_result()

        if General.is_tool_installed('jq'):
            self.__filter_httpx_results()
        

###################### CRAWLING ######################
class Crawling:
    def __init__(self):
        pass

    def __commands(self, url):
        return [
            ('katana', f'katana -u {General.GetStrippedString(url)} -d 100 -jc -delay 1 -c 15 -o {GlobalEnv.GetCrawlingFolderPath()}/katana.txt'),
            ('gau', f'gau {url} --subs --threads 15 --providers wayback,otx,commoncrawl --verbose --o {GlobalEnv.GetCrawlingFolderPath()}/gau.txt'),
            ('gospider', f'gospider -s {url} -d 100 -t 15 -c 5 --delay 1 --subs --js --other-source --robots --sitemap --user-agent --include-subs --verbose --output {GlobalEnv.GetCrawlingFolderPath()}/gospider')
        ]

    def __run_tools_for_url(self, url):
        try:
            commands_to_run = [
                cmd for tool, cmd in self.__commands(url)
                if General.is_tool_installed(tool)
            ]
            with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executor:
                futures = [executor.submit(General.ExecuteCommandNotmp, cmd) for cmd in commands_to_run]
                for future in futures:
                    future.result()

        except Exception as e:
            print(f"Error processing {url}: {e}")
    
    def Execute(self):
        try:
            with open(GlobalEnv.GetSubDomainsPath(), "r", encoding="utf-8", errors="ignore") as f:
                urls = [(((str(line)).split(" ["))[0]).strip() for line in f]
            
            tasks = [(self.__run_tools_for_url, url) for url in urls]
            if General.is_tool_installed('waybackurls'):
                cmd = f'waybackurls {GlobalEnv.GetDomain()} > {GlobalEnv.GetCrawlingFolderPath()}/waybackurls.txt'
                tasks.append((General.ExecuteCommandNotmp, cmd))

            with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executor:
                futures = [executor.submit(func, arg) for func, arg in tasks]
                for future in futures:
                    try:
                        future.result() 
                    except Exception as e:
                        print(f"Error in task: {e}")

        except Exception as e:
            print(f"Error in Execute: {e}")

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

    def __NmapCommand(self):    
        ports = GlobalEnv.GetPorts()
        output_file = f"{GlobalEnv.GetPortScanningFolderPath()}/nmap.txt" 
        if len(ports) > 0:
            command = f'nmap -sA -sU -p {ports} -A -iL {GlobalEnv.GetPortScanningTarget()} -oN {output_file}'
        else:    
            command = f'nmap -sA -sU --top-ports 100 -A -iL {GlobalEnv.GetPortScanningTarget()} -oN {output_file}'

        return command

    def __MasscanCommand(self):  
        ports = GlobalEnv.GetPorts()
        output_file = f"{GlobalEnv.GetPortScanningFolderPath()}/masscan.txt" 
        if len(ports) > 0:
            command = f'masscan -iL {GlobalEnv.GetPortScanningTarget()} -p {ports} > {output_file}'
        else:    
            command = f'masscan -p1-65535 -iL {GlobalEnv.GetPortScanningTarget()} > {output_file}'  

        return command

    def __NaabuCommand(self):  
        ports = GlobalEnv.GetPorts()
        output_file = f"{GlobalEnv.GetPortScanningFolderPath()}/naabu.txt" 
        if len(ports)>0:
            command = f'naabu -l {GlobalEnv.GetPortScanningTarget()} -p {ports} -o {output_file}'
        else:
            command = f'naabu -l {GlobalEnv.GetPortScanningTarget()} -top-ports 1000 -o {output_file}'
        return command

    def __commands(self):
        return [
            ('masscan', self.__MasscanCommand()),
            ('nmap', self.__NmapCommand()),
            ('naabu', self.__NaabuCommand())
        ]

    def __extractARecords(self):
        a_records = []

        with open(GlobalEnv.GetSubDomainsPath()) as f:
            for d in f:
                domain = d.strip()

                try:
                    answers = dns.resolver.resolve(domain, "A")
                    for rdata in answers:
                        a_records.append(rdata.to_text())
                except Exception:
                    continue  

        for ip in a_records:
            Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'a', ip)

        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTarget())

    def __dnsRecords(self):
        results = [] 

        with open(GlobalEnv.GetSubDomainsPath()) as f:
            for d in f:
                domain = d.strip()
                domain_result = {"domain": domain, "records": {}}  # dict للـ domain

                for record_type in self.__record_types:
                    try:
                        answers = dns.resolver.resolve(domain, record_type)
                        domain_result["records"][record_type] = []

                        for rdata in answers:
                            record_value = rdata.to_text()
                            domain_result["records"][record_type].append(record_value)

                    except Exception as e:
                        domain_result["records"][record_type] = f"Error: {str(e)}"

                results.append(domain_result)

        # save json to file
        with open(GlobalEnv.GetDNSPath(), "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTarget())

    def Execute(self):
        self.__extractARecords()

        commands_to_run = [
            cmd for tool, cmd in self.__commands()
            if General.is_tool_installed(tool)
        ]

        with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executer:
            for cmd in commands_to_run:
                executer.submit(General.ExecuteCommandNotmp, cmd)
            executer.submit(self.__dnsRecords)

###################### SCREENSHOT ######################
class ScreenShot:
    def __init__(self):
        pass
    
    def __commands(self):
        return [
            ('gowitness' , f'gowitness scan file --file "{GlobalEnv.GetSubDomainsPath()}" --write-none --screenshot-path "{GlobalEnv.GetGowitness()}"')
        ]

    def __TakeSubdomainsScreenshot(self):
        commands_to_run = [
            cmd for tool, cmd in self.__commands()
            if General.is_tool_installed(tool)
        ]

        with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executer:
            executer.map(General.ExecuteCommandNotmp, commands_to_run)

    def Execute(self):
        self.__TakeSubdomainsScreenshot()

###################### FUZZING ######################
class Fuzzing:
    def __init__(self):
        pass
    
    def __FFUFCommand(self, url):  
        if url.endswith('/'):
            url += 'FUZZ'
        else:
            url += '/FUZZ'

        return f'ffuf -u {url} -p 2 -r -w {GlobalEnv.GetFuffWordlist()} -rate 20 -recursion -o {GlobalEnv.GetFuzzingFolderPath()}/ffuf.json'
        

    def __commands(self, url):
        return [
            ('ffuf', self.__FFUFCommand(url))
        ]

    def __run_tools_for_url(self, url):
        try:
            commands_to_run = [
                cmd for tool, cmd in self.__commands(url)
                if General.is_tool_installed(tool)
            ]
            with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executor:
                futures = [executor.submit(General.ExecuteCommandNotmp, cmd) for cmd in commands_to_run]
                for future in futures:
                    future.result()

        except Exception as e:
            print(f"Error processing {url}: {e}")

    def Execute(self):
        try:
            with open(GlobalEnv.GetSubDomainsPath(), "r", encoding="utf-8", errors="ignore") as f:
                urls = [(((str(line)).split(' ['))[0]).strip() for line in f]
            
            tasks = [(self.__run_tools_for_url, url) for url in urls]

            with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executor:
                futures = [executor.submit(func, arg) for func, arg in tasks]
                for future in futures:
                    try:
                        future.result() 
                    except Exception as e:
                        print(f"Error in task: {e}")

        except Exception as e:
            print(f"Error in Execute: {e}")
        