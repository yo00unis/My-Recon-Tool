import argparse
from pathlib import Path
from Classes.files import Files
from Classes.globalEnv import GlobalEnv


class Config:
    def __init__(self):
        pass

    @staticmethod
    def __DealingWithDirectoryConfig(dir: str):
        if "../" in dir:
            lastSlashIndex = dir.rfind("/")
            if 1 + lastSlashIndex == len(dir):
                dirName = ""
            else:
                dirName = dir[1 + lastSlashIndex :]
            if lastSlashIndex % 2 == 0:
                levels = int(lastSlashIndex / 2)
            else:
                levels = int((lastSlashIndex - 1) / 2)
            path = Path.cwd()
            for i in range(0, levels):
                path = path.parent
            sDir = str(path)
            if sDir.endswith("/") or sDir.endswith("\\"):
                sDir += dirName
            else:
                sDir += f"/{dirName}"
            GlobalEnv.SetResultFolder(sDir)
        else:
            GlobalEnv.SetResultFolder(dir)


    @staticmethod
    def __InitialMessage():
        print("--------------------------------")
        print("Created By Younis 2003")
        print("--------------------------------")
        print("if you want to exit tool press Ctrl + c")
        print("--------------------------------")

    @staticmethod
    def __set_global_env_folders_files():
        # Create Result Folders
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}subdomains")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}portScanning")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}crawling")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}fuzzing")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}subdomains/httpx")
        
        # set result folders
        GlobalEnv.SetSubDomainsFolderPath(f"{GlobalEnv.GetResultFolder()}subdomains")
        GlobalEnv.SetPortScanningFolderPath(f"{GlobalEnv.GetResultFolder()}portScanning")
        GlobalEnv.SetCrawlingFolderPath(f"{GlobalEnv.GetResultFolder()}crawling")
        GlobalEnv.SetFuzzingFolderPath(f"{GlobalEnv.GetResultFolder()}fuzzing")
        GlobalEnv.SetHttpxPath(f"{GlobalEnv.GetResultFolder()}subdomains/httpx")
        GlobalEnv.SetLogFile(f"{GlobalEnv.GetResultFolder()}logs.txt")
        GlobalEnv.SetSubDomainsFile(f"{GlobalEnv.GetResultFolder()}subdomains/subdomains.txt")
        GlobalEnv.SetDNSPath(f"{GlobalEnv.GetResultFolder()}portScanning/dns.json")
        GlobalEnv.SetCrtSH(f"{GlobalEnv.GetResultFolder()}subdomains/crtSH.json")
        GlobalEnv.SetCrtShText(f"{GlobalEnv.GetResultFolder()}subdomains/crtSHtext.txt")
        GlobalEnv.SetPortScanningARecords(f"{GlobalEnv.GetResultFolder()}portScanning/Arecords.txt")
        GlobalEnv.SetGowitness(f"{GlobalEnv.GetResultFolder()}screenshots")

    @staticmethod
    def __cli_parser():
        parser = argparse.ArgumentParser(description="Recon Tool CLI")
        parser.add_argument("-rd", "--result-dir", default="ReconResult", help="Directory to save results")
        parser.add_argument("-d", "--domain", required=True, help="Target domain")
        parser.add_argument("-se", "--subdomain-enumeration", action="store_true", help="Do subdomain enumeration")
        parser.add_argument("-sh", "--screenshots", action="store_true", help="Take screenshots")
        parser.add_argument("-ps", "--port-scan", action="store_true", help="Do port scanning")
        parser.add_argument("-p", "--ports", default="443,80", help="Ports to scan (comma separated)")
        parser.add_argument("-c", "--crawling", action="store_true", help="Do crawling")
        parser.add_argument("-f", "--fuzzing", action="store_true", help="Do fuzzing")
        parser.add_argument("-fw", "--fuzz-wordlist", default="directory-list-2.3-medium.txt", help="Fuzzing wordlist file")
        parser.add_argument("-t", "--threads", type=int, default=15, help="Max number of threads")
        args = parser.parse_args()
        if not args.domain:
            args.domain = input("[?] Enter target domain: ").strip()
        if not args.result_dir:
            args.result_dir = input("[?] Enter result folder: ").strip() or "ReconResult"
        return args
    
    @staticmethod 
    def __set_cli_global_env(args):
        Config.__DealingWithDirectoryConfig(args.result_dir)
        GlobalEnv.SetDomain(args.domain)
        GlobalEnv.SetFuffWordlist(args.fuzz_wordlist)
        GlobalEnv.SetDoSubdomainEnumeration(args.subdomain_enumeration)
        GlobalEnv.SetTakeScreenShots(args.screenshots)
        GlobalEnv.SetPorts(args.ports)
        GlobalEnv.SetDoPortScanning(args.port_scan)
        GlobalEnv.SetDoCrawling(args.crawling)
        GlobalEnv.SetDoFuzzing(args.fuzzing)
        GlobalEnv.SetMaxThreads(args.threads)

    @staticmethod
    def LoadConfig():
        Config.__InitialMessage()
        args = Config.__cli_parser()
        Config.__set_cli_global_env(args)
        Config.__set_global_env_folders_files()
