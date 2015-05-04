# This file is part of elementary-test-generator.
# https://github.com/rflorianobr/elementary-test-generator

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Rafael Floriano da Silva <rflorianobr@gmail.com>

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies (do not forget to create a virtualenv first)
setup: setup-python

# install all python dependencies
setup-python:
	@pip install -U -e .\[tests\]

# run your django application
run:
	@python elementary_test_generator/manage.py runserver 0.0.0.0:8000

migrate:
	@python elementary_test_generator/manage.py migrate

makemigrations:
	@python elementary_test_generator/manage.py makemigrations

db: makemigrations migrate

createsuperuser:
	@python elementary_test_generator/manage.py createsuperuser

# test your application (tests in the tests/ directory)
test: unit

unit:
	@coverage run --branch `which nosetests` -vv --with-yanc -s tests/
	@coverage report -m --fail-under=80

# show coverage in html format
coverage-html: unit
	@coverage html

# run tests against all supported python versions
tox:
	@tox

#docs:
	#@cd elementary_test_generator/docs && make html && open _build/html/index.html
