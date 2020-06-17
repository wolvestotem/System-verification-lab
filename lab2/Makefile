all: lab2.out

install:
	pip3 install gcovr numpy

lab2.out: lab2.cpp Matrix.h Matrix.cpp
	g++ lab2.cpp Matrix.cpp -lstdc++ -o lab2.out

test: unittest.cpp Matrix.h Matrix.cpp
	g++ -fprofile-arcs -ftest-coverage -fPIC -O0 unittest.cpp Matrix.h Matrix.cpp -o test.out
	./test.out || echo ''
	python3 coverage.py -r . -f Matrix.cpp --html-details -o coverage.html
	python3 coverage.py -r . -f Matrix.cpp

test-tdd:
	python3 lab2_test.py test-tdd

test-cpp:
	python3 lab2_test.py test-cpp

serve:
	python3 -m http.server

clean:
	rm -rf lab2.out

