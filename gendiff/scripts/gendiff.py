#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str, help='Input first file for comparison')
parser.add_argument('second_file', type=str, help='Input second file for comparison')
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()