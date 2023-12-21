from pathlib import Path

from notion_to_md.data import FileInfo


def copy_file_by_fileinfo(fileinfo: FileInfo) -> None:
    fullpath = Path(fileinfo.path_to_dir) / Path(fileinfo.heading)
    filepath = Path(f'{fullpath}.md')

    content = '\n'.join(fileinfo.lines[1:])

    with Path.open(filepath, mode='w', encoding='utf-8') as file:
        file.write(content)
