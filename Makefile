install:
	poetry install

gen_diff:
	poetry run gendiff gendiff/file1.json gendiff/file1.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff