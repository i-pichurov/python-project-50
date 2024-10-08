from gendiff import engine


# Извлекаем плоскую образцовую строку
with open('tests/fixtures/result.txt') as r:
        result = r.read()

# Извлекаем многоуровневую образцовую stylish-строку
with open('tests/fixtures/result_stylish.txt') as r:
        result_stylish = r.read()

# Извлекаем многоуровневую образцовую stylish-строку
with open('tests/fixtures/result_plain.txt') as r:
        result_plain = r.read()

def test_engine():
    # Тестриуем результат функции с плоскими json/yml -файлами
    assert engine('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result
    assert engine('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == result

    # Тестриуем результат функции с вложенными json/yml -файлами в режиме stylish
    assert engine('tests/fixtures/file1_rec.json', 'tests/fixtures/file2_rec.json', 'stylish') == result_stylish
    assert engine('tests/fixtures/file1_rec.yml', 'tests/fixtures/file2_rec.yml', 'stylish') == result_stylish

    # Тестриуем результат функции с вложенными json/yml -файлами в режиме plain
    assert engine('tests/fixtures/file1_rec.json', 'tests/fixtures/file2_rec.json', 'plain') == result_plain
    assert engine('tests/fixtures/file1_rec.json', 'tests/fixtures/file2_rec.json', 'plain') == result_plain

