import os
from pathlib import PurePath

class Files:
    
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    def __init__(self):
        pass
    
    @staticmethod
    def WriteToFile(path, mode, line:str):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            f.write(line)
            
    @staticmethod
    def WriteListToFile(path, mode, lines:list):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            for l in lines:
                f.write(l)
    
    @staticmethod
    def GetWorkingDirectory():
        return os.getcwd() 
    
    @staticmethod
    def IsFileExists(path:str):
        return os.path.exists(path) 
    
    @staticmethod
    def CreateFile(path:str):
        with open(f'{path}', 'w') as f:
            pass
    @staticmethod
    def CopyFromTo(src:str, dest:str):
        if Files.IsPathValid(src) == False:
            raise ValueError(f'{src} file path is invalid')
        if Files.IsPathValid(dest) == False:
            raise ValueError(f'{dest} file path is invalid')
        
        if Files.IsFileExists(src) == False:
            raise FileNotFoundError()
        with open(src, 'r') as srcFile, open(dest, 'a') as destFile:
            from general.general import General
            for line in srcFile:
                destFile.write(f"{General.GetStrippedString(line)}\n")
    
    @staticmethod
    def SaveTextToFile(txt:str, file:str):
        if Files.IsPathValid(file) == False:
            raise ValueError(f'{file} file path is invalid')
        
        with open(file, 'a') as srcFile:
            srcFile.write(f"{txt}\n")
    
    @staticmethod
    def SaveListToFile(ls:list, file:str):
        if Files.IsPathValid(file) == False:
            raise ValueError(f'{file} file path is invalid')
        
        with open(file, 'a') as dest:
            for line in ls:
                dest.write(f"{line}\n")
    
    @staticmethod            
    def SaveUniqueListToFile(ls:list, file:str):
        try:
            from general.general import General
            uniqueURLs =  General.GetUniqueURLs(urls=ls)
            Files.SaveListToFile(uniqueURLs, file)
            return True
        except (TypeError, ValueError):
            return False
    
    @staticmethod
    def IsPathValid(path):
        try:
            #Path(path)
            PurePath(path)
            return True
        except (TypeError, ValueError):
            return False
    
    @staticmethod        
    def CreateFolder(path:str):
        from general.general import General
        if not os.path.isdir(General.GetStrippedString(path)):
            os.mkdir(path=General.GetStrippedString(path))
    
    @staticmethod  
    def ValidateDirectoryPath(path):
        from general.general import General
        if Files.IsPathValid(path):
            if Files.IsDirectory(path):
                return True
            General.CreateFolder(path=path)
            return True
        return False

    @staticmethod
    def IsDirectory(path):
        return os.path.isdir(path)