from gendiff import generate_diff
import pytest


@pytest.mark.parametrize(
    "first_file, second_file, format_name, result_fixture",
    [
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'stylish',
            'tests/fixtures/result_stylish.txt'
        ),
        (
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            'stylish',
            'tests/fixtures/result_stylish.txt'
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.yml',
            'stylish',
            'tests/fixtures/result_stylish.txt'
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'plain',
            'tests/fixtures/result_plain.txt'
        ),
        (
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            'plain',
            'tests/fixtures/result_plain.txt'
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.yml',
            'plain',
            'tests/fixtures/result_plain.txt'
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'json',
            'tests/fixtures/result_json.txt'
        ),
        (
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            'json',
            'tests/fixtures/result_json.txt'
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.yml',
            'json',
            'tests/fixtures/result_json.txt'
        ),
    ])
def test_generate_diff(first_file, second_file, format_name, result_fixture):
    with open (result_fixture) as r:
        result = r.read()
    assert generate_diff(first_file, second_file, format_name) == result

    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'spanish')

    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.txt', 'tests/fixtures/file2.txt')
