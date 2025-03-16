# Building package

build:
	@echo "Building Python packages..."
	hatch build --clean

# Building documentations

doc-serve:
	@echo "Serving documentation site locally..."
	cd docs && mkdocs serve && cd ..

doc-deploy:
	@echo "Building documentation site and deploying to GitHub Pages..."
	cd docs && mkdocs gh-deploy && cd ..

# Typing check

check-typing:
	@echo "Checking Python typing..."
	mypy --pretty .

# Python version check

check-python-version:
	@echo "Checking Python versions..."
	vermin --backport asyncio --backport enum --backport typing --eval-annotations --no-parse-comments -v src

check-python-detailed:
	@echo "Checking Python versions..."
	vermin --backport asyncio --backport enum --backport typing --eval-annotations --no-parse-comments -vvvv src

# Running tests

run-tests-units:
	@echo "Running unit tests..."
	pytest -v tests

run-tests-coverage:
	@echo "Running coverage tests..."
	coverage run -m pytest

generate-coverage-report:
	@echo "Generating coverage report..."
	coverage html
