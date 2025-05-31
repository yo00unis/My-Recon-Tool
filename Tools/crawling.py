import re
from commands import Commands
from files import Files
from globalEnv import GlobalEnv
from general import General
from request import Requests
import concurrent.futures
from threading import Lock


class Crawling:
    def __init__(self):
        pass

    __pattern = re.compile(r"\b([23]\d{2}|401|403)\b")
    __write_lock = Lock()

    def __process_url(self, url):
        response = Requests.Get(url)
        if self.__pattern.search(str(response.status_code)) and (str(url)).startswith('https'):
            with self.__write_lock:
                Files.WriteToFile(GlobalEnv.GetTempFile(), "a", url)

    def __filterWaybackurlsResult(self):

        Files.WriteToFile(GlobalEnv.GetTempFile(), 'w', '')

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            with open(GlobalEnv.GetWaybackurls(), 'r') as f:
                for line in f:
                    url = line.strip()
                    if url:
                        futures.append(executor.submit(self.__process_url, url))
            concurrent.futures.wait(futures)

        concurrent.futures.wait(futures)

        Files.WriteToFile(GlobalEnv.GetWaybackurls(), "w", "")
        Files.CopyFromTo(GlobalEnv.GetTempFile(), GlobalEnv.GetWaybackurls)
        Files.WriteToFile(GlobalEnv.GetTempFile(), "w", "")
        Files.CopyFromTo(GlobalEnv.GetWaybackurls(), GlobalEnv.GetLogFile())
        Files.RemoveDuplicateFromFile(GlobalEnv.GetWaybackurls())

    def __Katana(self, url):
        commands = Commands.KatanaCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetKatana(), False, False, True)

    def __Gau(self, url):
        commands = Commands.GauCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetGau(), False, False, True)

    def __GoSpider(self, url):
        commands = Commands.GoSpiderCommands(url)
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetGoSpider(), False, False, True)

    def __Waybackurls(self):
        commands = Commands.WaybackurlsCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetWaybackurls(), False, False, True)

    def __ReadSubdomains(self):
        if not GlobalEnv.GetDoSubdomainEnumeration():
            if Files.IsFileExists(GlobalEnv.GetSubDomainsPath()):
                Files.CopyFromTo(GlobalEnv.GetSubDomainsPath(), GlobalEnv.GetHttpx())
        Files.RemoveDuplicateFromFile(GlobalEnv.GetHttpx())

    def Execute(self):
        self.__ReadSubdomains()
        self.__Waybackurls()
        self.__filterWaybackurlsResult()
        try:
            with open(
                f"{GlobalEnv.GetHttpx()}", "r", encoding="utf-8", errors="ignore"
            ) as f:
                for line in f:
                    url = (((str(line)).split(" ["))[0]).strip()
                    self.__Katana(url)
                    self.__Gau(url)
                    self.__GoSpider(url)
        except Exception as e:
            print(f"Error running: {str(e)}")
