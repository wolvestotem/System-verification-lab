import os
import sys
import random
import unittest
import subprocess


# Fix for Python 3.4
check_output = lambda x: subprocess.check_output(x, universal_newlines=True)


class Lab1BashTest(unittest.TestCase):

  def setUp(self):
    """
    Remove bash-playground folder and run the script lab1.sh script file
    """

    # Remove bash-playground folder
    subprocess.check_call(["rm", "-rf", "bash-playground"])
    # Run lab1.sh script
    subprocess.check_call(["bash", "lab1.sh"])


  def test_folder_contents(self):
    """
    bash-playground folder contains the correct files
    """
    # Select .cpp files in the curent directory 
    cpp_files = {f for f in os.listdir(".") if f.endswith(".cpp")}

    # Check the contents of bash-playground folder
    bash_playground_files = set(os.listdir("./bash-playground/"))

    self.assertIn('backup', bash_playground_files)
    bash_playground_files.remove('backup')

    self.assertIn('VERSIONS', bash_playground_files)
    bash_playground_files.remove('VERSIONS')

    self.assertEqual(cpp_files, bash_playground_files)

    lab_files = {f for f in bash_playground_files if "lab" in f}

    # Check the contents of bash-playground/backup folder
    backup_files = set(os.listdir("./bash-playground/backup/"))
    self.assertEqual(lab_files, backup_files)


  def test_VERSIONS(self):
    """
    Check if VERSIONS files contains the right data
    """

    make_version = check_output(["make", "--version"]).split("\n")[0]
    gcc_version  = check_output(["gcc",  "--version"]).split("\n")[0]

    with open("./bash-playground/VERSIONS") as f:
      self.assertEqual([make_version, gcc_version], f.read().splitlines()[:2], msg="Versions do not match")


class Lab1MakefileTest(unittest.TestCase):

  def setUp(self):
    """
    Check update time for all files
    """

    subprocess.check_call(["rm", "-rf", "lab1.out"])


  def test_make_all(self):
    """
    Running make all creates the executable lab1.out
    """

    self.assertNotIn("lab1.out", os.listdir("."))
    subprocess.check_call(["make", "all"])
    self.assertIn("lab1.out", os.listdir("."))

  
  def test_make_all2(self):
    """
    Running make all second time should not alter the files
    """
    
    # Run make all twice
    subprocess.check_call(["make", "all"])
    files_before = {(f, os.stat(f).st_mtime) for f in os.listdir(".")}
    subprocess.check_call(["make", "all"])
    files_after = {(f, os.stat(f).st_mtime) for f in os.listdir(".")}

    self.assertEqual(files_before, files_after)

  
  def test_make_all3(self):
    """
    Running make all second time after changing Matrix.h should recreate lab1.out
    """
    
    # Run make all twice
    subprocess.check_call(["make", "all"])
    files_before = {(f, os.stat(f).st_mtime) for f in os.listdir(".")}
    # Add a comment line
    with open("Matrix.h", "a") as f:
      f.write("// Changed\n")

    subprocess.check_call(["make", "all"])
    files_after = {(f, os.stat(f).st_mtime) for f in os.listdir(".")}

    self.assertNotEqual(files_before, files_after)


  def test_make_clean(self):
    """
    Running make clean after make all restores the directory to initial state
    """

    self.assertNotIn("lab1.out", os.listdir("."))
    subprocess.check_call(["make", "all"])
    self.assertIn("lab1.out", os.listdir("."))
    subprocess.check_call(["make", "clean"])
    self.assertNotIn("lab1.out", os.listdir("."))


class Lab1CppTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "all"])

  
  def randmatrix(self, m, n):
    """
    Generate a matrix with random elements
    """
    return [[random.randint(-9, 9) for j in range(n)] for i in range(m)]


  def save(self, M, filename):
    """
    Save matrix M to file using the specified format
    """
    m, n = len(M), len(M[0])

    with open(filename, "w") as f:
      f.write("{} {}\n".format(m, n))

      for row in M:
        f.write(" ".join(map(str, row)) + "\n")


  def load(self, filename):
    """
    Load matrix from file. Returns [[int, ...], ...], (int, int)
    """

    # Separate first line from the rest
    with open(filename) as f:
      dimline, *datalines = f.readlines()

    mat = [list(map(int, line.split())) for line in datalines]
    dim = tuple(map(int, dimline.split()))

    return mat, dim


  def multiply(self, A, B):
    """
    Multiply two matrices
    """

    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]


  def test_example(self):
    """
    Check the program against provided test_example
    """

    A = [[-2, 0, 0], [0, 1, 0], [0, 0, -1]]
    B = [[1, 2], [3, 4], [5, 6]]

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab1.out", "A.txt", "B.txt"])

    C, dim = self.load("result.txt")

    self.assertEqual((3,2), dim, msg="Result dimensions do not match")
    self.assertEqual(self.multiply(A,B), C, msg="Incorrect multiplication result")


  def test_vector_vector(self):
    """
    Check vector (m by 1) multiplied with vector (1 by n)
    """

    m, p, n = 7, 1, 7

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab1.out", "A.txt", "B.txt"])

    C, dim = self.load("result.txt")

    self.assertEqual((m,n), dim, msg="Result dimensions do not match")
    self.assertEqual(self.multiply(A,B), C, msg="Incorrect multiplication result")

  
  def test_vector_vector2(self):
    """
    Check vector (1 by p) multiplied with vector (p by 1)
    """

    m, p, n = 1, 7, 1

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab1.out", "A.txt", "B.txt"])

    C, dim = self.load("result.txt")

    self.assertEqual((m,n), dim, msg="Result dimensions do not match")
    self.assertEqual(self.multiply(A,B), C, msg="Incorrect multiplication result")

  
  def test_matrix_vector(self):
    """
    Check matrix (m by p) multiplied with vector (p by 1)
    """

    m, p, n = random.randint(3, 9), random.randint(3, 9), 1

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab1.out", "A.txt", "B.txt"])

    C, dim = self.load("result.txt")

    self.assertEqual((m,n), dim, msg="Result dimensions do not match")
    self.assertEqual(self.multiply(A,B), C, msg="Incorrect multiplication result")


  def test_large_matrix_matrix(self):
    """
    Check matrix (m by p) multiplied with matrix (p by n)
    """

    m, p, n = random.randint(5, 9), random.randint(5, 9), random.randint(5, 9)

    A = self.randmatrix(m, p)
    B = self.randmatrix(p, n)

    self.save(A, "A.txt")
    self.save(B, "B.txt")

    subprocess.check_call(["./lab1.out", "A.txt", "B.txt"])

    C, dim = self.load("result.txt")

    self.assertEqual((m,n), dim, msg="Result dimensions do not match")
    self.assertEqual(self.multiply(A,B), C, msg="Incorrect multiplication result")

    
if __name__ == '__main__':

  # Run echo command if PROGRAM_NAME argument is missing
  #PROGRAM_NAME += sys.argv[1:] if len(sys.argv) >= 2 else "echo" 
  suite = unittest.TestSuite()

  if len(sys.argv) == 2 and sys.argv[1] == "test-bash":
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab1BashTest))
  elif len(sys.argv) == 2 and sys.argv[1] == "test-makefile":
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab1MakefileTest))
  elif len(sys.argv) == 2 and sys.argv[1] == "test-cpp":
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab1CppTest))
  else:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab1BashTest))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab1MakefileTest))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab1CppTest))


  result = unittest.TextTestRunner().run(suite)

  # Set the exit code based on the test result
  sys.exit(not result.wasSuccessful())
