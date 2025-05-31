from Config import Config
from Tools.fuzzing import Fuzzing
from Tools.crawling import Crawling
from Tools.portScanning import PortScanning
from Tools.screenshot import ScreenShot
from Tools.subdomainEnumeration import SubdomainEnumeration
from globalEnv import GlobalEnv

class Runner:
    def __init__(self):
        Config.LoadConfig()
        self.__screenshot = ScreenShot()

    def Execute(self):
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
