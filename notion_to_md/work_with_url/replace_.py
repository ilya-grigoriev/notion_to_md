from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from notion_to_md.folder import Folder


def replace_urls(folder_instance: 'Folder') -> None:
    """Replace incorrect urls in content of markdown file.

    Parameters
    ----------
    fileinfo : FileInfo

    """

