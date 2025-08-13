
import os
import re
import shutil
import subprocess
import zipfile
import requests

from Classes.general import General

###################### ADD TO PATH CLASS ######################
class PathClass:
    def __init__(self):
        pass

    @staticmethod
    def __read_user_path():
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

    @staticmethod
    def add_path_to_user_path_windows(new_path_entry):
        import winreg

        new_path_entry = os.path.normpath(new_path_entry.strip())

        if not os.path.exists(new_path_entry):
            print(f"Warning: The path '{new_path_entry}' does not exist on disk.")
            return False

        current_path = PathClass.__read_user_path()
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

    @staticmethod
    def add_to_path_linux(line):
        bashrc = os.path.expanduser("~/.bashrc")

        with open(bashrc, 'r') as file:
            lines = file.read()

        if line not in lines:
            with open(bashrc, 'a') as file:
                file.write(f"\n{line}\n")
            print(f"\033[32m[+] Added: {line} to ~/.bashrc (permanently)\033[0m")
        else:
            print(f"\033[33m[!] Already exists in ~/.bashrc: {line}\033[0m")

        # Apply it to current session
        os.environ["PATH"] += ":" + line.split(":")[-1].strip().replace('"', '')
        subprocess.run(["bash", "-c", "source ~/.bashrc"], check=False)


###################### GO TOOLS INSTALLER ######################
class GoToolsInstaller:

    def __init__(self):
        self.__local_bin_path_linux = 'export PATH="$HOME/go/bin:$PATH"'
        self.__local_bin_path_windows = os.path.expandvars(r'%USERPROFILE%\\go\bin')
    
    def __add_go_tools_to_path(self):
        if General.GetOStype() == "Windows":
            if not General.is_tool_in_path(self.__local_bin_path_windows):
                PathClass.add_path_to_user_path_windows(self.__local_bin_path_windows)
        else:
            if not General.is_tool_in_path(self.__local_bin_path_linux):
                PathClass.add_to_path_linux(self.__local_bin_path_linux)
    
    
    def __install_go_tool(self, toolname:str, command:str):
         if not General.is_tool_installed(f"{toolname.strip()}"):
            os.system(f"{command.strip()}")
            self.__add_go_tools_to_path()

    def __install_go_language_linux(self):
        
        if General.is_tool_installed("go"):
            print("[+] Go already installed.")
            return

        print("===================================")
        print("[+] Installing latest Go version...")
        print("===================================")

        print("[+] Fetching latest Go version...")

        # Get latest version from go.dev
        r = requests.get("https://go.dev/dl/")
        match = re.search(r'(go[0-9]+\.[0-9]+(?:\.[0-9]+)?\.linux-amd64\.tar\.gz)', r.text)

        if not match:
            print("[-] Could not find the latest Go version.")
            return

        filename = match.group(1)
        version = re.search(r'[0-9]+\.[0-9]+(?:\.[0-9]+)?', filename).group()
        download_url = f"https://go.dev/dl/{filename}"

        print(f"[+] Downloading Go {version}...")
        subprocess.run(["wget", download_url], check=True)

        print("[+] Removing old Go (if any)...")
        subprocess.run(["sudo", "rm", "-rf", "/usr/local/go"], check=True)

        print("[+] Extracting Go...")
        subprocess.run(["sudo", "tar", "-C", "/usr/local", "-xzf", filename], check=True)

        go_path = 'export PATH="/usr/local/go/bin:$PATH"'
        PathClass.add_to_path_linux(go_path)

        go_version = subprocess.run(["go", "version"], capture_output=True, text=True).stdout.strip()
        print(f"[+] Go installed: {go_version}")
    
    def __install_go_language_windows(self):

        if General.is_tool_installed("go"):
            print("[+] Go already installed.")
            return
        
        print("===================================")
        print("[+] Installing latest Go version for Windows...")
        print("===================================")

        # Get latest version
        print("[+] Fetching latest Go version...")
        r = requests.get("https://go.dev/dl/")
        match = re.search(r'(go[0-9]+\.[0-9]+(?:\.[0-9]+)?\.windows-amd64\.zip)', r.text)

        if not match:
            print("[-] Could not find the latest Go version.")
            return

        filename = match.group(1)
        version = re.search(r'[0-9]+\.[0-9]+(?:\.[0-9]+)?', filename).group()
        download_url = f"https://go.dev/dl/{filename}"

        print(f"[+] Downloading Go {version}...")
        subprocess.run(["curl", "-O", download_url], check=True)

        go_dir = "C:\\Go"
        if os.path.exists(go_dir):
            print("[+] Removing old Go (if any)...")
            shutil.rmtree(go_dir)

        print("[+] Extracting Go zip...")
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall("C:\\")

        go_bin_path = "C:\\Go\\bin"
        success = PathClass.add_path_to_user_path_windows(go_bin_path)

        if success:
            print(f"[+] Added Go to user PATH: {go_bin_path}")
        else:
            print(f"[-] Failed to update user PATH. Please add {go_bin_path} manually.")

        try:
            go_version = subprocess.run(["go", "version"], capture_output=True, text=True).stdout.strip()
            print(f"[+] Go installed: {go_version}")
        except Exception as e:
            print("[!] Go installed, but not yet in PATH for this terminal session.")


    def Execute(self):
        if General.GetOStype() == "Windows":
            self.__install_go_language_windows()
        elif General.GetOStype() == "Linux":
            self.__install_go_language_linux()
        self.__install_go_tool("subfinder", "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
        self.__install_go_tool("assetfinder", "go install github.com/tomnomnom/assetfinder@latest")
        self.__install_go_tool("chaos", "go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest")
        self.__install_go_tool("httpx", "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest")
        self.__install_go_tool("naabu", "go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest")
        self.__install_go_tool("katana", "go install github.com/projectdiscovery/katana/cmd/katana@latest")
        self.__install_go_tool("gau", "go install github.com/lc/gau/v2/cmd/gau@latest")
        self.__install_go_tool("gospider", "go install github.com/jaeles-project/gospider@latest")
        self.__install_go_tool("waybackurls", "go install github.com/tomnomnom/waybackurls@latest")
        self.__install_go_tool("ffuf", "go install github.com/ffuf/ffuf/v2@latest")
        self.__install_go_tool("gowitness", "go install github.com/sensepost/gowitness@latest")

###################### WINDOWS INSTALLER ######################
class WindowsInstaller:
    def __init__(self):
        self.__gotoolsinstaller = GoToolsInstaller()

    def __installScoope(self):
        if not General.is_tool_installed("scoop"):
            os.system('powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"')
            os.system('powershell -Command "iwr -useb get.scoop.sh | iex"')
            scoop_shims = os.path.join(os.path.expanduser("~"), "scoop", "shims")
            PathClass.add_path_to_user_path_windows(scoop_shims)
        return True

    def __installPipx(self):
        if not General.is_tool_installed("pipx"):
                os.system('pip install pipx')
                user_bin = os.path.expandvars(r'%USERPROFILE%\.local\bin')
                PathClass.add_path_to_user_path_windows(user_bin)
        return True
    
    def __installSublister(self):
        if not General.is_tool_installed("sublist3r"):
            os.system("pipx install sublist3r")

    def __add_go_bin_to_path(self):
        go_bin = os.path.expandvars(r'%USERPROFILE%\go\bin')
        PathClass.add_path_to_user_path_windows(go_bin)

    def __installPipLibraries(self):
        if not General.is_tool_installed("dnspython"):
            os.system("pipx install dnspython")

    def Execute(self):
        # self.__installScoope()
        self.__installPipx()
        self.__installSublister()
        self.__installPipLibraries()
        self.__add_go_bin_to_path()
        self.__gotoolsinstaller.Execute()

###################### LINUX INSTALLER ######################
class LinuxInstaller:
    def __init__(self):
        self.__gotoolsinstaller = GoToolsInstaller()

    def __run(self, cmd, check=True):
        print(f"[+] Running: {cmd}")
        subprocess.run(cmd, shell=True, check=check)

    def __installPIPX(self):
        try:
            import pip
        except ImportError:
            print("[-] pip not found. Installing pip...")
            self.__run("sudo apt update && sudo apt install -y python3-pip")
        if not General.is_tool_installed("pipx"):
            self.__run("pip install pipx --break-system-packages")
        local_bin_path = 'export PATH="$HOME/.local/bin:$PATH"'
        PathClass.add_to_path_linux(local_bin_path)

        # Ensure pipx adds required path lines
        print("[+] Running: pipx ensurepath")
        self.__run("pipx ensurepath", check=False)

        # Validate pipx is now available
        if not General.is_tool_installed("pipx"):
            print("\033[31m[-] pipx still not in PATH. Try restarting your shell.\033[0m")
        else:
            print("\033[32m[+] pipx installation completed.\033[0m")

    def __installSublister(self):
        if General.is_tool_installed("pipx"):
            if not General.is_tool_installed("sublist3r"):
                os.system("pipx install sublist3r")
        else:
            print("install pipx to install sublist3r")

    def Execute(self):
        self.__installPIPX()
        self.__installSublister()
        self.__gotoolsinstaller.Execute()
