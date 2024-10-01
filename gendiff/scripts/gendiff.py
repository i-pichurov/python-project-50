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
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


def main():
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
