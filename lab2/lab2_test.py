import os
import sys
import random
import unittest
import subprocess

import numpy as np


check_output = lambda x: subprocess.check_output(x, universal_newlines=True)


class Lab2Coverage(unittest.TestCase):

  def setUp(self):
    """
    Generate coverage report
    """

    # Remove bash-playground folder
    subprocess.check_call(["make", "test"])


  def test_Matrix_coverage(self):
    """
    Check if the test coverage of the Matrix.cpp is 100%
    """

    coverage = "not found"
    for l in check_output(["python3", "coverage.py", "-r", ".", "-f", "Matrix.cpp"]).split("\n"):
      if l.startswith("Matrix.cpp"):
        coverage = l.split()[3]

    self.assertEqual(coverage, "100%", msg="Test coverage is not 100%")


class Lab2CppTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "all"])

  
  def randmatrix(self, m, n):
    """
    Generate a matrix with random elements
    """
    A = np.random.randint(0, 100, size=[m, n])
    A[A > 10] = 0
    return A


  def save(self, M, filename):
    """
    Save matrix M to file using the specified format
    """
    m, n = M.shape

    np.savetxt(filename, M, fmt='%d', header="{} {}".format(m, n), comments='')


  def load(self, filename):
    """
    Load matrix from file.
    """

    return np.loadtxt(filename, dtype='int32', skiprows=1)


  def multiply(self, A, B):
    """
    Multiply two matrices
    """

    return np.matmul(A, B)


  def test_example(self):
    """
    Check the program against provided test_example
    """

    m, p, n = 3, 3, 2
    A = np.array([[-2, 0, 0], [0, 1, 0], [0, 0, -1]], dtype='int8')
    B = np.array([[1, 2], [3, 4], [5, 6]], dtype='int8')

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab2.out", "A.txt", "B.txt"])

    C = self.load("result.txt")
    self.assertTrue(np.array_equal(self.multiply(A,B), C), msg="Incorrect multiplication result")



  def test_vector_vector(self):
    """
    Check vector (m by 1) multiplied with vector (1 by n)
    """

    m, p, n = 700, 1, 700

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab2.out", "A.txt", "B.txt"])

    C = self.load("result.txt")

    self.assertTrue(np.array_equal(self.multiply(A,B), C), msg="Incorrect multiplication result")

  
  def test_vector_vector2(self):
    """
    Check vector (1 by p) multiplied with vector (p by 1)
    """

    m, p, n = 1, 10000, 1

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab2.out", "A.txt", "B.txt"])

    C = self.load("result.txt").reshape(m, n)

    self.assertTrue(np.array_equal(self.multiply(A,B), C), msg="Incorrect multiplication result")

  
  def test_matrix_vector(self):
    """
    Check matrix (m by p) multiplied with vector (p by 1)
    """

    m, p, n = random.randint(400, 500), random.randint(400, 500), 1

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab2.out", "A.txt", "B.txt"])

    C = self.load("result.txt").reshape(m, n)

    self.assertTrue(np.array_equal(self.multiply(A,B), C), msg="Incorrect multiplication result")


  def test_large_matrix_matrix(self):
    """
    Check matrix (m by p) multiplied with matrix (p by n)
    """

    m, p, n = random.randint(400, 500), random.randint(400, 500), random.randint(400, 500)

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab2.out", "A.txt", "B.txt"])

    C = self.load("result.txt")

    self.assertTrue(np.array_equal(self.multiply(A,B), C), msg="Incorrect multiplication result")

    
if __name__ == '__main__':

  suite = unittest.TestSuite()

  if len(sys.argv) == 2 and sys.argv[1] == "test-tdd":
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab2Coverage))
  elif len(sys.argv) == 2 and sys.argv[1] == "test-cpp":
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab2CppTest))
  else:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab2Coverage))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab2CppTest))


  result = unittest.TextTestRunner().run(suite)

  # Set the exit code based on the test result
  sys.exit(not result.wasSuccessful())
