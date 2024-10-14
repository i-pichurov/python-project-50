def to_str(value):
    """
    Checks the argument type and returns the required value depending on it.
    """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return value
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def flatten(seq):
    """
    Takes a list of nested lists and returns a flat list that contains
    all the nested values.
    """
    result = []

    def walk(sub_seq):
        for i in sub_seq:
            if isinstance(i, list):
                walk(i)
            else:
                result.append(i)
        return result
    return walk(seq)


def plain(diff):
    """
    Takes a dictionary containing the result of the diff() function
    from the calculate_diff module and produces a string.
    This string is formed taking into account the presence
    of nested data structures.

    Args:
        data: dict containing the result of the diff()

    Returns:
        Sorted string formed taking into account nested structures.
        String looks like the log of file merging.
    """
    def walk(data, ancestry):
        tree = []
        children = data.get('children')

        for elem in children:
            name = elem.get('name')
            type = elem.get('type')
            value = elem.get('value')
            string = to_str(value)
            old_string = to_str(elem.get('old_value'))
            new_string = to_str(elem.get('new_value'))

            if ancestry:
                path = f"{ancestry}.{name}"
            else:
                path = name

            match type:
                case 'added':
                    tree.append(f"Property '{path}' was added with value: "
                                f"{string}")

                case 'removed':
                    tree.append(f"Property '{path}' was removed")

                case 'changed':
                    tree.append(f"Property '{path}' was updated. "
                                f"From {old_string} to {new_string}")

                case 'nested':
                    tree.append(walk(elem, path))

        return flatten(tree)
    return '\n'.join(walk(diff, ''))
