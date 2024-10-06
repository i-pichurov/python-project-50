from gendiff import engine


# Извлекаем плоскую образцовую строку
with open('tests/fixtures/result.txt') as r:
        result = r.read()

# Извлекаем многоуровневую образцовую строку
with open('tests/fixtures/result_rec.txt') as r:
        result_rec = r.read()


def test_engine():
    # Тестриуем результат функции с json-файлами и образцовой строкой
    assert engine('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result

    # Тестриуем результат функции с yml-файлами и образцовой строкой
    assert engine('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == result

    # Тестриуем результат функции с json-файлами и образцовой строкой
    assert engine('tests/fixtures/file1_rec.json', 'tests/fixtures/file2_rec.json') == result_rec

    # Тестриуем результат функции с yml-файлами и образцовой строкой
    assert engine('tests/fixtures/file1_rec.yml', 'tests/fixtures/file2_rec.yml') == result_rec
