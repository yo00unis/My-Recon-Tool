from concurrent.futures import ThreadPoolExecutor
from Classes.Config import Config
from Classes.Tools.tools_execution import Crawling, Fuzzing, PortScanning, ScreenShot, SubdomainEnumeration
from Classes.Tools.tools_installer import LinuxInstaller, WindowsInstaller
from Classes.files import Files
from Classes.general import General
from Classes.globalEnv import GlobalEnv


class Runner:
    def __init__(self):
        Config.LoadConfig()
        self.__subdomainEnumeration = SubdomainEnumeration()
        self.__portScanning = PortScanning()
        self.__crawling = Crawling()
        self.__fuzzing = Fuzzing()
        self.__screenshot = ScreenShot()
        self.__windowsInstaller = WindowsInstaller()
        self.__linuxInstaller = LinuxInstaller()

    def __prepare(self):
        Files.WriteToFile(GlobalEnv.GetSubDomainsPath(), 'a', GlobalEnv.GetDomain())

    def Execute(self):
        self.__prepare()

        if General.GetOStype() == "Windows":
            self.__windowsInstaller.Execute()
        if General.GetOStype() == "Linux":
            self.__linuxInstaller.Execute()
        
        if GlobalEnv.GetDoSubdomainEnumeration():
            self.__subdomainEnumeration.Execute()

        tasks = []

        if GlobalEnv.GetTakeScreenShots():
            tasks.append(self.__screenshot.Execute)
            self.__screenshot.Execute()
        if GlobalEnv.GetDoPortScanning():
            tasks.append(self.__portScanning.Execute)
        if GlobalEnv.GetDoCrawling():
            tasks.append(self.__crawling.Execute)
        if GlobalEnv.GetDoFuzzing():
            tasks.append(self.__fuzzing.Execute)
        
        with ThreadPoolExecutor(max_workers=General.GetMaxThreadsNumber()) as executor:
            futures = [executor.submit(task) for task in tasks]
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print(f"Error in module: {e}")
