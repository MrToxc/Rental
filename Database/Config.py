from pathlib import Path

def find_root():
    return Path(find_config()).resolve().parent

def find_config():
    current_path = Path(__file__).resolve().parent

    for parent in [current_path] + list(current_path.parents):
        config_path = parent / "rental_config.json"
        if config_path.exists():
            return config_path

    raise FileNotFoundError("Could not find config.json in any parent directory.")

def find_file(file_path: str):
    return find_root() / file_path