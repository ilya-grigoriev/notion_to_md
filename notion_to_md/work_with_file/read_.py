from pathlib import Path
from typing import Any, Generator

from notion_to_md.work_with_file.check_ import check_file_exists


def read_file(filepath: str) -> Generator[str, Any, None]:
    """Read file by filepath.

    Parameters
    ----------
    filepath : str
        Path to file.

    Returns
    -------
    Generator[str, Any, None]
        Generator with lines of file.
    """
    if check_file_exists(filepath):
        with Path.open(Path(filepath), encoding='utf-8') as file:
            return (line.strip() for line in file.readlines())
    else:
        exc_msg = f"File '{filepath}' doesn't exist."
        raise FileNotFoundError(exc_msg)
