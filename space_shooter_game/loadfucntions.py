import os

def path_load(path: str) -> str:
    """
    Loads file paths with fallback logic for different directory structures.
    
    First checks if the path exists as-is, then checks within the working folder.
    Useful for handling both development and deployed environments.
    
    Args:
        path: Relative file path to load
        
    Returns:
        str: Full path to the existing file
        
    Raises:
        FileNotFoundError: If file is not found in either location
    """

    working_folder = "space_shooter_game"

    # Try the path as-is first
    if os.path.exists(path):
        return path

    # Try within the working folder
    full_path = os.path.join(working_folder, path)
    if os.path.exists(full_path):
        return full_path

    raise FileNotFoundError(f"File not found in '{path}' or '{full_path}'")