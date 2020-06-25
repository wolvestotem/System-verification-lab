[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2875275&assignment_repo_type=AssignmentRepo)
# EE 595 Lab 4 (Software Track)
In this lab, we are going to practice graph algorithms and implement them using the C++ Standard Library (`std`). The lab consists of two programs. The first program is mandatory but the second program is for extra credit and can be submitted only if the first one was completed. For the mandatory part, you will check if a given graph is bipartite and output the minimum spanning tree of the graph. For the extra credit part, you will write a simple algorithm to perform the topological sorting of a given graph. We encourage you to use as much code (data structures and algorithms) as possible from the C++ standard library for the C++17 standard.

## :clipboard: Requirements
**Please read the entire file before proceeding!**
- **Deadline:** Friday, June 26, 2020, 23:59 PDT
- **Score:** Maximum 200 points.
    - 50+50 points for the first C++ program.
    - 50+50 points (extra credit) for the second C++ program. The extra credit is applied only if the first program is completed.
- **Submission limit:** Unlimited.
- **Time limit:** 3 minutes for each of the two grading scripts, minimum spanning tree, and topological sort.
- **Files:** You are allowed to change only the ``lab4a.cpp`` and ``lab4b.cpp`` files. Changing other files will result in 0 points for this lab irrespective of the auto-grading result. In case you changed other files by accident, use the ``git`` command or the GitHub website to revert them to their initial content.
- **Grading:** Both C++ programs will be auto-graded by GitHub every time you submit new files.
- **Dependencies:** To work on this lab on your machine you will need to have ``python3``, ``pip3``, ``gcc``, ``make``, and ``git`` programs installed. To install them on Ubuntu, in a terminal run ``sudo apt install python3 python3-pip build-essential git``. Moreover, to run the grading script locally on your machine the ``networkx`` Python 3 package must be installed. To install this package use the command ``pip3 install networkx``. 
- **Online IDE:** You can work on this assignment online using the [repl.it](https://repl.it/) website which has all the required tools installed. Note, you still need to install the Python package using the command ``make install``. **Please log in using your GitHub account**. If the [repl.it](https://repl.it/) website does not allow you to open this repository then you need to claim your [GitHub Student Pack](https://education.github.com/discount_requests/new) (takes less than a minute).


## :keyboard: Usage
- ``make install`` to install the Python 3 packages required for auto-grading.
- ``make lab4a`` to compile the first C++ program.
- ``./lab4a.out network.txt`` to run the first C++ program assuming ``network.txt`` exists. Run ``make lab4a`` first to generate the executable.
- ``make test-bipartite`` to evaluate the bipartite part of the first C++ program.
- ``make test-mst`` to evaluate the minimum spanning tree part of the first C++ program.
- ``make lab4b`` to compile the second C++ program.
- ``./lab4b.out network.txt`` to run the second C++ program assuming ``network.txt`` exists. Run ``make lab4b`` first to generate the executable.
- ``make test-tlsort`` to evaluate the second C++ program ignoring the lexicographical order of the nodes.
- ``make test-tlordered`` to evaluate the second C++ program and checking the lexicographical order of the nodes.

## :abacus: Problem Description
Create a program that checks if a given **undirected graph** is bipartite and also outputs the minimum spanning tree of the graph. The graph configuration will be given in a file using an edge list format and the file name will be passed as an argument to the program. 

The input file will have the following format: 
- The first line will contain 2 numbers separated by space, ``N M``, where ``N`` is the number of nodes in the undirected graph, and ``M`` is the number of edges. 
- The next ``M`` lines will contain 3 numbers, the two nodes between which a connection exists, and the weight of that connections.

The program will write the result into the ``result.txt`` file:
- On the first line, the program will write ``Yes`` if the given graph is bipartite or `No` otherwise. (50 points)
- On the subsequent lines, the program will write the graph edges, one per line, that are part of the minimum spanning tree in the ascending order by their weight. The edges are written as a pair of two nodes which they connect. (50 points)

Note, all numbers are positive integers and the two parts of the program are checked independently.


#### Example
Executing the following command ``./lab4b.out network.txt`` where the content of ``network.txt`` is:
```
6 7
3 1 0
3 5 3
1 0 1
0 5 2
0 2 5
5 4 3
4 2 4
```

This is a bipartite graph with `6` nodes and `7` edges. The two partitions contain the nodes `[3, 0, 4]` and `[1, 5, 2]`. The ``result.txt`` file should have the following content:
```
Yes
3 1
1 0
0 5
5 4
4 2
```
Note, if the graph had an additional edge between node `4` and `0` of weight `6` then the graph would no longer be bipartite, however, the minimum spanning tree would have remained the same.


## :abacus: Problem Description
Create a program that outputs the nodes of a given **directed graph** in topological order. The graph configuration will be given in a file using an edge list format and the file name will be passed as an argument to the program. 

The input file will have the following format: 
- The first line will contain 2 numbers separated by space, ``N M``, where ``N`` is the number of nodes in the undirected graph, and ``M`` is the number of edges. 
- The next ``M`` lines will contain 2 numbers, the source and destination nodes between which a connection exists.

The program will write the result into the ``result.txt`` file as a list of nodes in topological order separated by space. (50 points). An additional 50 points will be awarded if the nodes follow the topological and lexicographical order.


#### Example
Executing the following command ``./lab4b.out network.txt`` where the content of ``network.txt`` is:
```
5 4
2 1
3 1
1 0
1 4
```

The ``result.txt`` should contain one of the possible results, e.g., `3 2 1 4 0` or ` 2 3 1 0 4` which is also in lexicographical order.


## :bulb: Hints
- Check the ``lab4_test.py`` file to see what tests your programs have to pass.
- If your computer struggles to run the Linux virtual machine you can use the [repl.it](https://repl.it/) website which has all the needed tools preinstalled. If you claim your [GitHub Student Pack](https://education.github.com/discount_requests/new) and log in using GitHub then the available resources on this website are more than enough for this assignment.


## :memo: Grading
Grading is done automatically by GitHub every time you push your commits. Allow some time for the grading script to complete. The grading time depends on how efficient your code is. Each part of the homework has an independent time limit. Check the requirements section for details. 

GitHub will mark your commit message based on the grading result:
  * :white_check_mark: All test scenarios pass for all evaluation commands 
  * :x: At least one test scenario failed in at least one evaluation command
  
To see the grading result for the last commit click:
> *Actions* → *Commit message to check* → *Scroll down for the auto grading result*
>
> [![Check grading result](https://i.gyazo.com/cd72e0166bdeb3ef291c9f2b4454f4c7.gif)](https://gyazo.com/cd72e0166bdeb3ef291c9f2b4454f4c7)

For a detailed grading report containing each failed test click:
> *Actions* → *Commit message to check* → *Autograding in the left menu* → *Expand ``Run education/autograding@v1``*
>
> [![GIF animation with steps for the grade report](https://i.gyazo.com/2c98694f1d372a5be13e95641912228e.gif)](https://gyazo.com/2c98694f1d372a5be13e95641912228e)
