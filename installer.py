import os
import shutil
import subprocess

from general import General 

class Installer:
    def __init__(self):
        pass

    def __isToolInstalled(self, toolname:str):
        return shutil.which(toolname.strip()) is not None

    def __read_user_path(self):
        import winreg
        try:
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ
            ) as key:
                path_value, _ = winreg.QueryValueEx(key, "Path")
                return path_value
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Error reading user PATH: {e}")
            return ""

    def __add_path_to_user_path(self, new_path_entry):
        import winreg

        new_path_entry = os.path.normpath(new_path_entry.strip())

        if not os.path.exists(new_path_entry):
            print(f"Warning: The path '{new_path_entry}' does not exist on disk.")
            return False

        current_path = self.__read_user_path()
        paths = current_path.split(os.pathsep) if current_path else []

        if any(os.path.normcase(p) == os.path.normcase(new_path_entry) for p in paths):
            print(f"{new_path_entry} is already in user PATH.")
            return True

        updated_path = current_path + os.pathsep + new_path_entry if current_path else new_path_entry

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, updated_path)
            return True
        except Exception as e:
            return False

    def __add_path_to_user_path_linux(self, new_path_entry, shell_rc=None):
        if shell_rc is None:
            shell_rc = os.path.expanduser('source ~/.bashrc')

        new_path_entry = new_path_entry.rstrip('/')

        # Check if the path is already exported in shell_rc
        if os.path.exists(shell_rc):
            with open(shell_rc, 'r') as f:
                content = f.read()
            if new_path_entry in content:
                print(f"{new_path_entry} is already in PATH in {shell_rc}")
                return True
        else:
            content = ""

        # Append export line
        export_line = f'\n# Added by YourClass\nexport PATH="$PATH:{new_path_entry}"\n'

        try:
            with open(shell_rc, 'a') as f:
                f.write(export_line)
            return True
        except Exception as e:
            print(f"Failed to update {shell_rc}: {e}")
            return False

    def __installScoope(self):
        if not self.__isToolInstalled("scoop"):
            if General.GetOStype() == "Windows":
                os.system('powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"')
                os.system('powershell -Command "iwr -useb get.scoop.sh | iex"')
                scoop_shims = os.path.join(os.path.expanduser("~"), "scoop", "shims")
                self.__add_path_to_user_path(scoop_shims)
        return True

    def __installPipx(self):
        if not self.__isToolInstalled("pipx"):
            if General.GetOStype() == 'Windows':
                os.system('powershell -Command "scoop install pipx"')
                user_bin = os.path.expandvars(r'%USERPROFILE%\.local\bin')
                self.__add_path_to_user_path(user_bin)
            else:
                os.system("python3 -m pip install --user pipx")
                os.system("python3 -m pipx ensurepath")
                # os.system('bash -c "source ~/.bashrc"')
                subprocess.run("source ~/.bashrc", shell=True, executable="/bin/bash")
                return self.__isToolInstalled("pipx")
        return True

    def __installSubfinder(self):
        if not self.__isToolInstalled("subfinder"):
            os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")

    def __installSublister(self):
        if not self.__isToolInstalled("sublist3r"):
            os.system("pipx install sublist3r")

    def __installAssetFinder(self):
        if not self.__isToolInstalled("assetfinder"):
            os.system("go install github.com/tomnomnom/assetfinder@latest")

    def __installChaos(self):
        if not self.__isToolInstalled("chaos"):
            os.system("go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest")

    def __installAmass(self):
        if not self.__isToolInstalled("amass"):
            os.system("go get -u github.com/caffix/amass")

    def __installHttpx(self):
        if not self.__isToolInstalled("httpx"):
            os.system("go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest")

    def __installNaabu(self):
        if not self.__isToolInstalled("naabu"):
            os.system("go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest")

    def __installKatana(self):
        if not self.__isToolInstalled("katana"):
            os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")

    def __installGau(self):
        if not self.__isToolInstalled("gau"):
            os.system("go install github.com/lc/gau/v2/cmd/gau@latest")

    def __installGoSpider(self):
        if not self.__isToolInstalled("gospider"):
            os.system("go install github.com/jaeles-project/gospider@latest")

    def __installWaybackurls(self):
        if not self.__isToolInstalled("waybackurls"):
            os.system("go install github.com/tomnomnom/waybackurls@latest")

    def __installFFUF(self):
        if not self.__isToolInstalled("ffuf"):
            os.system("go install github.com/ffuf/ffuf/v2@latest")

    def __installGowitness(self):
        if not self.__isToolInstalled("gowitness"):
            os.system("go install github.com/sensepost/gowitness@latest")

    def __add_go_bin_to_path(self):
        go_bin = os.path.expandvars(r'%USERPROFILE%\go\bin')
        if General.GetOStype() == "Windows":
            return self.__add_path_to_user_path(go_bin)
        else:
            self.__add_path_to_user_path_linux("~/go/bin")
            # os.system('bash -c "source ~/.bashrc"')
            subprocess.run("source ~/.bashrc", shell=True, executable="/bin/bash")

    def __installPipLibraries(self):
        if General.GetOStype() == "Windows":
            os.system("pipx install dnspython")
        else:
            os.system("pip install dnspython --break-system-packages")

    def Execute(self):
        self.__installScoope()
        self.__installPipx()
        self.__installPipLibraries()
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
        self.__add_go_bin_to_path()
