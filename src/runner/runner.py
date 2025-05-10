from globalEnv.globalEnv import GlobalEnv
from config.config import Config
from crawling.base import CrawlingBase
from fuzzing.base import FuzzingBase
from port_scan.base import PortScanningBase
from subdomain.base import SubdomainEnumerationBase


class Runner:
    def __init__(self):
        Config.LoadConfig()

    def Execute(self):
        if GlobalEnv.GetIsWildcard():
            subdomainEnumerationBase = SubdomainEnumerationBase()
            subdomainEnumerationBase.Exexute()

        if GlobalEnv.GetDoPortScanning():
            portScanningBase = PortScanningBase()
            portScanningBase.Exexute()

        if GlobalEnv.GetDoCrawling():
            crawlingBase = CrawlingBase()
            crawlingBase.Exexute()

        if GlobalEnv.GetDoFuzzing():
            fuzzingBase = FuzzingBase()
            fuzzingBase.Exexute()
