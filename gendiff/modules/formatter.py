from gendiff.modules.formats.stylish import stylish
from gendiff.modules.formats.plain import plain
from gendiff.modules.formats.json import to_json


def set_format(data, format_name='stylish'):
    match format_name:
        case 'stylish':
            return stylish(data)
        case 'plain':
            return plain(data)
        case 'json':
            return to_json(data)
