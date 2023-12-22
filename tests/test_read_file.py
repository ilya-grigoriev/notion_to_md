from pathlib import Path

import pytest

from notion_to_md.work_with_file.read_ import read_file


@pytest.mark.parametrize(
    'path',
    [Path('tests/test_folder/test_file.md')],
)
def test_read_file_correct(path: Path) -> None:
    assert tuple(read_file(path)) == ('# Test', 'hello')


@pytest.mark.parametrize(
    'path',
    [Path('file_doesnt_exist')],
)
def test_read_file_incorrect(path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        read_file(path)
