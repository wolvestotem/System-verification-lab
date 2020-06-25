all: lab4a lab4b

install:
	pip3 install networkx

lab4a: lab4a.cpp
	g++ lab4a.cpp -Wall -Wextra -lstdc++ -std=c++17 -o lab4a.out

lab4b: lab4b.cpp
	g++ lab4b.cpp -Wall -Wextra -lstdc++ -std=c++17 -o lab4b.out

test-bipartite:
	python3 lab4_test.py test-bipartite

test-mst:
	python3 lab4_test.py test-mst

test-tlsort:
	python3 lab4_test.py test-tlsort

test-tlordered:
	python3 lab4_test.py test-tlordered

clean:
	rm -rf lab4a.out
	rm -rf lab4b.out