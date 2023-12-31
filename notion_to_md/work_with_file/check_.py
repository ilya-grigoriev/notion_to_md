from pathlib import Path


def check_file_content(filepath: Path, content: str) -> bool:
    real_file_content = filepath.read_text(encoding='utf-8')
    return real_file_content == content
