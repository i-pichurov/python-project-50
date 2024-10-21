from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import to_json


def set_formatter(format_name='stylish'):
    """
    Based on the value of "format_name",
    returns the formatter function corresponding to it.

    Args:
        format_name: a string containing the name
        of the formatter whose function will be returned:
            - 'stylish'
            - 'plain'
            - 'json'

    Returns:
            - 'stylish' - stylish function
            - 'plain' - plain function
            - 'json' - json function

    """
    match format_name:
        case 'stylish':
            return stylish
        case 'plain':
            return plain
        case 'json':
            return to_json
        case _:
            raise Exception('The format name is invalid.')
