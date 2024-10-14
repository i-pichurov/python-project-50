def added(key, value):
    """
    Creates a node of type 'added'.
    """
    return {
        'name': key,
        'type': 'added',
        'value': value
    }


def removed(key, value):
    """
    Creates a node of type 'removed'.
    """
    return {
        'name': key,
        'type': 'removed',
        'value': value
    }


def unchanged(key, value):
    """
    Creates a node of type 'unchanged'.
    """
    return {
        'name': key,
        'type': 'unchanged',
        'value': value
    }


def changed(key, value1, value2):
    """
    Creates a node of type 'changed'.
    """
    return {
        'name': key,
        'type': 'changed',
        'old_value': value1,
        'new_value': value2
    }


def nested(key, value1, value2):
    """
    Creates a node of type 'nested'.
    """
    return {
        'name': key,
        'type': 'nested',
        'children': calculate_diff(value1, value2)
    }


def make_root(data):
    """
    Creates a root node.
    """
    return {
        'name': 'main',
        'type': 'root',
        'children': data
    }


def calculate_diff(data1, data2):
    """
    Computes the differences between two files and
    produces a dictionary containing an internal representation
    of their differences.

    Args:
        data1: dict
        data: dict

    Returns:
        dict containing an internal representation of their differences
    """

    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()
    union_keys = data1.keys() | data2.keys()

    result = []

    for key in sorted(union_keys):
        if key in added_keys:
            result.append(added(key, data2[key]))
        elif key in removed_keys:
            result.append(removed(key, data1[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append(nested(key, data1[key], data2[key]))
        elif data1[key] != data2[key]:
            result.append(changed(key, data1[key], data2[key]))
        else:
            result.append(unchanged(key, data1[key]))
    return result


def diff(data1, data2):
    """
    Wraps the result of the calculate_diff() function in the 'root' node.
    """
    return make_root(calculate_diff(data1, data2))
