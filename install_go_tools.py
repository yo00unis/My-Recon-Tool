
import os
import shutil


class GoToolsInstaller:

    def __init(self):
        self.__local_bin_path = 'export PATH="$HOME/go/bin:$PATH"'

    def __isToolInstalled(self, toolname:str):
        return shutil.which(toolname.strip()) is not None

    def __installSubfinder(self):
        if not self.__isToolInstalled("subfinder"):
            os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installSublister(self):
        if not self.__isToolInstalled("sublist3r"):
            os.system("pipx install sublist3r")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installAssetFinder(self):
        if not self.__isToolInstalled("assetfinder"):
            os.system("go install github.com/tomnomnom/assetfinder@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installChaos(self):
        if not self.__isToolInstalled("chaos"):
            os.system("go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installAmass(self):
        if not self.__isToolInstalled("amass"):
            os.system("go get -u github.com/caffix/amass")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installHttpx(self):
        if not self.__isToolInstalled("httpx"):
            os.system("go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installNaabu(self):
        if not self.__isToolInstalled("naabu"):
            os.system("go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installKatana(self):
        if not self.__isToolInstalled("katana"):
            os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installGau(self):
        if not self.__isToolInstalled("gau"):
            os.system("go install github.com/lc/gau/v2/cmd/gau@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installGoSpider(self):
        if not self.__isToolInstalled("gospider"):
            os.system("go install github.com/jaeles-project/gospider@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installWaybackurls(self):
        if not self.__isToolInstalled("waybackurls"):
            os.system("go install github.com/tomnomnom/waybackurls@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installFFUF(self):
        if not self.__isToolInstalled("ffuf"):
            os.system("go install github.com/ffuf/ffuf/v2@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()

    def __installGowitness(self):
        if not self.__isToolInstalled("gowitness"):
            os.system("go install github.com/sensepost/gowitness@latest")
            if not self.__is_in_path(self.__local_bin_path):
                self.__add_go_tools_to_path()
    
    def __add_go_tools_to_path(self):
        self.__add_to_path(self.__local_bin_path)
    
    def __is_in_path(self, path_to_check: str):
        path_dirs = os.environ.get("PATH", "").split(":")
        return path_to_check in path_dirs

    
    def Execute(self):
        self.__installAmass()
        self.__installAssetFinder()
        self.__installChaos()
        self.__installSubfinder()
        self.__installSublister()
        self.__installHttpx()
        self.__installKatana()
        self.__installWaybackurls()
        self.__installGau()
        self.__installGoSpider()
        self.__installNaabu()
        self.__installFFUF()
        self.__installGowitness()
