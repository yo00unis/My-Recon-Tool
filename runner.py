


from Config import Config
from Tools.fuzzing import Fuzzing
from Tools.crawling import Crawling
from Tools.portScanning import PortScanning
from Tools.subdomainEnumeration import SubdomainEnumeration
from globalEnv import GlobalEnv

class Runner:
    def __init__(self):
        Config.LoadConfig()

    def Execute(self):
        if GlobalEnv.GetIsWildcard():
            subdomainEnumeration = SubdomainEnumeration()
            subdomainEnumeration.Execute()

        if GlobalEnv.GetDoPortScanning():
            portScanning = PortScanning()
            portScanning.Execute()

        if GlobalEnv.GetDoCrawling():
            crawling = Crawling()
            crawling.Execute()

        if GlobalEnv.GetDoFuzzing():
            fuzzing = Fuzzing()
            fuzzing.Execute()
