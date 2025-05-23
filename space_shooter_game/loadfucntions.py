import os

working_folder = "space_shooter_game"

def path_load(path:str) -> str:
    try:
        return f"{path}"                                             # for windows users
    except FileNotFoundError:
        return f"{os.getcwd()}/{working_folder}/{path}"                            # for linux users