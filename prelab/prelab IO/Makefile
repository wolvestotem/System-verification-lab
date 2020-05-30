.PHONY: all clean

all: test-c test-python

test-c: prelab.out
	python3 prelab_test.py ./prelab.out

test-python: prelab.out
	python3 prelab_test.py python3 prelab.py

prelab.out: prelab.c
	gcc prelab.c -o prelab.out
  
clean:
	rm -f prelab.out result.txt