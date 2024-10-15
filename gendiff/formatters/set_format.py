from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import to_json


def set_format(data, format_name='stylish'):
    """
    Depending on the value of 'format_name',
    returns information from 'data' in the desired format.

    Args:
        data: dict - internal representation of the difference
        format_name: a string indicating the format in which
        the result will be output:
            - 'stylish'
            - 'plain'
            - 'json'

    Returns:
            - 'stylish' - string containing indents and nesting
            - 'plain' - string containing the log of file merging
            - 'json' - internal representation of the difference in JSON format.

    """
    match format_name:
        case 'stylish':
            return stylish(data)
        case 'plain':
            return plain(data)
        case 'json':
            return to_json(data)
        case _:
            raise Exception('The format name is invalid.')
