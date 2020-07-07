import sys
import unittest
import subprocess


import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

PROGRAM = ""

check_output = lambda x: subprocess.check_output(x, universal_newlines=True)


class Lab5Test(unittest.TestCase):


  def test_model(self):
    """
    Check program output for the given dataset
    """
    X_raw, y_raw = make_classification(200, n_features=4, n_redundant=0, n_informative=2, class_sep=1.4, random_state=42)

    X, X_grading, y, y_grading = train_test_split(X_raw, y_raw, test_size=0.5, random_state=42)

    np.savetxt("X.txt", X)
    np.savetxt("y.txt", y, fmt="%d")
    np.savetxt("X-grading.txt", X_grading)

    subprocess.check_call(["python3", PROGRAM, "X.txt", "y.txt", "X-grading.txt"])

    result    = np.loadtxt("result.txt", dtype=np.int)
    accuracy  = accuracy_score(y_grading, result)

    self.assertGreaterEqual(accuracy, 0.90)

    
if __name__ == '__main__':

  if len(sys.argv) == 2 and sys.argv[1] == "test-knn":
    PROGRAM = "lab5knn.py"

  elif len(sys.argv) == 2 and sys.argv[1] == "test-dt":
    PROGRAM = "lab5dt.py"

  elif len(sys.argv) == 2 and sys.argv[1] == "test-svm":
    PROGRAM = "lab5svm.py"

  elif len(sys.argv) == 2 and sys.argv[1] == "test-nn":
    PROGRAM = "lab5nn.py"

  else:
    print("No tests provided")
    sys.exit(1)

  suite = unittest.TestSuite()
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab5Test))
  result = unittest.TextTestRunner().run(suite)

  # Set the exit code based on the test result
  sys.exit(not result.wasSuccessful())
