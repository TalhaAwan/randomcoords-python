SRC = randomcoords tests

test:
	pytest

typecheck:
	mypy

format:
	ruff format $(SRC)

check-format:
	ruff format --check $(SRC)

validate: check-format typecheck test