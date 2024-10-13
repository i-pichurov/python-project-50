from gendiff.modules.formatter.stylish import stylish
from gendiff.modules.formatter.plain import plain
from gendiff.modules.formatter.json import to_json


def set_format(data, format_name='stylish'):
    match format_name:
        case 'stylish':
            return stylish(data)
        case 'plain':
            return plain(data)
        case 'json':
            return to_json(data)
