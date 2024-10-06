from gendiff.modules.parser import pars_to_dict
from gendiff.modules.generate_diff_2 import gen_diff
from gendiff.modules.root import make_root
from gendiff.modules.set_format import set_format


def engine(first_file, second_file, format_name='stylish'):
    data1 = pars_to_dict(first_file)
    data2 = pars_to_dict(second_file)

    return set_format(make_root(gen_diff(data1, data2)), format_name)
