PACKAGE_DIRECTORY := .
CACHE_DIRECTORY := .cache

# Clean the cache directory
.PHONY: clean
clean:
	rm --force --recursive "${CACHE_DIRECTORY}"
	rm --force --recursive `find . -type d -name __pycache__`

# Linting commands
.PHONY: lint
lint:
	@hatch run mypy ${PACKAGE_DIRECTORY}
	@hatch run ruff check ${PACKAGE_DIRECTORY}
	@hatch run ruff format --check ${PACKAGE_DIRECTORY}

.PHONY: format
format:
	@hatch run ruff format ${PACKAGE_DIRECTORY}
	@hatch run ruff check --fix ${PACKAGE_DIRECTORY}

# Dependency commands
.PHONY: install
install:
	hatch env create
	hatch env shell
	hatch run pip install .

# Development commands
.PHONY: dev
dev:
	hatch env create
	hatch env shell
	hatch run pip install .
	hatch run pip install .[dev]
	hatch run pip install .[tests]

# Testing commands
.PHONY: test
test:
	@hatch run pytest

# Run the application
.PHONY: run
run:
	@hatch run uvicorn app.main:app --reload
