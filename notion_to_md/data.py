from dataclasses import dataclass
from typing import Sequence


@dataclass
class FileInfo:
    """
    Attrs:
        lines: Sequence[str]
            Content of file with title inside.
    """

    path_to_dir: str
    filepath: str
    heading: str
    lines: Sequence[str]
