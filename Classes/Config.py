import json
import os
from pathlib import Path
from Classes.general import General
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
    def __ReadConfigFile():
        try:
            conf_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../config.json")
            )

            with open(conf_path, "r") as file:
                data = json.load(file)

            Config.__DealingWithDirectoryConfig(str(data["ResultDirectory"]))
            GlobalEnv.SetDomain(data["Domain"])
            GlobalEnv.SetFuffWordlist(data["FuzzingWordlist"])
            GlobalEnv.SetDoSubdomainEnumeration(data["DoSubdomainEnumeration"])
            GlobalEnv.SetTakeScreenShots(data["TakeScreenShots"])
            GlobalEnv.SetPorts(data["Ports"])
            GlobalEnv.SetDoPortScanning(data["DoPortScanning"])
            GlobalEnv.SetDoCrawling(data["DoCrawling"])
            GlobalEnv.SetDoFuzzing(data["DoFuzzing"])

            if len(GlobalEnv.GetResultFolder()) == 0:
                General.ReadResultDirectory()
            if len(GlobalEnv.GetDomain()) == 0:
                General.ReadDomain()
            if len(GlobalEnv.GetFuffWordlist()) == 0 and not GlobalEnv.GetDoFuzzing():
                General.ReadFFUFwordlist()

        except FileNotFoundError:
            print(f"[!] config.json not found at: {conf_path}")
            return None
        except json.JSONDecodeError:
            print("[!] Failed to parse config.json (invalid JSON)")
            return None
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
            return None

    @staticmethod
    def __InitialMessage():
        print("--------------------------------")
        print("Created By Younis 2003")
        print("--------------------------------")
        print("if you want to exit tool press Ctrl + c")
        print("--------------------------------")

    @staticmethod
    def __SetGlobalEnv():
        # Create Result Folders
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}subdomains")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}portScanning")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}crawling")
        Files.CreateFolder(f"{GlobalEnv.GetResultFolder()}fuzzing")
        
        # set result folders
        GlobalEnv.SetSubDomainsFolderPath(f"{GlobalEnv.GetResultFolder()}subdomains")
        GlobalEnv.SetPortScanningFolderPath(f"{GlobalEnv.GetResultFolder()}portScanning")
        GlobalEnv.SetCrawlingFolderPath(f"{GlobalEnv.GetResultFolder()}crawling")
        GlobalEnv.SetFuzzingFolderPath(f"{GlobalEnv.GetResultFolder()}fuzzing")

        # Set log file and base file containing all results in the folder
        GlobalEnv.SetLogFile(f"{GlobalEnv.GetResultFolder()}logs.txt")

        GlobalEnv.SetSubDomainsPath(f"{GlobalEnv.GetResultFolder()}subdomains/subdomains.txt")

        GlobalEnv.SetCrtSH(f"{GlobalEnv.GetResultFolder()}subdomains/crtSH.json")
        GlobalEnv.SetCrtShText(f"{GlobalEnv.GetResultFolder()}subdomains/crtSHtext.txt")

        # Set port scanning result files
        GlobalEnv.SetPortScanningTarget(
            f"{GlobalEnv.GetResultFolder()}portScanning/Arecords.txt"
        )
        GlobalEnv.SetPortScanningTargetDomains(
            f"{GlobalEnv.GetResultFolder()}portScanning/targetDomain.txt"
        )
        GlobalEnv.SetDnsRecords(
            f"{GlobalEnv.GetResultFolder()}portScanning/dnsRecords.txt"
        )

        # Set temp file
        GlobalEnv.SetTempFile(f"{GlobalEnv.GetResultFolder()}temp.txt")
        GlobalEnv.SetTempJson(f"{GlobalEnv.GetResultFolder()}temp.json")

        # Set screenshot result path
        GlobalEnv.SetGowitness(f"{GlobalEnv.GetResultFolder()}screenshots")

    @staticmethod
    def __CheckDoSubdomainEnumerationConfig():
        # append domain to httpx if config domain not wildcard
        if not GlobalEnv.GetDoSubdomainEnumeration():
            Files.WriteToFile(GlobalEnv.GetHttpx(), "a", GlobalEnv.GetDomain())

    @staticmethod
    def LoadConfig():
        Config.__InitialMessage()
        Config.__ReadConfigFile()
        Config.__SetGlobalEnv()
        Config.__CheckDoSubdomainEnumerationConfig()
        Config.__InitialMessage()
