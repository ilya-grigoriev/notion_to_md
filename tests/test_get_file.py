from notion_to_md.data import FileInfo
from notion_to_md.work_with_file.get_ import get_heading


def test_get_heading_correct():
    fileinfo = FileInfo('', '', '', ['# Test'])
    assert get_heading(fileinfo) == 'Test'


def test_get_file_heading_incorrect():
    fileinfo = FileInfo('', '', '', [''])
    get_heading(fileinfo)
