#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import cli


def main():
    """
    Calls the generate_diff() function from gendiff module.
    Args:
        module: gendiff/modules/generate_diff.py
    """
    first_file, second_file, format = cli()
    print(generate_diff(first_file, second_file, format))


if __name__ == '__main__':
    main()
