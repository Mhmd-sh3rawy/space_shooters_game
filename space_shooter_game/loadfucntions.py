import os

working_folder = "space_shooter_game"

def path_load(path:str) -> str:
    try:
        return f"{os.getcwd()}\{working_folder}\{path}"
    except FileNotFoundError:
        return f"{os.getcwd()}/{working_folder}/{path}"