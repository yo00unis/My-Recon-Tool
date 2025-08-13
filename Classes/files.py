import os
from pathlib import PurePath
import re
import shutil

class Files:
    def __init__(self):
        pass

    @staticmethod
    def IsFileEmpty(path):
        return os.path.getsize(path) == 0

    @staticmethod
    def GetNumberOfLines(path):
        with open(f'{path}', 'r') as file:
            return len(file.readlines())
        return 0

    @staticmethod
    def GetWorkingDirectory():
        return os.getcwd() 

    @staticmethod        
    def CreateFolder(path:str):
        from Classes.general import General
        if not os.path.isdir(path.strip()):
            try:
                os.mkdir(path.strip())
            except Exception as e:
                print("Failed to create folder")


    @staticmethod
    def CopyFromTo(src:str, dest:str):
        if not Files.IsPathValid(src) or not Files.IsFileExists(src):
            raise FileNotFoundError(f"Source file not found or invalid: {src}")

        # Ensure destination directory exists
        dest_dir = os.path.dirname(dest)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        with open(src, 'r', encoding='utf-8') as fsrc:
            content = fsrc.read()

        with open(dest, 'a', encoding='utf-8') as fdest:
            fdest.write(content)

    @staticmethod
    def CopyDomainsFromTo(src:str, dest:str):
        if Files.IsPathValid(src) == False:
            raise ValueError(f'{src} file path is invalid')
        if Files.IsPathValid(dest) == False:
            raise ValueError(f'{dest} file path is invalid')

        if Files.IsFileExists(src) == False:
            raise FileNotFoundError()
        with open(src, 'r') as srcFile, open(dest, 'a') as destFile:
            for line in srcFile:
                destFile.write(f"{Files.ExtractUrlFromLine(line)}\n")

    @staticmethod  
    def ValidateDirectoryPath(path):
        from Classes.general import General
        if Files.IsPathValid(path):
            if Files.IsDirectory(path):
                return True
            General.CreateFolder(path=path)
            return True
        return False

    @staticmethod
    def IsDirectory(path):
        return os.path.isdir(path)

    @staticmethod            
    def SaveUniqueListToFile(ls:list, file:str):
        try:
            from Classes.general import General
            uniqueURLs =  General.GetUniqueURLs(urls=ls)
            Files.SaveListToFile(uniqueURLs, file)
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def IsPathValid(path):
        try:
            PurePath(path)
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def SaveTextToFile(txt:str, file:str, mode='a'):
        if Files.IsPathValid(file) == False:
            raise ValueError(f'{file} file path is invalid')

        with open(file, mode) as srcFile:
            srcFile.write(f"{txt}\n")

    @staticmethod
    def SaveListToFile(ls:list, file:str):
        if Files.IsPathValid(file) == False:
            raise ValueError(f'{file} file path is invalid')

        with open(file, 'a') as dest:
            for line in ls:
                dest.write(f"{line}\n")

    @staticmethod
    def IsFileExists(path:str):
        return os.path.exists(path) 

    @staticmethod
    def CreateFile(path:str):
        with open(f'{path}', 'w') as f:
            pass

    @staticmethod
    def WriteToFile(path, mode, line:str):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            f.write(f'{line}\n')
        Files.RemoveDuplicateFromFile(path)

    @staticmethod
    def WriteToPortScanningTargetFile():
        from Classes.globalEnv import GlobalEnv
        from Classes.general import General
        with open(GlobalEnv.GetHttpx(), 'r', encoding="utf-8", errors='ignore') as f:
            for line in f:
                domain = Files.ExtractUrlFromLine(line)
                if domain != None:
                    ip = General.getIPfromDomain(domain)
                    if ip != None:
                        print(f'{ip.strip()} -> {domain.strip()}')
                        Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'a', ip)
                        Files.WriteToFile(GlobalEnv.GetPortScanningTargetDomains(), 'a', domain)  

    @staticmethod
    def ExtractUrlFromLine(line:str):
        match = re.search(
            r"(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", line
        )
        if match:
            url = match.group()
            return url
        else:   
            return None

    @staticmethod
    def ExtractUrlsFromFile(filename:str):
        with open(filename.strip(), encoding="utf-8", errors="ignore") as f:
            urls = re.findall(r'https?://[^\s\[]+', f.read())
        return list(set(urls))

    @staticmethod
    def WriteListToFile(path, mode, lines:list):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            for l in lines:
                f.write(f'{l}\n')

    @staticmethod
    def RemoveDuplicateFromFile(path):
        try:
            seen = set()
            unique_lines = []

            with open(path, 'r') as infile:
                for line in infile:
                    if line not in seen:
                        seen.add(line)
                        unique_lines.append(line)

            with open(path, 'w') as outfile:
                outfile.writelines(unique_lines)
        except(FileNotFoundError):
            pass
