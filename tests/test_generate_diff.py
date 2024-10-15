from gendiff import generate_diff, pars_to_dict
import json
import pytest


# Извлекаем образцовую stylish-строку
with open('tests/fixtures/result_stylish.txt') as r:
    result_stylish = r.read()

# Извлекаем образцовую plain-строку
with open('tests/fixtures/result_plain.txt') as r:
    result_plain = r.read()

# Извлекаем образцовый json
with open('tests/fixtures/result_json.json', 'r') as r:
    result_json = json.load(r)


def test_generate_diff():
    # Тестриуем результат функции с вложенными json/yml -файлами в режиме stylish
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish') == result_stylish
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'stylish') == result_stylish

    # Тестриуем результат функции с вложенными json/yml -файлами в режиме plain
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain') == result_plain
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain') == result_plain

    # Тестриуем результат функции с вложенными json/yml -файлами в режиме json
    assert json.loads(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')) == result_json
    assert json.loads(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')) == result_json

    # Тестируем выпадение ошибки при некорректном format_name
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'spanish')

    # Тестируем выпадение ошибки при некорректном file_format
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.txt', 'tests/fixtures/file2.txt')