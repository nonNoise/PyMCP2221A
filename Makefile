
init:
	mkdir -p build dist

build-arm:
	cp LICENSE README.rst pypi/armv7l/
	cp PyMCP2221A/* pypi/armv7l/PyMCP2221A
	cd pypi/armv7l && python3 setup.py bdist_wheel

build-x86_64:
	cp LICENSE README.rst pypi/main/
	cp PyMCP2221A/* pypi/main/PyMCP2221A
	cd pypi/main && python3 setup.py bdist_wheel

clean:
	rm -r pypi/*/build/*
	rm -r pypi/*/dist/*
	rm -r pypi/*/*.egg-info
