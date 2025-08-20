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
            GlobalEnv.result_folder = sDir
        else:
            GlobalEnv.result_folder = dir


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
        Files.create_folder(f"{GlobalEnv.result_folder}")
        Files.create_folder(f"{GlobalEnv.result_folder}/subdomains")
        Files.create_folder(f"{GlobalEnv.result_folder}/portScanning")
        Files.create_folder(f"{GlobalEnv.result_folder}/crawling")
        Files.create_folder(f"{GlobalEnv.result_folder}/fuzzing")
        Files.create_folder(f"{GlobalEnv.result_folder}/subdomains/httpx")
        
        # set result folders
        GlobalEnv.subdomains_folder = f"{GlobalEnv.result_folder}/subdomains"
        GlobalEnv.port_scanning_folder = f"{GlobalEnv.result_folder}/portScanning"
        GlobalEnv.crawling_folder = f"{GlobalEnv.result_folder}/crawling"
        GlobalEnv.fuzzing_folder = f"{GlobalEnv.result_folder}/fuzzing"
        GlobalEnv.httpx_path = f"{GlobalEnv.result_folder}/subdomains/httpx"
        GlobalEnv.log_file = f"{GlobalEnv.result_folder}/logs.txt"
        GlobalEnv.subdomains_file = f"{GlobalEnv.result_folder}/subdomains/subdomains.txt"
        GlobalEnv.dns_path = f"{GlobalEnv.result_folder}/portScanning/dns_records.json"
        GlobalEnv.crtsh = f"{GlobalEnv.result_folder}/subdomains/crtSH.json"
        GlobalEnv.crtsh_txt = f"{GlobalEnv.result_folder}/subdomains/crtSHtext.txt"
        GlobalEnv.port_scanning_a_records = f"{GlobalEnv.result_folder}/portScanning/a_records.txt"
        GlobalEnv.gowitness = f"{GlobalEnv.result_folder}/screenshots"

        GlobalEnv.user_agents_file = f"Files/user-agents.txt"

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
        parser.add_argument("-fw", "--fuzz-wordlist", default="Files/dicc.txt", help="Fuzzing wordlist file")
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
        GlobalEnv.domain = args.domain
        GlobalEnv.ffuf_wordlist = args.fuzz_wordlist
        GlobalEnv.do_subdomain_enumeration = args.subdomain_enumeration
        GlobalEnv.take_screenshot = args.screenshots
        GlobalEnv.ports = args.ports
        GlobalEnv.do_port_scanning = args.port_scan
        GlobalEnv.do_crawling = args.crawling
        GlobalEnv.do_fuzzing = args.fuzzing
        GlobalEnv.max_threads = args.threads

    @staticmethod
    def LoadConfig():
        Config.__InitialMessage()
        args = Config.__cli_parser()
        Config.__set_cli_global_env(args)
        Config.__set_global_env_folders_files()
