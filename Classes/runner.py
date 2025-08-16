from concurrent.futures import ThreadPoolExecutor, as_completed
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
        Files.write_to_file(GlobalEnv.subdomains_file, 'a', GlobalEnv.domain)

    def Execute(self):
        self.__prepare()

        if General.get_os_type() == "Windows":
            self.__windowsInstaller.Execute()
        elif General.get_os_type() == "Linux":
            self.__linuxInstaller.Execute()
        
        if GlobalEnv.do_subdomain_enumeration:
            self.__subdomainEnumeration.Execute()

        tasks = []

        if GlobalEnv.take_screenshot:
            tasks.append(self.__screenshot.Execute)
        if GlobalEnv.do_port_scanning:
            tasks.append(self.__portScanning.Execute)
        if GlobalEnv.do_crawling:
            tasks.append(self.__crawling.Execute)
        if GlobalEnv.do_fuzzing:
            tasks.append(self.__fuzzing.Execute)
        
        with ThreadPoolExecutor(max_workers=General.get_max_number_of_threads()) as executor:
            futures = [executor.submit(task) for task in tasks]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error in module: {e}")
