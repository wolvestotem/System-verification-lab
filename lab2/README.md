[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2838042&assignment_repo_type=AssignmentRepo)
# EE 595 Lab 2 (Software Track)
In this lab, you are going to practice the Test Driven Development methodology and write a simple C++ program that performs *sparse* matrix multiplication. We will continue to explore the object-oriented programming in C++ while getting our first hands-on experience with data structures. As the majority of elements in sparse matrices are 0, we will use linked lists to store only the non-zero elements to reduce the memory and the algorithmic complexity of the multiplication program.


## :clipboard: Requirements
**Please read the entire file before proceeding!**
- **Deadline:** Wednesday, June 10, 2020, 23:59 PDT
- **Score:** Maximum 110 points.
    - 50 points for using Test Driven Development.
    - 50 points for the C++ program.
    - 10 points for answering the questions. (Extra Credit)
- **Submission limit:** Unlimited.
- **Time limit:** 20 minutes for each grading script, TDD code coverage, and C++ program.
- **Files:** You are allowed to change only the ``lab2.cpp``, ``unittest.cpp``, ``Matrix.h``, ``Matrix.cpp``, and ``ANSWERS.md`` files. Changing other files will result in 0 points for this lab irrespective of the auto-grading result. In case you changed other files by accident, use the ``git`` command or the GitHub website to revert them to their initial content.
- **Grading:** The TDD code coverage and the C++ program will be auto graded by GitHub every time you submit new files. ``ANSWERS.md`` file will be manually graded after the deadline.
- **Dependencies:** To work on this lab on your machine you will need to have ``python3``, ``pip3``, ``gcc``, ``make``, and ``git`` programs installed. To install them on Ubuntu, in a terminal run ``sudo apt install python3 python3-pip build-essential git``. Moreover, to run the grading script locally on your machine the ``gcovr`` and ``numpy`` Python 3 packages must be installed. To install these package use the command ``pip3 install gcovr numpy``. 
- **Online IDE:** You can work on this assignment online using the [repl.it](https://repl.it/) website which has all the required tools installed. Note, you still need to install the Python package using the command ``pip3 install gcovr numpy``. If the [repl.it](https://repl.it/) website does not allow you to open this repository then you need to claim your [GitHub Student Pack](https://education.github.com/discount_requests/new) (takes less than a minute).


## :keyboard: Usage
- ``make install`` to install the Python 3 packages required for auto grading.
- ``make test`` to compile and run the unit tests from ``unittest.cpp`` file. Will generate an HTML report.
- ``make serve`` to start a webserver to view the code coverage report. You can also open the HTML files using your browser.
- ``make test-tdd`` to evaluate the code coverage part.
- ``make`` to compile the C++ program.
- ``./lab2.out file1.txt file2.txt`` to run the C++ program assuming ``file1.txt`` and ``file2.txt`` exist. Run ``make`` first to generate the executable.
- ``make test-cpp`` to evaluate the C++ program.


## :abacus: Test Driven Development (50 points)
Based on the Test Driven Development methodology implement unit tests in the ``unittest.cpp`` file before writing the implementations for the methods in the ``Matrix.cpp`` file. Use the [Catch2](https://github.com/catchorg/Catch2) test framework to write this tests. ([Short tutorial](https://github.com/catchorg/Catch2/blob/master/docs/tutorial.md#top) on Catch2 and [functions reference](https://github.com/catchorg/Catch2/blob/master/docs/Readme.md#top)) 

The auto grading script will award 50 points for reaching 100% code coverage for the ``Matrix.cpp`` file when running the unit tests. The branch coverage will be ignored during auto grading.

The use of the Test Driven Development methodology will be manually verified after the deadline based on the commit history. **A penalty of -20 points** will be applied if the development process will not reflect the following steps in order:
1. Write a unit test, check that it fails, and if so commit the unit test.
2. Write the minimal code that passes the test and then commit the implementation.
3. Refactor the code or the unit tests if necessary. If the code was modified check that all tests pass and then commit the modifications.
4. Repeat steps 1 to 3 until all the requirements for the methods in ``Matrix.cpp`` are implemented and tested.

All changes to the ``Matrix.cpp`` file should follow the above steps and be reflected in the git history.


## :abacus: C++ Problem Description
Create a program that receives two file names as arguments that contain the data for two *sparse* matrices and writes in the ``result.txt`` file the multiplication result of these matrices. However, this time the input matrices are large, a maximum dimension of 10000 by 10000 should be expected, but with only 10% of elements different from 0. Thus, implement a ``Vector`` class that stores only the non zero elements in a linked list. Next, implement a ``Matrix`` class which stores the data as an array of ``Vector``s. Follow the Test Driven Development methodology when implementing these two classes. Finally, implement the ``main`` function in ``lab2.cpp`` which will read the files, use the Matrix class to perform the multiplication, and then save the result into the ``result.txt`` file. 

All data files must have the following format: 
- The first row contains two numbers ``m n`` separated by space, and where ``m`` specifies the number of rows and ``n`` the number of columns of the matrix. 
- The following ``m`` lines contain ``n`` numbers separated by space. 
Also, assume that all the matrix entries are integer numbers and the dimensions of the two matrices are compatible with the matrix multiplication operation.

The ``Vector`` class will be manually verified after the deadline and a **penalty of -20 points** will be applied for using a different implementation other than linked lists.

#### Example
Executing the following command ``./lab2.out file1.txt file2.txt`` with the content for ``file1.txt``:
```
 3  3
-2  0  0
 0  1  0
 0  0 -1
```
and with the content for ``file2.txt``:
```
 3  2
 1  2
 3  4
 5  6
```
should produce a ``result.txt``:
```
 3  2
-2 -4
 3  4
-5 -6
```


## :abacus: Questions
Write the answer to these questions in the ``ANSWERS.md`` file and for each question explain your reasoning in one line.

1. *(2 points)* What actions can we take to ensure the tests in the Test Driven Development contain no mistakes?
2. *(2 points)* Assume all the requirements are covered by the unit tests, why this still does not guarantee an error-free execution of the program? (Hint: you can get some inspiration from the investigations of failed space missions) 
3. *(2 points)* What other code metrics besides test coverage can be used to evaluate the quality of the source code?
4. *(2 points)* Based on the description of the matrix multiplication problem, approximately how many elements would be non zero, as a function of ``n``, in the multiplication result matrix? (Note, matrices have the dimension of ``n`` by ``n`` and with the elements independent and identically distributed with a probability of 0.9 to be 0 and a probability of 0.1 to be non zero)
5. *(2 points)* Same question but for the matrix addition operation?


## :bulb: Hints
- Check the ``lab2_test.py`` file to see what tests your programs have to pass.
- A nice visualization of [common operations](https://www.tutorialspoint.com/data_structures_algorithms/linked_list_algorithms.htm) on linked lists.
- A short C++ tutorial on working with files can be found [here](https://www.cplusplus.com/doc/tutorial/files/).
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
