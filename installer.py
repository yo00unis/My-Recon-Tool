import os
import shutil
import subprocess

from general import General
from install_go_tools import GoToolsInstaller 

class Installer:
    def __init__(self):
        self.__gotoolsinstaller = GoToolsInstaller()

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

    def __installScoope(self):
        if not self.__isToolInstalled("scoop"):
            os.system('powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"')
            os.system('powershell -Command "iwr -useb get.scoop.sh | iex"')
            scoop_shims = os.path.join(os.path.expanduser("~"), "scoop", "shims")
            self.__add_path_to_user_path(scoop_shims)
        return True

    def __installPipx(self):
        if not self.__isToolInstalled("pipx"):
                os.system('pip install pipx')
                user_bin = os.path.expandvars(r'%USERPROFILE%\.local\bin')
                self.__add_path_to_user_path(user_bin)
        return True

    def __add_go_bin_to_path(self):
        go_bin = os.path.expandvars(r'%USERPROFILE%\go\bin')
        self.__add_path_to_user_path(go_bin)

    def __installPipLibraries(self):
        if not self.__isToolInstalled("dnspython"):
            os.system("pipx install dnspython")

    def Execute(self):
        self.__installScoope()
        self.__installPipx()
        self.__installPipLibraries()
        self.__add_go_bin_to_path()
        self.__gotoolsinstaller.Execute()
