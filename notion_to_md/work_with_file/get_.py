from __future__ import annotations

import re
from typing import TYPE_CHECKING

from loguru import logger

if TYPE_CHECKING:
    from notion_to_md.data import FileInfo


def get_heading(fileinfo: FileInfo) -> str | None:
    """Get heading from file content.

    Parameters
    ----------
    fileinfo: FileInfo
        Dataclass FileInfo

    Returns
    -------
    str | None
        Path if it there is heading.
    """
    try:
        heading = fileinfo.lines[0]

        matches = re.findall('# (.*)', heading)
        return matches[0]   # get first match, because it is heading
    except Exception:
        if fileinfo.filepath:
            exc_msg = f"File '{fileinfo.filepath}' doesn't have heading."
        else:
            exc_msg = "File doesn't have heading."
        logger.error(exc_msg)
