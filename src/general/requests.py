
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Requests:
    
    __reqSession = requests.Session()
    
    def __init__(self):
        pass
    
    @staticmethod
    def Get(url):
        return Requests.__reqSession.get(url=url, verify=False)