
import os
from pathlib import PurePath



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
        from general import General
        if not os.path.isdir(General.GetStrippedString(path)):
            os.mkdir(path=General.GetStrippedString(path))
    
    @staticmethod
    def CopyFromTo(src:str, dest:str):
        from general import General
        if Files.IsPathValid(src) == False:
            raise ValueError(f'{src} file path is invalid')
        if Files.IsPathValid(dest) == False:
            raise ValueError(f'{dest} file path is invalid')
        
        if Files.IsFileExists(src) == False:
            raise FileNotFoundError()
        with open(src, 'r') as srcFile, open(dest, 'a') as destFile:
            for line in srcFile:
                destFile.write(f"{General.GetStrippedString(line)}\n")
    
    @staticmethod  
    def ValidateDirectoryPath(path):
        from general import General
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
            from general import General
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
            
    @staticmethod
    def WriteListToFile(path, mode, lines:list):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            for l in lines:
                f.write(f'{l}\n')
    
    @staticmethod
    def RemoveDuplicateFromDile(path):
        seen = set()
        unique_lines = []

        with open(path, 'r') as infile:
            for line in infile:
                if line not in seen:
                    seen.add(line)
                    unique_lines.append(line)

        with open(path, 'w') as outfile:
            outfile.writelines(unique_lines)