import os

def path_load(path: str) -> str:
    working_folder = "space_shooter_game"
    if os.path.exists(path):
        return path
    full_path = os.path.join(working_folder, path)
    if os.path.exists(full_path):
        return full_path
    raise FileNotFoundError(f"File not found in '{path}' or '{full_path}'")