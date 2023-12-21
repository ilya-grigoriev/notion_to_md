import pytest

from notion_to_md.work_with_file.check_ import (check_file_exists,
                                                check_file_extension_md)


@pytest.mark.parametrize(
    'path',
    ['tests/test_folder/test_file.md', 'tests/test_folder/test_file_2.md'],
)
def test_checking_file_exists_correct(path: str) -> None:
    assert check_file_exists(path) == True


@pytest.mark.parametrize(
    'path',
    ['not_real_file.md'],
)
def test_checking_file_exists_incorrect(path: str) -> None:
    assert check_file_exists(path) == False


@pytest.mark.parametrize('filepath', ['test.md'])
def test_check_extension_correct(filepath: str) -> None:
    assert check_file_extension_md(filepath) == True


@pytest.mark.parametrize('filepath', ['not_correct_file'])
def test_check_extension_incorrect(filepath: str) -> None:
    assert check_file_extension_md(filepath) == False
