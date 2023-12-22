from pathlib import Path

from notion_to_md.data import FileInfo


def copy_file_by_fileinfo(fileinfo: FileInfo) -> None:
    if isinstance(fileinfo, FileInfo):
        fullpath = fileinfo.path_to_dir / fileinfo.heading
        filepath = Path(f'{fullpath}.md')

        content = '\n'.join(fileinfo.lines[1:])

        with Path.open(filepath, mode='w', encoding='utf-8') as file:
            file.write(content)
    else:
        exc_msg = 'Attribute `fileinfo` is not instance of FileInfo.'
        raise TypeError(exc_msg)
