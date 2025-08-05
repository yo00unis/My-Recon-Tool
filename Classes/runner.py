from Classes.Config import Config
from Classes.Tools.tools_execution import Crawling, Fuzzing, PortScanning, ScreenShot, SubdomainEnumeration
from Classes.Tools.tools_installer import LinuxInstaller, WindowsInstaller


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

    def Execute(self):

        self.__windowsInstaller.Execute()
        self.__linuxInstaller.Execute()
        self.__subdomainEnumeration.Execute()
        self.__screenshot.Execute()
        self.__portScanning.Execute()
        self.__crawling.Execute()
        self.__fuzzing.Execute()
