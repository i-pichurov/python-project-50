import json
import yaml
from yaml.loader import SafeLoader


# Переводим bool-значения в нижний регистр.
def bool_to_lower_str(data: dict):
    for k in data.keys():
        if isinstance(data[k], bool):
            data[k] = str(data[k]).lower()
    return data


# Парсим yml/json в словарь.
def pars_to_dict(file):
    with open(file, 'r') as file1:
        if file.endswith('.json'):
            data = bool_to_lower_str(json.load(file1))
        elif file.endswith(('.yml', '.yaml')):
            data = bool_to_lower_str(yaml.load(file1, Loader=SafeLoader))
        else:
            raise Exception('Задан неверный тип файла!')
    return data
