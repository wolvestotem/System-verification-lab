hello.o: hellomake.c hellofunc.c hellomake.h
	$(CC) hellomake.c hellofunc.c -o $@

all: hello.o
	./hello.o

clean:
	rm -f hello.o