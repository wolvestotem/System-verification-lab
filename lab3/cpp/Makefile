all: lab3a lab3b

install:
	pip3 install networkx numpy matplotlib

lab3a: lab3a.cpp Tensors.h Tensors.cpp
	g++ lab3a.cpp Tensors.cpp -Wall -Wextra -lstdc++ -std=c++17 -o lab3a.out

lab3b: lab3b.cpp
	g++ lab3b.cpp -lstdc++ -Wall -Wextra -lstdc++ -std=c++17 -o lab3b.out

test-nocycle:
	python3 lab3_test.py test-nocycle

test-cycle:
	python3 lab3_test.py test-cycle

generate-tests:
	python3 lab3_test.py generate-tests

test-lab3a:
	python3 lab3_test.py test-lab3a

clean:
	rm -rf lab3a.out
	rm -rf lab3b.out
