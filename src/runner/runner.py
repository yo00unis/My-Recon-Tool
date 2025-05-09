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

        portScanningBase = PortScanningBase()
        portScanningBase.Exexute()

        crawlingBase = CrawlingBase()
        crawlingBase.Exexute()

        fuzzingBase = FuzzingBase()
        fuzzingBase.Exexute()
