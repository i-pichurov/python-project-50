from gendiff.modules.formatter.stylish import stylish
from gendiff.modules.formatter.plain import plain


def set_format(data, format_name='stylish'):
    if format_name == 'stylish':
        return stylish(data)
    elif format_name == 'plain':
        return plain(data)
