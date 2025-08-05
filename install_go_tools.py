
import os
import shutil


class GoToolsInstaller:

    def __init(self):
        self.installAmass()
        self.installAssetFinder()
        self.installChaos()
        self.installSubfinder()
        self.installSublister()
        self.installHttpx()
        self.installKatana()
        self.installWaybackurls()
        self.installGau()
        self.installGoSpider()
        self.installNaabu()
        self.installFFUF()
        self.installGowitness()

    def isToolInstalled(self, toolname:str):
        return shutil.which(toolname.strip()) is not None

    def installSubfinder(self):
        if not self.isToolInstalled("subfinder"):
            os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")

    def installSublister(self):
        if not self.isToolInstalled("sublist3r"):
            os.system("pipx install sublist3r")

    def installAssetFinder(self):
        if not self.isToolInstalled("assetfinder"):
            os.system("go install github.com/tomnomnom/assetfinder@latest")

    def installChaos(self):
        if not self.isToolInstalled("chaos"):
            os.system("go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest")

    def installAmass(self):
        if not self.isToolInstalled("amass"):
            os.system("go get -u github.com/caffix/amass")

    def installHttpx(self):
        if not self.isToolInstalled("httpx"):
            os.system("go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest")

    def installNaabu(self):
        if not self.isToolInstalled("naabu"):
            os.system("go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest")

    def installKatana(self):
        if not self.isToolInstalled("katana"):
            os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")

    def installGau(self):
        if not self.isToolInstalled("gau"):
            os.system("go install github.com/lc/gau/v2/cmd/gau@latest")

    def installGoSpider(self):
        if not self.isToolInstalled("gospider"):
            os.system("go install github.com/jaeles-project/gospider@latest")

    def installWaybackurls(self):
        if not self.isToolInstalled("waybackurls"):
            os.system("go install github.com/tomnomnom/waybackurls@latest")

    def installFFUF(self):
        if not self.isToolInstalled("ffuf"):
            os.system("go install github.com/ffuf/ffuf/v2@latest")

    def installGowitness(self):
        if not self.isToolInstalled("gowitness"):
            os.system("go install github.com/sensepost/gowitness@latest")

    def add_go_bin_to_path(self):
        go_bin = os.path.expandvars(r'%USERPROFILE%\go\bin')
        self.add_path_to_user_path(go_bin)

    def installPipLibraries(self):
        if not self.isToolInstalled("dnspython"):
            os.system("pipx install dnspython")