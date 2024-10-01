install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

check:
	poetry run flake8 gendiff
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml