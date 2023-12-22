from pathlib import Path

from notion_to_md.data import FileInfo
from notion_to_md.work_with_file.get_ import get_heading


def test_get_heading_correct() -> None:
    fileinfo = FileInfo(Path(), Path(), '', ['# Test'])
    assert get_heading(fileinfo) == 'Test'


def test_get_file_heading_incorrect() -> None:
    fileinfo = FileInfo(Path(), Path(), '', [''])
    get_heading(fileinfo)   # Loguru output that there is error
