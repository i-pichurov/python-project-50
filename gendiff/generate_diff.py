import json


# Переводим bool-значения в нижний регистр.
def bool_to_lower_str(data: dict):
    for k in data.keys():
        if isinstance(data[k], bool):
            data[k] = str(data[k]).lower()
    return data


def generate_diff(first_file, second_file):

    # Распаковываем json-файлы в словари.
    with open (first_file, 'r') as file1:
        data1 = bool_to_lower_str(json.load(file1))
    with open (second_file, 'r') as file2:
        data2 = bool_to_lower_str(json.load(file2))

    # Формируем строку с результатом.
    result = ["{"]

    merged_dict = {**data1, **data2}

    for key, value in sorted(merged_dict.items()):
        if key not in data1:
            result.append(f'+ {key}: {value}')

        elif key not in data2:
            result.append(f'- {key}: {value}')

        elif data1[key] == data2[key]:
            result.append(f'  {key}: {value}')

        else:
            result.append(f'- {key}: {data1[key]}')
            result.append(f'+ {key}: {data2[key]}')

    result.append("}")
    return "\n".join(result)