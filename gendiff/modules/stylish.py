NEW = '+ '
OLD = '- '
EMPTY = '  '
SEPARATOR = ' '


def stylish(data, depth=2):
    space = depth * SEPARATOR
    tree = []
    children = data.get('children')

    for elem in children:
        name = elem.get('name')
        type = elem.get('type')
        value = elem.get('value')
        string = to_str(value, depth)
        old_string = to_str(elem.get('old_value'), depth)
        new_string = to_str(elem.get('new_value'), depth)

        if type == 'added':
            tree.append(f"{space}{NEW}{name}: {string}")
        elif type == 'removed':
            tree.append(f"{space}{OLD}{name}: {string}")
        elif type == 'unchanged':
            tree.append(f"{space}{EMPTY}{name}: {string}")
        elif type == 'changed':
            tree.append(f"{space}{OLD}{name}: {old_string}")
            tree.append(f"{space}{NEW}{name}: {new_string}")
        else:
            tree.append(f"{space}{EMPTY}{name}: {stylish(elem, depth + 4)}")
    format = "\n".join(tree)
    end_space = (depth - 2) * SEPARATOR
    return f"{{\n{format}\n{end_space}}}"


def to_str(data, depth=4):
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    if isinstance(data, int):
        return data
    elif isinstance(data, dict):
        space = (depth + 4) * SEPARATOR
        tree = []

        for key, value in data.items():
            tree.append(f"{space}{EMPTY}{key}: {to_str(value, depth + 4)}")
        format = "\n".join(tree)
        end_space = (depth + 2) * SEPARATOR
        return f"{{\n{format}\n{end_space}}}"

    else:
        return f"{data}"
