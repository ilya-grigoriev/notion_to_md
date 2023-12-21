from dataclasses import dataclass
from typing import Sequence


@dataclass
class FileInfo:
    path_to_dir: str
    filepath: str
    heading: str
    lines: Sequence[str]
