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

    if data_path.exists() is not True:
        Path(data_path).mkdir()

    shutil.copy(filepath, data_path)
