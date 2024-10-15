import json
import yaml
from yaml.loader import SafeLoader


# Парсим yml/json в словарь.
def pars_to_dict(file):
    """
    Takes a json or yml file and parses it into a Python object.

    Args:
        - file: path to file in string format.

    Returns:
        A Python object containing information from the original file.
    """
    with open(file, 'r') as file1:
        if file.endswith('.json'):
            data = json.load(file1)
        elif file.endswith(('.yml', '.yaml')):
            data = yaml.load(file1, Loader=SafeLoader)
        else:
            raise Exception('The file type is invalid.')
    return data
