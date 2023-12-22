from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass
class FileInfo:
    """Dataclass with file info.

    Attrs:
        path_to_dir: str
        filepath: str
        heading: str
        lines: Sequence[str]
            Content of file with heading inside.
    """

    path_to_dir: Path
    filepath: Path
    heading: str
    lines: Sequence[str]
