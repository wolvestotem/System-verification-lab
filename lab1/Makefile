all: lab1.out
	make lab1.out

lab1.out: lab1.cpp Matrix.h Matrix.cpp
	g++ $? $(LDFLAGS) -o $@

clean:
	rm -f lab1.out result.txt A.txt B.txt
