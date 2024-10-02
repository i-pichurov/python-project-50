from gendiff import generate_diff


# Извлекаем образцовую строку
with open('tests/fixtures/result.txt') as r:
        result = r.read()


def test_generate_diff():
    # Тестриуем результат функции с json-файлами и образцовой строкой
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result

    # Тестриуем результат функции с yml-файлами и образцовой строкой
    assert generate_diff('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == result