# (c) 2012 Ian Dennis Miller
# http://www.iandennismiller.com

SHELL=/bin/bash

clean:
	rm -rf build dist *.egg-info *.pyc

install:
	python setup.py install

docs:
	rm -rf var/sphinx/build
	sphinx-build -b html docs var/sphinx/build

open:
	open var/sphinx/build/index.html

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: clean install docs open release
