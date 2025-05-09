
from subdomain.httpx import HTTPx
from subdomain.chaos import Chaos
from subdomain.assetfinder import AssetFinder
from subdomain.amass import Amass
from subdomain.sublister import Sublist3r
from subdomain.subfinder import Subfinder
from subdomain.crt_sh import CrtSH


class SubdomainEnumerationBase:
    def __init__(self):
        self.__CreateObjects()
    
    def __CreateObjects(self):
        self.__crtsh = CrtSH()
        self.__subfinder = Subfinder()
        self.__sublister = Sublist3r()
        self.__amass = Amass()
        self.__assetfinder = AssetFinder()
        self.__chaos = Chaos()
        self.__httpx = HTTPx()
    
    def __DoSubDomainEnumeration(self):
        try:
            self.__crtsh.Execute()
            self.__subfinder.Execute()
            self.__sublister.Execute()
            self.__chaos.Execute()
            #TheHarvester.StaticExecute()
            self.__assetfinder.Execute()
            self.__amass.Execute()
            self.__httpx.Execute()
        except Exception as e:
            print(f"Error running: {str(e)}")
    
    def Exexute(self):
        self.__DoSubDomainEnumeration()
        
        