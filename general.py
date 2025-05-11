
import io
import os
import platform
import re
import socket
import sys
from urllib.parse import urlparse

from files import Files
from globalEnv import GlobalEnv


class General:
    def __init__(self):
        pass
    
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    __domainPattern = r'^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,63}$'
    
    @staticmethod
    def getIPfromDomain(domain):
        try:
            ip = socket.gethostbyname(domain)
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
    def ExecuteCommand(command:str, outputFile:str, isForSubDomainEnumeration=False, isForPortScanning = False, isForCrawling=False, isForFuzzing=False):
        os.system(command)
        Files.CopyFromTo(outputFile, GlobalEnv.GetLogFile())
        if isForSubDomainEnumeration:
            Files.CopyFromTo(outputFile, GlobalEnv.GetSubDomainsPath())
                        
        if isForCrawling:
            Files.CopyFromTo(outputFile, GlobalEnv.GetCrawlingPath())
        
        if isForFuzzing:
            Files.CopyFromTo(outputFile, GlobalEnv.GetFuzzingPath())

        if isForPortScanning:
            Files.CopyFromTo(outputFile, GlobalEnv.GetPortScanningPath())
    
    @staticmethod
    def GetDomainFromUrl(url):
        # Add 'https://' if missing to ensure urlparse works correctly
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Remove 'www.' if present
        if domain.startswith('www.'):
            domain = domain[4:]
        
        return domain