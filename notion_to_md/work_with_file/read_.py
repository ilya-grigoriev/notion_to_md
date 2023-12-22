from pathlib import Path
from typing import Any, Generator


def read_file(filepath: Path) -> Generator[str, Any, None]:
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
    if filepath.exists():
        with Path.open(filepath, encoding='utf-8') as file:
            return (line.strip() for line in file.readlines())
    else:
        exc_msg = f"File '{filepath}' doesn't exist."
        raise FileNotFoundError(exc_msg)
