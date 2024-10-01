from gendiff import generate_diff


# Извлекаем образцовую строку
with open('tests/fixtures/result.txt') as r:
        result = r.read()

# Тестриуем результат функции с образцовой строкой
def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result