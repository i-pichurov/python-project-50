from gendiff.parser import pars_to_dict
from gendiff.calculate_diff import diff
from gendiff.formatters.set_format import set_format


def generate_diff(first_file, second_file, format_name='stylish'):
    """
    Takes two .json or .yml files and shows their differences.

    Args:
        first_file: path to first file in string format;
        second_file path to second file in string format;
        format_name: a string indicating the format in which
        the result will be output:
            - 'stylish'
            - 'plain'
            - 'json'

    Returns:
        The result of comparing two files in the selected format:
            - 'stylish' - string containing indents and nesting
            - 'plain' - string containing the log of file merging
            - 'json' - internal representation of the difference in JSON format.
    """
    data1 = pars_to_dict(first_file)
    data2 = pars_to_dict(second_file)

    return set_format(diff(data1, data2), format_name)
