from Config import Config
from Tools.fuzzing import Fuzzing
from Tools.crawling import Crawling
from Tools.portScanning import PortScanning
from Tools.screenshot import ScreenShot
from Tools.subdomainEnumeration import SubdomainEnumeration
from general import General
from globalEnv import GlobalEnv
from installer import Installer
from linux_installer import LinuxInstaller


class Runner:
    def __init__(self):
        Config.LoadConfig()
        self.__screenshot = ScreenShot()
        self.__installer = Installer()
        self.__linuxinstaller = LinuxInstaller()

    def Execute(self):

        if General.GetOStype() == "Windows":
            self.__installer.Execute()
        else:
            self.__linuxinstaller.Execute()
        

        if GlobalEnv.GetDoSubdomainEnumeration():
            subdomainEnumeration = SubdomainEnumeration()
            subdomainEnumeration.Execute()

        if GlobalEnv.GetTakeScreenShots():
            self.__screenshot.Execute()

        if GlobalEnv.GetDoPortScanning():
            portScanning = PortScanning()
            portScanning.Execute()

        if GlobalEnv.GetDoCrawling():
            crawling = Crawling()
            crawling.Execute()

        if GlobalEnv.GetDoFuzzing():
            fuzzing = Fuzzing()
            fuzzing.Execute()
