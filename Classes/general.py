import io
import json
import os
from pathlib import Path
import platform
import re
import shutil
import socket
import subprocess
import sys
from threading import Lock
from urllib.parse import urlparse
import concurrent.futures
from Classes.files import Files
from Classes.globalEnv import GlobalEnv
from Classes.request import Requests


class General:
    def __init__(self):
        pass

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    __domainPattern = r"\b(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b"
    __urlPattern = r'https?://[^\s"\'<>]+'
    __statusPattern = re.compile(r"\b([23]\d{2}|401|403)\b")
    __write_lock = Lock()

    @staticmethod
    def getIPfromDomain(domain):
        try:
            ip = socket.gethostbyname(domain.strip())
            return ip
        except socket.gaierror as e:
            print(f"Error resolving {domain}: {e}")
            return None

    @staticmethod
    def IsDomainValid(domain):
        return bool(re.fullmatch(General.__domainPattern, domain))

    @staticmethod
    def GetUniqueURLs(urls):
        return list(set(urls))

    @staticmethod
    def ReadResultDirectory():
        while True:
            fpath = input('Enter valid directory to save result: ')
            if Files.ValidateDirectoryPath(fpath):
                GlobalEnv.SetResultFolder(General.GetStrippedString(fpath))
                return True

            if General.GetOStype() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')

            print('invalid path!')

    @staticmethod
    def ReadDomain():
        while True:
            domain = input('Enter valid domain: ')
            if General.IsDomainValid(General.GetStrippedString(domain)):
                GlobalEnv.SetDomain(domain)
                return True

            if General.GetOStype() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')

            print('invalid domain!')

    @staticmethod
    def ReadFFUFwordlist():
        ffufWordlist = input('Enter ffuf wordlist: ')
        GlobalEnv.SetFuffWordlist(str(ffufWordlist))
        return True

    @staticmethod
    def GetOStype():
        return platform.system()

    @staticmethod
    def GetStrippedString(s:str):
        return s.strip()

    @staticmethod
    def ExecuteCommand(cmd:str, outputFile:str='', tmpfile:str=''):
        if outputFile == '':
            return
        subprocess.run(cmd, shell=True, check=True)
        if tmpfile == '':
            tmpfile = GlobalEnv.GetTempFile()   
        Files.CopyFromTo(tmpfile, outputFile)
        Files.CopyFromTo(outputFile, GlobalEnv.GetLogFile())
        if 'json' in outputFile:
            General.reformat_json_in_file(outputFile, outputFile)

    @staticmethod
    def ExecuteCommandNotmp(cmd:str, outputFile:str=''):
        print(f"[+] Running Command: {cmd}")
        os.system(cmd)
        if outputFile != '':
            Files.CopyFromTo(outputFile, GlobalEnv.GetLogFile())

    @staticmethod
    def GetUrlFromDomain(url):
        # Add 'https://' if missing to ensure urlparse works correctly
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Remove 'www.' if present
        if domain.startswith('www.'):
            domain = domain[4:]

        return domain

    @staticmethod
    def ExtractDomainsFromJsonFile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        try:
            data = json.loads(content)
            content = json.dumps(data)
        except Exception as e:
            print(f"[!] Warning: JSON parse failed, treating as plain text: {e}")

        urls = re.findall(General.__urlPattern, content)
        domains = re.findall(General.__domainPattern, content, re.IGNORECASE)

        # Remove domains that already appear as part of a URL
        clean_domains = [d for d in domains if all(d not in u for u in urls)]

        # Combine both
        results = urls + clean_domains
        results = sorted(set(results))
        return results

    @staticmethod
    def ExtractDomainsFromTextFile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        urls = re.findall(General.__urlPattern, content)
        domains = re.findall(General.__domainPattern, content, re.IGNORECASE)

        # Remove domains that already appear as part of a URL
        clean_domains = [d for d in domains if all(d not in u for u in urls)]

        # Combine both
        results = urls + clean_domains
        results = sorted(set(results))
        return results

    @staticmethod
    def RemoveOutOfScopeFromSubdomains(path):
        seen = set()
        unique_lines = []

        with open(path, 'r') as infile:
            for line in infile:
                if line not in seen and GlobalEnv.GetDomain() in line:
                    seen.add(line)
                    unique_lines.append(line)

        with open(path, 'w') as outfile:
            outfile.writelines(unique_lines)

    @staticmethod
    def RemoveOutOfScopeFromListOfSubdomains(urls:list):
        inscopeurls = []
        for url in urls:
            s = (((str(url)).strip()).split('.com'))[0]
            if GlobalEnv.GetDomain() in s:
                inscopeurls.append(s)
        return inscopeurls
        

    ### filter result files like subdomains file and waybackurls file from dublicate and bad urls

    @staticmethod
    def __process_url(url):
        response = Requests.Get(url)
        if General.__statusPattern.search(str(response.status_code)) and (str(url)).startswith('https'):
            with General.__write_lock:
                Files.WriteToFile(GlobalEnv.GetTempFile(), "a", url)

    @staticmethod
    def FilterResultFile(filename:str):

        Files.WriteToFile(GlobalEnv.GetTempFile(), 'w', '')

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            with open(filename, 'r') as f:
                for line in f:
                    url = General.GetUrlFromDomain(line.strip())
                    if url:
                        futures.append(executor.submit(General.__process_url, url))

        concurrent.futures.wait(futures)

        Files.WriteToFile(filename, "w", "")
        Files.CopyFromTo(GlobalEnv.GetTempFile(), filename)
        Files.WriteToFile(GlobalEnv.GetTempFile(), "w", "")
        Files.CopyFromTo(filename, GlobalEnv.GetLogFile())
        Files.RemoveDuplicateFromFile(filename)

    # get httpx domains
    @staticmethod
    def GetDomainsFromHttpxFile():
        from globalEnv import GlobalEnv
        from general import General

        domains = []
        with open(GlobalEnv.GetHttpx(), "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                strippedLine = line.strip()
                if '[' in strippedLine:
                    url = (strippedLine.split('['))[0]
                domain = General.GetUrlFromDomain(url.strip())
                domains.append(domain)
        return sorted(set(domains))

    @staticmethod
    def commandsExecuter(func, path:str, toolname:str, ext:str="txt", tmpfile:str=""):
        i = 1
        commands = func
        for c in commands:
            outFile = f"{path}/{toolname}{i}.{ext}"
            if not Files.IsFileExists(outFile):
                Files.CreateFile(outFile)
            General.ExecuteCommand(c, outFile, tmpfile=tmpfile)
            i = i + 1
    
    @staticmethod
    def is_tool_installed(toolname:str):
        return shutil.which(toolname) is not None
        # if subprocess.run(["which", f"{toolname}"], capture_output=True).returncode == 0:
        #     return True
        # return False
    
    @staticmethod
    def is_tool_in_path(self, path_to_check: str):
        path_dirs = os.environ.get("PATH", "").split(":")
        return path_to_check in path_dirs
    
    @staticmethod
    def reformat_json_in_file(input_file:str, output_file:str):
        General.fix_json_file(input_file, output_file)
        # Load JSON data from file
        with open(input_file, "r") as f:
            data = json.load(f)  # Parse JSON

        # Write reformatted JSON (indented, sorted keys)
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4, sort_keys=True)  # Pretty-print
    
    @staticmethod
    def fix_json_file(input_file:str, output_file:str):
        try:
            content = Path(input_file).read_text(encoding='utf-8').strip()
            
            if content.startswith('[') and content.endswith(']'):
                content = content[1:-1]
            
            objects = []
            buffer = ""
            brace_count = 0
            
            for char in content:
                if char == '{':
                    brace_count += 1
                    buffer += char
                elif char == '}':
                    brace_count -= 1
                    buffer += char
                    if brace_count == 0:
                        objects.append(buffer)
                        buffer = ""
                elif brace_count > 0:
                    buffer += char
            
            valid_objects = []
            for obj in objects:
                try:
                    valid_objects.append(json.loads(obj))
                except json.JSONDecodeError:
                    continue
            
            Path(output_file).write_text(
                json.dumps(valid_objects, indent=4, ensure_ascii=False),
                encoding='utf-8'
            )
            
            return True
        
        except Exception as e:
            print(f"Error fixing JSON file: {str(e)}")
            return False
    
    @staticmethod
    def GetMaxThreadsNumber():
        try:
            threads = int(GlobalEnv.GetMaxThreads()) 
            if threads > 15:
                return 15
            return threads
        except:
            return 10
    

