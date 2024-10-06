from gendiff.modules.stylish import stylish


def set_format(data, format_name='stylish'):
    if format_name == 'stylish':
        return stylish(data)
