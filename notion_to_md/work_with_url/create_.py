from pathlib import Path


def create_dict_with_path_to_internals_urls(
    path: Path,
    internal_urls: set[str],
) -> dict[str, set[str]]:
    """Create dict with path to internal urls in markdown file.

    Parameters
    ----------
    path : Path
        Path to markdown file.
    internal_urls : set[str]
        Set of internal urls.

    Returns
    -------
    dict[str, set[str]]
        Dict with path to set of internal urls.
    """
    filename = path.name
    return {filename: internal_urls}
