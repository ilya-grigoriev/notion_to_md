from pathlib import Path

from notion_to_md.data import FileInfo
from notion_to_md.file import File


def process_filepath(filepath: Path) -> None:
    dirpath = filepath.parent
    lines = tuple(line for line in File.read(filepath) if line)
    fileinfo = FileInfo(dirpath, filepath, '', lines)

    heading = File.get_heading(fileinfo)

    if heading:
        fileinfo.heading = heading

        File.copy(fileinfo)

        filepath.unlink()
