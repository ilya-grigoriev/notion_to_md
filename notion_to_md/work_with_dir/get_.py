from pathlib import Path


def get_dir_by_path(path: str) -> str:
    return str(Path(path).parent)
