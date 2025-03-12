build:
	@echo "Building Python packages..."
	hatch build --clean

doc-serve:
	@echo "Serving documentation site locally..."
	cd docs && mkdocs serve && cd ..

doc-deploy:
	@echo "Building documentation site and deploying to GitHub Pages..."
	cd docs && mkdocs gh-deploy && cd ..

check-typing:
	@echo "Checking Python typing..."
	mypy --pretty .

check-python-version:
	@echo "Checking Python versions..."
	vermin --backport asyncio --backport enum --backport typing --eval-annotations --no-parse-comments -v src

check-python-detailed:
	@echo "Checking Python versions..."
	vermin --backport asyncio --backport enum --backport typing --eval-annotations --no-parse-comments -vvvv src
