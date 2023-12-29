from typing import TYPE_CHECKING

from notion_to_md.data import FileInfo
from notion_to_md.work_with_url.create_ import \
    create_dict_with_path_to_internals_urls
from notion_to_md.work_with_url.format_ import \
    format_incorrect_internal_file_url

if TYPE_CHECKING:
    from notion_to_md.folder import Folder


def process_urls(fileinfo: FileInfo, folder_instance: 'Folder') -> None:
    format_urls = format_incorrect_internal_file_url(fileinfo.lines)

    if format_urls:
        path_to_internal_urls = create_dict_with_path_to_internals_urls(
            fileinfo.filepath,
            format_urls,
        )
        folder_instance.paths_to_urls.update(path_to_internal_urls)

    folder_instance.incorrect_to_correct_names[
        fileinfo.old_path
    ] = fileinfo.filepath
