from pathlib import Path
from typing import Any

import pytest
from hypothesis import given
from hypothesis import strategies as st

from notion_to_md.data import FileInfo
from notion_to_md.work_with_file.copy_ import copy_file_by_fileinfo


@pytest.mark.parametrize(
    'fileinfo',
    [
        FileInfo(
            Path('tests/test_folder/'),
            Path('tests/test_folder/test_file.md'),
            'Test',
            ['#Test', 'hello'],
        ),
    ],
)
def test_copy_file_by_fileinfo_correct(fileinfo: FileInfo) -> None:
    copy_file_by_fileinfo(fileinfo)

    fullpath = Path(fileinfo.path_to_dir) / Path(fileinfo.heading)
    filepath = Path(f'{fullpath}.md')

    Path(filepath).unlink()


@given(st.data())
def test_copy_file_by_fileinfo_incorrect(fileinfo: Any) -> None:
    with pytest.raises(TypeError):
        copy_file_by_fileinfo(fileinfo)
