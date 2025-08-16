import io
import json
import os
import platform
import re
import shutil
import socket
import sys
from urllib.parse import urlparse
from Classes.files import Files
from Classes.globalEnv import GlobalEnv


class General:
    def __init__(self):
        pass

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    __domainPattern = r"\b(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b"
    __urlPattern = r'https?://[^\s"\'<>]+'
    __statusPattern = re.compile(r"\b([23]\d{2}|401|403)\b")

    @staticmethod
    def get_ip_from_domain(domain):
        try:
            ip = socket.gethostbyname(domain.strip())
            return ip
        except socket.gaierror as e:
            print(f"Error resolving {domain}: {e}")
            return None

    @staticmethod
    def is_domain_valid(domain):
        return bool(re.fullmatch(General.__domainPattern, domain))


    @staticmethod
    def get_os_type():
        return platform.system()

    @staticmethod
    def exexute_command(cmd:str, outputFile:str=''):
        print(f"[+] Running Command: {cmd}")
        os.system(cmd)
        if outputFile != '':
            Files.copy_from_to(outputFile, GlobalEnv.log_file)

    @staticmethod
    def get_url_from_domain(domain:str):
        # Add 'https://' if missing to ensure urlparse works correctly
        if not domain.startswith(('http://', 'https://')):
            domain = 'https://' + domain

        parsed_url = urlparse(domain)
        domain = parsed_url.netloc

        # Remove 'www.' if present
        if domain.startswith('www.'):
            domain = domain[4:]

        return domain

    @staticmethod
    def extract_domains_from_json(file_path):
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
    def extract_domains_from_txt(file_path):
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
    def remove_out_of_scope_subdomains(path):
        seen = set()
        unique_lines = []

        with open(path, 'r') as infile:
            for line in infile:
                if line not in seen and GlobalEnv.domain in line:
                    seen.add(line)
                    unique_lines.append(line)

        with open(path, 'w') as outfile:
            outfile.writelines(unique_lines)

    @staticmethod
    def is_tool_installed(toolname:str):
        return shutil.which(toolname) is not None
    
    @staticmethod
    def is_tool_in_path(self, path_to_check: str):
        path_dirs = os.environ.get("PATH", "").split(":")
        return path_to_check in path_dirs
    
    @staticmethod
    def reformat_json_in_file(input_file:str, output_file:str):
        General.fix_json_file(input_file, output_file)

        with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write("[\n")
            first = True
            for line in f_in:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)  # Parse كل سطر على حدة
                if not first:
                    f_out.write(",\n")
                f_out.write(json.dumps(obj, indent=4, sort_keys=True, ensure_ascii=False))
                first = False
            f_out.write("\n]")
    
    @staticmethod
    def fix_json_file(input_file:str, output_file:str):
        with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write("[\n")
            first = True
            for line in f_in:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                if not first:
                    f_out.write(",\n")
                f_out.write(json.dumps(obj, ensure_ascii=False))
                first = False
            f_out.write("\n]")
    
    @staticmethod
    def get_max_number_of_threads():
        try:
            return int(GlobalEnv.max_threads) 
        except:
            return 10
    
    @staticmethod
    def is_valid_url(url):
        try:
            parsed = urlparse(url)
            return all([parsed.scheme, parsed.netloc])
        except:
            return False

