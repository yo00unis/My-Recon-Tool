
from  general.general import General
from  globalEnv.globalEnv import GlobalEnv


class GoSpider:
    
    def __init__(self):
        pass
    
    def Execute(self, url):
        command = f'gospider -s {url} -d 100 -t 15 -c 5 --delay 1 --subs --js --other-source --robots --sitemap --user-agent --include-subs --verbose --output {GlobalEnv.GetGoSpider()}'
        return General.ExecuteRealTimeCommand(command, False, True)
