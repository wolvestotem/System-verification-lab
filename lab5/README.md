[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2902664&assignment_repo_type=AssignmentRepo)
# EE 595 Lab 5 (Software Track)
In this lab, we are going to practice machine learning algorithms for classification. You will have to write and programs that implement k Nearest Neighbor,  Decision Tree, Support Vector Machines, and Neural Network machine learning algorithms to correctly classify a two-class dataset with an accuracy higher than 90%. We encourage you to try to achieve higher accuracy than the minimum required by the grading script. You can use the [Google Colab Notebook](https://colab.research.google.com/drive/1qqUB4n3QrRxeNye8TnehKbxBFNjm7zJj?usp=sharing) to access the dataset used for grading and also work online to find the best hyperparameters for this dataset. You can find more information about each algorithm along with examples of how to use them in the [User Guide](https://scikit-learn.org/stable/user_guide.html) of the `scikit-learn` library.

## :clipboard: Requirements
**Please read the entire file before proceeding!**
- **Deadline:** Friday, July 11, 2020, 23:59 PDT
- **Score:** Maximum 100 points.
    - 25 points for the k Nearest Neighbor classifier.
    - 25 points for the Decision Tree classifier.
    - 25 points for the Support Vector Machines classifier.
    - 25 points for the Neural Network classifier.
- **Submission limit:** Unlimited.
- **Time limit:** 1 minute for each of the four grading scripts.
- **Files:** You are allowed to change only the `lab5knn.py`, `lab5dt.py`, `lab5svm.py`, and `lab5nn.py` files. Changing other files will result in 0 points for this lab irrespective of the auto-grading result. In case you changed other files by accident, use the ``git`` command or the GitHub website to revert them to their initial content.
- **Grading:** The programs will be auto-graded by GitHub every time you submit new files.
- **Dependencies:** To work on this lab on your machine you will need to have ``python3``, ``pip3``, ``gcc``, ``make``, and ``git`` programs installed. To install them on Ubuntu, in a terminal run ``sudo apt install python3 python3-pip build-essential git``. Moreover, to run the grading script locally on your machine the ``scikit-learn`` Python 3 package must be installed. To install this package use the command ``pip3 install scikit-learn``. 
- **Online IDE:** You can work on this assignment online using the [repl.it](https://repl.it/) website which has all the required tools installed. Note, you still need to install the Python package using the command ``make install``. **Please log in using your GitHub account**. If the [repl.it](https://repl.it/) website does not allow you to open this repository then you need to claim your [GitHub Student Pack](https://education.github.com/discount_requests/new) (takes less than a minute).


## :keyboard: Usage
- ``make install`` to install the Python 3 packages required for auto-grading.
- ``python3 lab5knn.py X.txt y.txt X-grading.txt`` to run the classifier program assuming ``x.txt``, `y.txt` and `x-grading.txt` exist. Replace `lab5knn.py` with `lab5dt.py`, `lab5svm.py`, or `lab5nn.py` to run other classifiers.
- ``make test-knn`` to evaluate the k Nearest Neighbor classifier part of the assignment.
- ``make test-dt`` to evaluate the Decision Tree classifier part of the assignment.
- ``make test-svm`` to evaluate the Support Vector Machines classifier part of the assignment.
- ``make test-nn`` to evaluate the Neural Network classifier part of the assignment.


## :abacus: Problem Description
Implement four machine learning algorithms, k Nearest Neighbor,  Decision Tree, Support Vector Machines, and Neural Networks, for classification that achieve an accuracy higher than 90%. The name of the files containing the training dataset along with the input to be classified will be received as arguments. The classification result for the grading input will be written to the `result.txt` file. Each model has an associated python file where it must be implemented:
- `lab5knn.py` – k Nearest Neighbor
- `lab5dt.py` – Decision Tree
- `lab5svm.py` – Support Vector Machines
- `lab5nn.py` – Neural Networks

Note, these files already contain the code to load the dataset and save the result. You must write the code that finds the hyperparameters of the model that give an accuracy higher than 90% and train the model using the best hyperparameters.


## :bulb: Hints
- Check the ``lab5_test.py`` file to see what tests your programs have to pass.
- Check the [User Guide](https://scikit-learn.org/stable/user_guide.html) of the `scikit-learn` library for more information on the machine learning algorithms.
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
