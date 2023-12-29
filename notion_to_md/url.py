from notion_to_md.work_with_url.create_ import \
    create_dict_with_path_to_internals_urls
from notion_to_md.work_with_url.format_ import \
    format_incorrect_internal_file_url
from notion_to_md.work_with_url.process_ import process_urls


class Url:
    format_ = staticmethod(format_incorrect_internal_file_url)
    create_dict = staticmethod(create_dict_with_path_to_internals_urls)
    process = staticmethod(process_urls)
