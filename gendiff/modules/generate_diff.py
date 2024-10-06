from gendiff.modules.parser import pars_to_dict


def generate_diff(first_file, second_file):

    data1 = pars_to_dict(first_file)
    data2 = pars_to_dict(second_file)
    merged_dict = {**data1, **data2}

    result = ["{"]

    for key, value in sorted(merged_dict.items()):
        if key not in data1:
            result.append(f'  + {key}: {value}')

        elif key not in data2:
            result.append(f'  - {key}: {value}')

        elif data1[key] == data2[key]:
            result.append(f'    {key}: {value}')

        else:
            result.append(f'  - {key}: {data1[key]}')
            result.append(f'  + {key}: {data2[key]}')

    result.append("}")
    return "\n".join(result)
