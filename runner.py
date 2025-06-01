from Config import Config
from Tools.fuzzing import Fuzzing
from Tools.crawling import Crawling
from Tools.portScanning import PortScanning
from Tools.screenshot import ScreenShot
from Tools.subdomainEnumeration import SubdomainEnumeration
from globalEnv import GlobalEnv
from installer import Installer


class Runner:
    def __init__(self):
        Config.LoadConfig()
        self.__screenshot = ScreenShot()
        self.__installer = Installer()

    def Execute(self):
        self.__installer.Execute()

        if GlobalEnv.GetDoSubdomainEnumeration():
            subdomainEnumeration = SubdomainEnumeration()
            subdomainEnumeration.Execute()

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
