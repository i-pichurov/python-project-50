import json
import yaml
from yaml.loader import SafeLoader


# Парсим yml/json в словарь.
def pars_to_dict(file):
    with open(file, 'r') as file1:
        if file.endswith('.json'):
            data = json.load(file1)
        elif file.endswith(('.yml', '.yaml')):
            data = yaml.load(file1, Loader=SafeLoader)
        else:
            raise Exception('Задан неверный тип файла!')
    return data
