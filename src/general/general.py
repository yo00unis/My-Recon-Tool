import os
from urllib.parse import urlparse
from  files.files import Files
import platform
import re
import subprocess
import sys
import io
from globalEnv.globalEnv import GlobalEnv

class General:
    
    def __init__(self):
        self.__domainPattern = r'^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,63}$'
    
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    
    def IsDomainValid(self, domain):
        return bool(re.fullmatch(self.__domainPattern, domain))
    
    def GetUniqueURLs(self, urls):
        return list(set(urls))
    
    def ReadResultDirectory(self):
        while True:
            fpath = input('Enter valid directory to save result: ')
            if Files.ValidateDirectoryPath(fpath):
                GlobalEnv.SetResultFolder(self.GetStrippedString(fpath))
                return True
            
            if self.GetOStype() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
                
            print('invalid path!')
    
    def ReadDomain(self):
        while True:
            domain = input('Enter valid domain: ')
            if self.IsDomainValid(self.GetStrippedString(domain)):
                GlobalEnv.SetDomain(domain)
                return True
            
            if self.GetOStype() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
                
            print('invalid domain!')
    
    def ReadFFUFwordlist(self):
        ffufWordlist = input('Enter ffuf wordlist: ')
        GlobalEnv.SetFuffWordlist(str(ffufWordlist))
        return True

    
    def GetOStype(self):
        return platform.system()
    
    
    def ExecuteBasicCommand(self,command:str):
        command_parts = command.split()
        return subprocess.run(command_parts, capture_output=True, text=True)
    
    @staticmethod
    def ExecuteRealTimeCommand(command:str, isForSubDomainEnumeration=False, isForCrawling=False, isForFuzzing=False, urlFuzzing='', isForPortScanning=False):
        from log.logger import Logger
        if len(command) == 0:
            Logger.log(GlobalEnv.GetLogFile(), 'Command is empty\n')
            raise ValueError('Command is empty')
        
        command_parts = command.split()
        try:
            # Run command with real-time output
            process = subprocess.Popen(
                command_parts,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True,
                encoding='utf-8'
            )
            
            # Print output in real-time  
            Logger.log(f"{command_parts[0]} is running... (Press Ctrl+C to stop)\n")          
            print(f"{command_parts[0]} is running... (Press Ctrl+C to stop)\n")
            
            for line in process.stdout:
                l = f'{General.GetStrippedString(str(line))}\n'
                Logger.logAndPrintToConsole(line=l)
                
                if isForSubDomainEnumeration:
                    Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), 'a', l)
                        
                if isForCrawling:
                    Files.WriteToFile(GlobalEnv.GetCrawlingPath(), 'a', l)
                
                if isForFuzzing:
                    s =  f'{General.GetStrippedString(str(urlFuzzing))}, {l}'
                    Files.WriteToFile(GlobalEnv.GetFuzzingPath(), 'a', s)

                if isForPortScanning:
                    Files.WriteToFile(GlobalEnv.GetPortScanningPath(), 'a', l)
                
            # Wait for completion
            process.wait()

            Logger.log(f"\n\nProcess completed with return code: {process.returncode}")
            print(f"\n\nProcess completed with return code: {process.returncode}")
            return process
            
        except KeyboardInterrupt:
            Logger.log("\nProcess interrupted by user")
            print("\nProcess interrupted by user")
            process.terminate()
        except Exception as e:
            Logger.log(f"Error running: {str(e)}")
            print(f"Error running: {str(e)}")
    
    @staticmethod
    def ExecuteRealTimeCommandAndSaveToFile(command:str, path:str, fileType='w', isForSubDomainEnumeration=False, isForCrawling=False, isForFuzzing=False, urlFuzzing='', isForPortScanning=False):
        from log.logger import Logger
        if len(command) == 0:
            Logger.log('Command is empty')
            raise ValueError('Command is empty')
        
        command_parts = command.split()
        try:
            # Run command with real-time output
            process = subprocess.Popen(
                command_parts,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True,
                encoding='utf-8'
            )
            
            Logger.log(f"{command_parts[0]} is running... (Press Ctrl+C to stop)\n")          
            print(f"{command_parts[0]} is running... (Press Ctrl+C to stop)\n")
            
            with open(f'{path}', f'{fileType}', encoding="utf-8", errors='ignore') as f:
                for line in process.stdout:
                    l = f'{General.GetStrippedString(str(line))}\n'
                    Logger.logAndPrintToConsole(line=l)
                    f.write(l)
                    
                if isForSubDomainEnumeration:
                    Files.WriteToFile( GlobalEnv.GetSubDomainsPath(), 'a', l)
                        
                if isForCrawling:
                    Files.WriteToFile( GlobalEnv.GetCrawlingPath(), 'a', l)
                
                if isForFuzzing:
                    s =  f'{General.GetStrippedString(str(urlFuzzing))}, {l}'
                    Files.WriteToFile( GlobalEnv.GetFuzzingPath(), 'a', s)

                if isForPortScanning:
                    Files.WriteToFile( GlobalEnv.GetPortScanningPath(), 'a', l)
                        
            # Wait for completion
            process.wait()

            Logger.log(f"\n\nProcess completed with return code: {process.returncode}")
            print(f"\n\nProcess completed with return code: {process.returncode}")
            return process
            
        except KeyboardInterrupt:
            Logger.log("\nProcess interrupted by user")
            print("\nProcess interrupted by user")
            process.terminate()
        except Exception as e:
            Logger.log(f"Error running: {str(e)}")
            print(f"Error running: {str(e)}")

    
    def ExecuteTesting(self, command:str):
        if len(command) == 0:
            raise ValueError('Command is empty')
    
        command_parts = command.split()
        try:
            # Run command with real-time output
            process = subprocess.Popen(
                command_parts,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,  # Line buffered
                universal_newlines=True,
                encoding='utf-8'
            )
            
            print(f"{command_parts[0]} is running... (Press Ctrl+C to stop)\n")
            
            for line in process.stdout:
                print(line, end='')
                
            # Wait for completion
            process.wait()

            print(f"\n\nProcess completed with return code: {process.returncode}")
            return process
            
        except KeyboardInterrupt:
            print("\nProcess interrupted by user")
            process.terminate()
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    @staticmethod
    def GetStrippedString(s:str):
        return s.strip()
    
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