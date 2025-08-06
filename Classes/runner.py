from Classes.Config import Config
from Classes.Tools.tools_execution import Crawling, Fuzzing, PortScanning, ScreenShot, SubdomainEnumeration
from Classes.Tools.tools_installer import LinuxInstaller, WindowsInstaller
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

    def Execute(self):
        if General.GetOStype() == "Windows":
            self.__windowsInstaller.Execute()
        if General.GetOStype() == "Linux":
            self.__linuxInstaller.Execute()
        if GlobalEnv.GetDoSubdomainEnumeration():
            self.__subdomainEnumeration.Execute()
        if GlobalEnv.GetTakeScreenShots():
            self.__screenshot.Execute()
        if GlobalEnv.GetDoPortScanning():
            self.__portScanning.Execute()
        if GlobalEnv.GetDoCrawling():
            self.__crawling.Execute()
        if GlobalEnv.GetDoFuzzing():
            self.__fuzzing.Execute()
