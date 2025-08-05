
import os
import subprocess
import requests
import re
from install_go_tools import GoToolsInstaller

class LinuxInstaller:
    def __init__(self):
        self.__gotoolsinstaller = GoToolsInstaller()
    
    def __add_to_path(self, line):
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


    def __is_tool_installed(self, toolname:str):
        if subprocess.run(["which", f"{toolname}"], capture_output=True).returncode == 0:
            return True
        return False

    def __install_go_language(self):
        if self.__is_tool_installed("go"):
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
        self.__add_to_path(go_path)

        go_version = subprocess.run(["go", "version"], capture_output=True, text=True).stdout.strip()
        print(f"[+] Go installed: {go_version}")

    def __run(self, cmd, check=True):
        print(f"[+] Running: {cmd}")
        subprocess.run(cmd, shell=True, check=check)

    def __installPIPX(self):
        try:
            import pip
        except ImportError:
            print("[-] pip not found. Installing pip...")
            self.__run("sudo apt update && sudo apt install -y python3-pip")
        if not self.__is_tool_installed("pipx"):
            self.__run("pip install pipx --break-system-packages")
        local_bin_path = 'export PATH="$HOME/.local/bin:$PATH"'
        self.__add_to_path(local_bin_path)

        # Ensure pipx adds required path lines
        print("[+] Running: pipx ensurepath")
        self.__run("pipx ensurepath", check=False)

        # Validate pipx is now available
        if not self.__is_tool_installed("pipx"):
            print("\033[31m[-] pipx still not in PATH. Try restarting your shell.\033[0m")
        else:
            print("\033[32m[+] pipx installation completed.\033[0m")


    def Execute(self):
        self.__install_go_language()
        self.__installPIPX()
