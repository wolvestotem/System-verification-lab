.PHONY: all clean

all: test-c test-python

test-c: prelab
	python3 prelab_test.py ./prelab

test-python: prelab
	python3 prelab_test.py python3 prelab.py

prelab: prelab.c
	gcc prelab.c -o prelab
  
clean:
	rm -f prelab result.txt