
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
    
    @staticmethod
    def send(method: str, url: str, parameters=None, json_body=None):
        if method in ("GET", "DELETE"):
            return Requests.__reqSession.request(
                method=method, url=url, params=parameters, verify=False
            )
        else:
            return Requests.__reqSession.request(
                method=method, url=url, params=parameters, json=json_body, verify=False
            )