import re
from typing import Iterable

from notion_to_md.data import INCORRECT_INTERNAL_FILE_URL, INTERNAL_FILE_URL


def format_incorrect_internal_file_url(lines: Iterable[str]) -> set[str]:
    correct_internal_urls = set()

    for line in lines:
        format_line = re.sub(INCORRECT_INTERNAL_FILE_URL, '', line)
        urls = re.findall(INTERNAL_FILE_URL, format_line)
        correct_internal_urls.update(set(urls))

    return correct_internal_urls
