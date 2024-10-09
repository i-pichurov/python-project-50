def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def flatten(seq):
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
