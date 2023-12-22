from argparse import ArgumentParser, Namespace, RawTextHelpFormatter


def parse_args() -> Namespace:
    """Parse args from command line.

    Returns
    -------
    Namespace
        Object with args and their values.
    """
    parser = ArgumentParser(
        'notion_to_md',
        formatter_class=RawTextHelpFormatter,
    )
    set_setttings_parser(parser)

    return parser.parse_args()


def set_setttings_parser(parser: ArgumentParser) -> None:
    help_msg = 'Enter path to the folder that it will be used for converting notion to markdown.\nBy example, `./converting_notion_to_md -p tests/folder`'

    parser.add_argument(
        '-p',
        '--path',
        default='',
        help=help_msg,
        required=True,
        type=str,
    )


if __name__ == '__main__':
    parse_args()
