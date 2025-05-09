from crawling.gau import Gau
from crawling.go_spider import GoSpider
from crawling.katana import Katana
from crawling.waybackurls import Waybackurls
from globalEnv.globalEnv import GlobalEnv


class CrawlingBase:
    def __init__(self):
        self.__CreateObjects()

    def __CreateObjects(self):
        self.__katana = Katana()
        self.__gau = Gau()
        self.__gospider = GoSpider()
        self.__waybackurls = Waybackurls()

    def __DoCrawling(self):
        try:
            with open(
                f"{GlobalEnv.GetHttpx()}", "r", encoding="utf-8", errors="ignore"
            ) as f:
                for line in f:
                    url = (((str(line)).split(" ["))[0]).strip()
                    self.__katana.Execute(url)
                    self.__gau.Execute(url)
                    self.__gospider.Execute(url)

            self.__waybackurls.Execute()
        except Exception as e:
            print(f"Error running: {str(e)}")

    def Exexute(self):
        self.__DoCrawling()
