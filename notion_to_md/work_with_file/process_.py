import shutil
from pathlib import Path

from notion_to_md.data import FileInfo
from notion_to_md.file import File


def process_md(filepath: Path) -> None:
    dirpath = filepath.parent
    lines = tuple(line for line in File.read(filepath) if line)
    fileinfo = FileInfo(dirpath, filepath, '', lines)

    heading = File.get_heading(fileinfo)

    if heading:
        fileinfo.heading = heading

        File.copy(fileinfo)

        filepath.unlink()


def process_img(filepath: Path) -> None:
    dirpath = filepath.parent.parent   # Path of overfolder
    data_path = dirpath / Path('data')
    full_path = data_path / filepath.name

    if data_path.exists() is not True:
        Path(data_path).mkdir()

    if full_path.exists() is not True:
        shutil.copy(filepath, data_path)
    else:
        filepath_without_ext = str(filepath).rsplit('.', maxsplit=1)[0]
        new_path = filepath_without_ext + '1' + filepath.suffix

        filepath.rename(new_path)
        process_img(Path(new_path))
