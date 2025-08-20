
import json
import os
import threading
import dns.resolver
from Classes.files import Files
from Classes.request import Requests
from Classes.general import General
from Classes.globalEnv import GlobalEnv
from concurrent.futures import ThreadPoolExecutor


###################### SUBDOMAIN ENUMERATION ######################
class SubdomainEnumeration:
    def __init__(self):
        self.__crtSHsiteUrl = f'https://crt.sh/json?q='
        self.__threads = General.get_max_number_of_threads()
        self.__httpx_path = f'{GlobalEnv.httpx_path}'
        self.__f = os.path.abspath(f"{self.__httpx_path}/httpx.json")
        self.__subdomains_file = f'{GlobalEnv.subdomains_folder}'
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
            ('subfinder', f'subfinder -d {GlobalEnv.domain} -all -t {self.__threads} -o {self.__subdomains_file}/subfinder.txt'),
            ('sublist3r', f"sublist3r -d {GlobalEnv.domain} -t {self.__threads} -o {self.__subdomains_file}/sublist3r.txt"),
            ('assetfinder', f'assetfinder {GlobalEnv.domain} > {self.__subdomains_file}/assetfinder.txt')
        ]

    def __CrtSh(self):
        response = Requests.send("GET", url=f"{self.__crtSHsiteUrl}{GlobalEnv.domain}")
        Files.save_txt_to_file(response.text, f"{GlobalEnv.crtsh}", 'w')
        General.reformat_json_in_file(GlobalEnv.crtsh, GlobalEnv.crtsh)
        Files.save_txt_to_file(response.text, f"{GlobalEnv.log_file}")
        if response.status_code == 200:
            domains = General.extract_domains_from_json(GlobalEnv.crtsh)
            Files.write_list_to_file(GlobalEnv.subdomains_file, 'a', domains)
            Files.write_list_to_file(GlobalEnv.crtsh_txt, 'w', domains)
            General.remove_out_of_scope_subdomains(GlobalEnv.crtsh_txt)
        else:
            self.__CrtSh()

    def __compine_subdomain_enumeration_result(self):
        for filename in os.listdir(GlobalEnv.subdomains_folder):
            file_path = os.path.join(GlobalEnv.subdomains_folder, filename)

            if os.path.isfile(file_path) and "httpx" not in file_path and "json" not in file_path:
                Files.copy_from_to(file_path, GlobalEnv.subdomains_file)

    # get valid urls from httpx result
    def __extract_urls_from_httpx_result(self):
        path = f"{self.__httpx_path}/httpx.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        Files.write_to_file(GlobalEnv.subdomains_file, 'w', '')
        for item in data:
            if 'www' in item['input']:
                continue
            if "input" in item:
                Files.write_to_file(GlobalEnv.subdomains_file, 'a', item['input'])
    
    def __execute_httpx_filter_command(self, c:str):
        f = (c.split('>')[-1]).strip()
        Files.create_file(f)
        f = os.path.abspath(f)
        c = '>'.join(c.split('>')[:-1])
        c = c.strip()
        c = f'{c} > "{f}"' 
        General.exexute_command(c, f)

    def __filter_httpx_results(self):
        with ThreadPoolExecutor(max_workers=self.__threads) as executer:
            executer.map(self.__execute_httpx_filter_command, self.__httpx_filters)
    
    def Execute(self):
        
        commands_to_run = [
            cmd for tool, cmd in self.__commands()
            if General.is_tool_installed(tool)
        ]

        with ThreadPoolExecutor(max_workers=self.__threads) as executer:
            executer.submit(self.__CrtSh)
            executer.map(General.exexute_command, commands_to_run)

        self.__compine_subdomain_enumeration_result()
        Files.remove_duplicate_from_file(GlobalEnv.subdomains_file)
        General.remove_out_of_scope_subdomains(GlobalEnv.subdomains_file)

        if General.is_tool_installed('httpx'):
            input_file = f"{self.__httpx_path}/httpx1.json"
            output_file = f"{self.__httpx_path}/httpx.json"
            cmd = f"httpx -l {GlobalEnv.subdomains_file} -status-code -fc 404 -title -tech-detect -follow-redirects -nc -o {input_file} -json"
            General.exexute_command(cmd)
            General.reformat_json_in_file(input_file, output_file)

        self.__extract_urls_from_httpx_result()

        if General.is_tool_installed('jq'):
            self.__filter_httpx_results()
        

###################### CRAWLING ######################
class Crawling:
    def __init__(self):
        self.__lock = threading.Lock()
        self.__threads = General.get_max_number_of_threads()
        self.__crawling_path = GlobalEnv.crawling_folder
        self.__wayback_file = f'{self.__crawling_path}/waybackurls.txt'
        self.__wayback_filter = f'{self.__crawling_path}/filtered_waybackurls.txt'

    def __commands(self, url:str):
        return [
            ('katana', f'katana -u {url.strip()} -d 100 -jc -delay 1 -c {self.__threads} -o {self.__crawling_path}/katana.txt'),
            ('gau', f'gau {url.strip()} --subs --threads {self.__threads} --providers wayback,otx,commoncrawl --verbose --o {self.__crawling_path}/gau.txt'),
            ('gospider', f'gospider -s {url.strip()} -d 100 -t {self.__threads} -c 5 --delay 1 --subs --js --other-source --robots --sitemap --user-agent --include-subs --verbose --output {self.__crawling_path}/gospider')
        ]

    def __run_tools_for_url(self, url):
        try:
            commands_to_run = [
                cmd for tool, cmd in self.__commands(url)
                if General.is_tool_installed(tool)
            ]
            with ThreadPoolExecutor(max_workers=self.__threads) as executor:
                futures = [executor.submit(General.exexute_command, cmd) for cmd in commands_to_run]
                for future in futures:
                    future.result()

        except Exception as e:
            print(f"Error processing {url}: {e}")
    
    def __filter_waybackurls_result(self):
        cmd = f"httpx -l {self.__wayback_file} -status-code -fc 404 -follow-redirects -nc -t {self.__threads} -o {self.__wayback_filter}"
        General.exexute_command(cmd)

    def __run_wayback_and_filter(self, executor:ThreadPoolExecutor):
        if General.is_tool_installed('waybackurls'):
            cmd = f'waybackurls {GlobalEnv.domain} > {self.__wayback_file}'
            wayback_future = executor.submit(General.exexute_command, cmd)
            wayback_future.result()
            return executor.submit(self.__filter_waybackurls_result)
        return None

    def Execute(self):
        try:
            with ThreadPoolExecutor(max_workers=self.__threads) as executor:
                self.__run_wayback_and_filter(executor)

                with open(GlobalEnv.subdomains_file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        url = line.strip()
                        if not url:
                            continue

                        executor.submit(self.__run_tools_for_url, General.get_url_from_domain(url))

        except Exception as e:
            print(f"Error in Execute: {e}")

###################### PORT SCANNING ######################
class PortScanning:
    def __init__(self):
        self.__threads = General.get_max_number_of_threads()

    __record_types = ['A', 'AAAA', 'AFSDB', 'APL', 'CAA', 'CDNSKEY', 'CDS', 'CERT',
            'CNAME', 'CSYNC', 'DHCID', 'DLV', 'DNAME', 'DNSKEY', 'DS', 'EUI48',
            'EUI64', 'HINFO', 'HIP', 'HTTPS', 'IPSECKEY', 'KEY', 'KX', 'LOC',
            'MX', 'NAPTR', 'NS', 'NSEC', 'NSEC3', 'NSEC3PARAM', 'OPENPGPKEY', 'PTR',
            'RP', 'RRSIG', 'SIG', 'SMIMEA', 'SOA', 'SRV', 'SSHFP', 'SVCB',
            'TA', 'TKEY', 'TLSA', 'TSIG', 'TXT', 'URI', 'ZONEMD']

    def __NmapCommand(self):    
        ports = GlobalEnv.ports
        output_file = f"{GlobalEnv.port_scanning_folder}/nmap.txt" 
        if len(ports) > 0:
            command = f'nmap -sA -sU -p {ports} -A -iL {GlobalEnv.port_scanning_a_records} -oN {output_file}'
        else:    
            command = f'nmap -sA -sU --top-ports 100 -A -iL {GlobalEnv.port_scanning_a_records} -oN {output_file}'

        return command

    def __MasscanCommand(self):  
        ports = GlobalEnv.ports
        output_file = f"{GlobalEnv.port_scanning_folder}/masscan.txt" 
        if len(ports) > 0:
            command = f'masscan -iL {GlobalEnv.port_scanning_a_records} -p {ports} > {output_file}'
        else:    
            command = f'masscan -p1-65535 -iL {GlobalEnv.port_scanning_a_records} > {output_file}'  

        return command

    def __NaabuCommand(self):  
        ports = GlobalEnv.ports
        output_file = f"{GlobalEnv.port_scanning_folder}/naabu.txt" 
        if len(ports)>0:
            command = f'naabu -l {GlobalEnv.port_scanning_a_records} -p {ports} -o {output_file}'
        else:
            command = f'naabu -l {GlobalEnv.port_scanning_a_records} -top-ports 1000 -o {output_file}'
        return command

    def __commands(self):
        return [
            ('masscan', self.__MasscanCommand()),
            ('nmap', self.__NmapCommand()),
            ('naabu', self.__NaabuCommand())
        ]

    def __extractARecords(self):
        a_records = []

        with open(GlobalEnv.subdomains_file) as f:
            for d in f:
                domain = d.strip()

                try:
                    answers = dns.resolver.resolve(domain, "A")
                    for rdata in answers:
                        a_records.append(rdata.to_text())
                except Exception:
                    continue  

        for ip in a_records:
            Files.write_to_file(GlobalEnv.port_scanning_a_records, 'a', ip)

        Files.remove_duplicate_from_file(GlobalEnv.port_scanning_a_records)

    def __dnsRecords(self):
        results = [] 

        with open(GlobalEnv.subdomains_file) as f:
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
        with open(GlobalEnv.dns_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        Files.remove_duplicate_from_file(GlobalEnv.port_scanning_a_records)

    def Execute(self):
        self.__extractARecords()

        commands_to_run = [
            cmd for tool, cmd in self.__commands()
            if General.is_tool_installed(tool)
        ]

        with ThreadPoolExecutor(max_workers=self.__threads) as executer:
            for cmd in commands_to_run:
                executer.submit(General.exexute_command, cmd)
            executer.submit(self.__dnsRecords)

###################### SCREENSHOT ######################
class ScreenShot:
    def __init__(self):
        self.__threads = General.get_max_number_of_threads()
    
    def __commands(self):
        return [
            ('gowitness' , f'gowitness scan file --file "{GlobalEnv.subdomains_file}" --write-none --screenshot-path "{GlobalEnv.gowitness}"')
        ]

    def __TakeSubdomainsScreenshot(self):
        commands_to_run = [
            cmd for tool, cmd in self.__commands()
            if General.is_tool_installed(tool)
        ]

        with ThreadPoolExecutor(max_workers=self.__threads) as executer:
            executer.map(General.exexute_command, commands_to_run)

    def Execute(self):
        self.__TakeSubdomainsScreenshot()

###################### FUZZING ######################
class Fuzzing:
    def __init__(self):
        self.__threads = General.get_max_number_of_threads()
    
    def __FFUFCommand(self, url:str):  
        if url.endswith('/'):
            url += 'FUZZ'
        else:
            url += '/FUZZ'
        
        url = url.strip()

        return f'''ffuf -u {url} \
                -w {GlobalEnv.ffuf_wordlist} \
                -p 2 \
                -r \
                -rate 15 \
                -timeout 10 \
                -t 1 \
                -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36" \
                -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
                -H "Accept-Language: en-US,en;q=0.5" \
                -H "Connection: keep-alive" \
                -H "Upgrade-Insecure-Requests: 1" \
                -recursion \
                -recursion-depth 2 \
                -fs 0 \
                -o {GlobalEnv.fuzzing_folder}/ffuf.json \
                -of json'''
        

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
            with ThreadPoolExecutor(max_workers=self.__threads) as executor:
                futures = [executor.submit(General.exexute_command, cmd) for cmd in commands_to_run]
                for future in futures:
                    future.result()

        except Exception as e:
            print(f"Error processing {url}: {e}")

    def Execute(self):
        try:
            with ThreadPoolExecutor(max_workers=self.__threads) as executor:
                with open(GlobalEnv.subdomains_file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        url = line.strip()
                        if not url:
                            continue

                        executor.submit(self.__run_tools_for_url, General.get_url_from_domain(url))

        except Exception as e:
            print(f"Error in Execute: {e}")
        