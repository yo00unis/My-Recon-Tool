
from general import General
from globalEnv import GlobalEnv

class Commands:
    def __init__(self):
        pass
    
    @staticmethod
    def SubfinderCommands():    
        commands = [
            f'subfinder -d {GlobalEnv.GetDomain()} -all -o {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def Sublist3rCommands():    
        commands = [
            f"sublist3r -d {GlobalEnv.GetDomain()} -t 10 -o {GlobalEnv.GetTempFile()}"
        ]
        return commands
    
    @staticmethod
    def AmassCommands():    
        commands = [
            f'amass enum -passive -d {GlobalEnv.GetDomain()} -o {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def AssetFinderCommands():    
        commands = [
            f'assetfinder {GlobalEnv.GetDomain()} > {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def ChaosCommands():    
        commands = [
            f'chaos -d {GlobalEnv.GetDomain()} -o {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def HttpxCommands():    
        commands = [
            f'httpx -l {GlobalEnv.GetSubDomainsPath()} -status-code -fc 404 -title -tech-detect -follow-redirects -o {GlobalEnv.GetTempFile()}'
            #f'httpx -l {GlobalEnv.GetSubDomainsPath()} -status-code -fc 404 -o {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def KatanaCommands(url):    
        commands = [
           f'katana -u {General.GetStrippedString(url)} -d 100 -jc -delay 1 -c 15 -o {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def GauCommands(url):    
        commands = [
           f'gau {url} --subs --threads 15 --providers wayback,otx,commoncrawl --verbose --o {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def GoSpiderCommands(url):    
        commands = [
           f'gospider -s {url} -d 100 -t 15 -c 5 --delay 1 --subs --js --other-source --robots --sitemap --user-agent --include-subs --verbose --output {GlobalEnv.GetGoSpider()}'
        ]
        return commands
    
    @staticmethod
    def WaybackurlsCommands():    
        commands = [
           f'waybackurls {GlobalEnv.GetDomain()} > {GlobalEnv.GetTempFile()}'
        ]
        return commands
    
    @staticmethod
    def NmapCommands():    
        commands = []
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'nmap -sA -sU -p {ports} -A -iL {GlobalEnv.GetPortScanningTargetDomains()} -oN {GlobalEnv.GetTempFile()}'
            commands.append(command)
        else:    
            command = f'nmap -sA -sU --top-ports 100 -A -iL {GlobalEnv.GetPortScanningTargetDomains()} -oN {GlobalEnv.GetTempFile()}'
            commands.append(command)
            
        return commands
    
    @staticmethod
    def MasscanCommands():  
        commands = []
        ports = GlobalEnv.GetPorts()
        if len(ports) > 0:
            command = f'masscan -iL {GlobalEnv.GetPortScanningTarget()} -p {ports} > {GlobalEnv.GetTempFile()}'
            commands.append(command)
        else:    
            command = f'masscan -p1-65535 -iL {GlobalEnv.GetPortScanningTarget()} > {GlobalEnv.GetTempFile()}'  
            commands.append(command)
            
        return commands
    
    @staticmethod
    def NaabuCommands():  
        commands = []
        ports = GlobalEnv.GetPorts()
        if len(ports)>0:
            command = f'naabu -l {GlobalEnv.GetPortScanningTarget()} -p {ports} -o {GlobalEnv.GetTempFile()}'
        else:
            command = f'naabu -l {GlobalEnv.GetPortScanningTargetDomains()} -top-ports 1000 -o {GlobalEnv.GetTempFile()}'
        commands.append(command)
        return commands
    
    @staticmethod
    def FFUFCommands(url):  
        if url.endswith('/'):
            url += 'FUZZ'
        else:
            url += '/FUZZ'
              
        commands = [
           f'ffuf -u {url} -p 2 -r -w {GlobalEnv.GetFuffWordlist()} -rate 20 -recursion -o {GlobalEnv.GetTempJson()}'
        ]
        return commands
    