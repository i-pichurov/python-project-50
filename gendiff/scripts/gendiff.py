#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument(
    'first_file', type=str,
    help='Input first file for comparison')
parser.add_argument(
    'second_file', type=str,
    help='Input second file for comparison')
parser.add_argument('-f', '--format', type=str,
                    default='stylish', help='set format of output')
args = parser.parse_args()


def main():
    """
    Calls the generate_diff() function from gendiff module.
    Args:
        module: gendiff/modules/generate_diff.py
    """
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
