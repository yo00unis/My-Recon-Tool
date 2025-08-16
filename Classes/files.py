import os
from pathlib import PurePath
import re

class Files:
    def __init__(self):
        pass

    @staticmethod
    def is_file_empty(path):
        return os.path.getsize(path) == 0

    @staticmethod
    def number_of_lines(path):
        with open(f'{path}', 'r') as file:
            return len(file.readlines())
        return 0

    @staticmethod
    def working_directory():
        return os.getcwd() 

    @staticmethod        
    def create_folder(path:str):
        if not os.path.isdir(path.strip()):
            try:
                os.mkdir(path.strip())
            except Exception as e:
                print("Failed to create folder")


    @staticmethod
    def copy_from_to(src:str, dest:str):
        if not Files.is_path_valid(src) or not Files.is_file_exists(src):
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
    def copy_domains_from_to(src:str, dest:str):
        if Files.is_path_valid(src) == False:
            raise ValueError(f'{src} file path is invalid')
        if Files.is_path_valid(dest) == False:
            raise ValueError(f'{dest} file path is invalid')

        if Files.is_file_exists(src) == False:
            raise FileNotFoundError()
        with open(src, 'r') as srcFile, open(dest, 'a') as destFile:
            for line in srcFile:
                destFile.write(f"{Files.ExtractUrlFromLine(line)}\n")

    @staticmethod
    def is_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def is_path_valid(path):
        try:
            PurePath(path)
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def save_txt_to_file(txt:str, file:str, mode='a'):
        if Files.is_path_valid(file) == False:
            raise ValueError(f'{file} file path is invalid')

        with open(file, mode) as srcFile:
            srcFile.write(f"{txt}\n")

    @staticmethod
    def save_list_to_file(ls:list, file:str):
        if Files.is_path_valid(file) == False:
            raise ValueError(f'{file} file path is invalid')

        with open(file, 'a') as dest:
            for line in ls:
                dest.write(f"{line}\n")

    @staticmethod
    def is_file_exists(path:str):
        return os.path.exists(path) 

    @staticmethod
    def create_file(path:str):
        with open(f'{path}', 'w') as f:
            pass

    @staticmethod
    def write_to_file(path, mode, line:str):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            f.write(f'{line}\n')
        Files.remove_duplicate_from_file(path)
    
    @staticmethod
    def write_to_file_with_duplicates(path, mode, line:str):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            f.write(f'{line}\n')

    @staticmethod
    def extract_url_from_str(line:str):
        match = re.search(
            r"(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", line
        )
        if match:
            url = match.group()
            return url
        else:   
            return None

    @staticmethod
    def extact_urls_from_file(filename:str):
        with open(filename.strip(), encoding="utf-8", errors="ignore") as f:
            urls = re.findall(r'https?://[^\s\[]+', f.read())
        return list(set(urls))

    @staticmethod
    def write_list_to_file(path, mode, lines:list):
        with open(path, mode, encoding="utf-8", errors='ignore') as f:
            for l in lines:
                f.write(f'{l}\n')

    @staticmethod
    def remove_duplicate_from_file(path):
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
