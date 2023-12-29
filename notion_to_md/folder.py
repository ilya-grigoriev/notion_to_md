from pathlib import Path

from notion_to_md.file import File
from notion_to_md.url import Url


class Folder:
    def __init__(self) -> None:
        self.paths_to_urls = {}
        self.incorrect_to_correct_names = {}

    def process(self, dirpath: Path) -> None:
        """Process paths in folder path.

        Parameters
        ----------
        dirpath : Path
            Path of folder.
        """
        for path in dirpath.iterdir():
            if path.suffix == '.md':
                fileinfo = File.process_md(path)
                Url.process(fileinfo, self)
            elif path.suffix in ('.jpg', '.png'):
                File.process_img(path)
            elif path.is_dir():
                self.process(path)
