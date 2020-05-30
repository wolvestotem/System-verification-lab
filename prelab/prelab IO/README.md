# EE 595 Prelab
In this lab, you are going to write simple programs in C and Python to filter a large dataset file based on a keyword. This is usually the first step of any machine learning algorithm. To make things easier the requirements for the C and Python 3 programs are the same. 


## :clipboard: Requirements
- **Deadline:** Wednesday, May 27, 2020, 23:59 PDT
- **Score:** Maximum 100 points.
    - 50 points for the Python program.
    - 50 points for the C program.
- **Time limit:** 5 minutes for both, C and Python, grading scripts (10 minutes total).
- **Files:** You are allowed to change only the ``prelab.py`` and ``prelab.c`` files. Changing other files will result in 0 points for this lab irrespective of the auto-grading result. In case you changed other files by accident, use the ``git`` command to revert them to their initial content. 
- **Dependencies:** To complete this lab you will need to have ``python3``, ``gcc``, ``make``, and ``git`` programs installed on your system. To install them on Ubuntu, in a terminal run ``sudo apt install python3 build-essential git``.


## :abacus: Problem Description

Create a program that receives a keyword as the first command-line argument and writes in the ``result.txt`` file all the lines of ``covid-confirmed-us-subset.txt`` file that contain the keyword. If the keyword is omitted then the ``result.txt`` file must be empty. Similarly, if none of the lines in ``covid-confirmed-us-subset.txt`` contains the keyword then ``result.txt`` file must also be empty.

``covid-confirmed-us-subset.txt`` is a small subset that contains time series of the number of confirmed COVID-19 cases for different counties in the US. For now, we are not interested in the actual numbers, just in generating subsets of it such as California cases only. If you are interested, the full dataset that can be found [here](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv).


## :ab: Example
Assuming a ``covid-confirmed-us-subset.txt`` file with the following content:
```
Autauga,Alabama,US,127,136,143,149
Los Angeles,California,US,262,270,269,271  
```
Running ``python3 prelab.py California`` should produce a ``result.txt`` file with the following content:
```
Los Angeles,California,US,262,270,269,271  
```
However, running ``python3 prelab.py`` or ``python3 prelab.py Jalisco`` should produce an empty ``result.txt`` file.


## :keyboard: Usage 
- ``python3 prelab.py keyword`` to run the Python program.
- ``make test-python`` to evaluate the Python program against the 3 test cases.
- ``make prelab.out`` to compile the C program, an executable file called ``prelab.out`` will be created.
- ``./prelab.out keyword`` to run the C program.
- ``make test-c`` to evaluate the C program against the 3 test cases.
- ``make`` to evaluate both, C and Python programs.
- ``make clean`` to remove the generated files.


## :bulb: Hints
- Check the ``prelab_test.py`` file to see exactly how your program will be evaluated.
- Opening a file in write mode automatically clears its content.
- For Python, you can use [``readlines``](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) method of the file object to read all the lines in a list.
- For C, you can use [``fgets``](https://www.tutorialspoint.com/c_standard_library/c_function_fgets.htm) and [``strstr``](https://www.tutorialspoint.com/c_standard_library/c_function_strstr.htm) functions to read a line from a file and to search for a string respectively.
- If your computer struggles to run the Linux virtual machine you can use the [repl.it](https://repl.it/) website which has all the needed tools preinstalled. The free version is more than enough for this assignment.


## :feet: Recommended Steps
- [ ] **``Python``** If no input arguments ``len(sys.argv) < 2``, create an empty ``result.txt`` file.
- [ ] **``Python``** Use the first input argument ``sys.argv[1]`` to filter the lines in ``covid-confirmed-us-subset.txt``.
- [ ] **``Python``** Check that if ``sys.argv[1]`` is not present in ``covid-confirmed-us-subset.txt`` then ``result.txt`` file is empty.
- [ ] **``Git``** Commit and push ``prelab.py`` to GitHub for partial credit.
- [ ] **``C``** If no input arguments ``argc < 2``, create an empty ``result.txt`` file.
- [ ] **``C``** Use the first input argument ``argv[1]`` to filter the lines in ``covid-confirmed-us-subset.txt``. 
- [ ] **``C``** Check that if ``argv[1]`` is not present in ``covid-confirmed-us-subset.txt`` then ``result.txt`` file is empty.
- [ ] **``Git``** Commit and push ``prelab.c`` to GitHub for full credit.


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
