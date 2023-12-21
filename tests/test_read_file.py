import pytest

from notion_to_md.work_with_file.read_ import read_file


@pytest.mark.parametrize(
    'path',
    ['tests/test_folder/test_file.md'],
)
def test_read_file_correct(path):
    assert tuple(read_file(path)) == ('# Test', 'hello')


@pytest.mark.parametrize(
    'path',
    ['file_doesnt_exist'],
)
def test_read_file_incorrect(path):
    with pytest.raises(FileNotFoundError):
        read_file(path)
