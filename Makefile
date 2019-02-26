FILE=VERSION
VERSION=`cat $(FILE)`

.PHONY: package release

package: 
	python setup.py sdist bdist_wheel

release: package
	twine upload dist/isdc-userstatistics-$(VERSION).tar.gz