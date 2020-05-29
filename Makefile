build:
	python3 setup.py build
inplace:
	python3 setup.py build_ext --inplace
clean:
	rm -rf build *.so
install:
	python3 setup.py install

test:
	python3 tests.py
