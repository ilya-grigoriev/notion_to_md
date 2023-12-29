from pathlib import Path


def create_new_filepath(filepath: Path) -> Path:
    while True:
        filepath_without_ext = str(filepath).rsplit('.', maxsplit=1)[0]
        new_path = filepath_without_ext + '1' + filepath.suffix

        if Path(new_path).exists() is not True:
            return Path(new_path)

        filepath = Path(new_path)
