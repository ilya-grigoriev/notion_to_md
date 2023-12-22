from pathlib import Path

from notion_to_md.work_with_file.process_ import process_img, process_md


def test_process_img() -> None:
    filepath = Path('tests/test_folder/subfolder/pic.jpg')
    dirpath = filepath.parent.parent   # Path of overfolder
    full_path = dirpath / Path('data/') / Path(filepath.name)

    process_img(filepath)

    assert full_path.exists() == True
