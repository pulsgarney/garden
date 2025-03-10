build:
	hatch build --clean

check-typing:
	mypy --pretty .

check-python-version:
	@echo "Checking Python versions..."
	vermin --backport asyncio --backport enum --backport typing --eval-annotations --no-parse-comments -v src

check-python-detailed:
	@echo "Checking Python versions..."
	vermin --backport asyncio --backport enum --backport typing --eval-annotations --no-parse-comments -vvvv src
