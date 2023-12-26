import shutil
from pathlib import Path

from notion_to_md.data import FileInfo
from notion_to_md.work_with_file.copy_ import copy_file_by_fileinfo
from notion_to_md.work_with_file.get_ import get_heading
from notion_to_md.work_with_file.read_ import read_file


def process_md(filepath: Path) -> None:
    dirpath = filepath.parent
    lines = tuple(line for line in read_file(filepath) if line)
    fileinfo = FileInfo(dirpath, filepath, '', lines)

    heading = get_heading(fileinfo)

    if heading:
        fileinfo.heading = heading

        copy_file_by_fileinfo(fileinfo)

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
