from notion_to_md.work_with_file import copy_, get_, read_


class File:
    copy = staticmethod(copy_.copy_file_by_fileinfo)
    get_heading = staticmethod(get_.get_heading)
    read = staticmethod(read_.read_file)
