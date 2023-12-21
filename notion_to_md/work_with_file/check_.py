from pathlib import Path


def check_file_exists(filepath: str) -> bool:
    return Path.is_file(Path(filepath))


def check_file_extension_md(filepath: str) -> bool:
    """Check that file extension is markdown.

    Parameters
    ----------
    filepath : str
        Path to file.

    Returns
    -------
    bool
        Return `True` if extension is markdown.
    """
    EXTENSION = -2
    return filepath.strip()[EXTENSION:] == 'md'
