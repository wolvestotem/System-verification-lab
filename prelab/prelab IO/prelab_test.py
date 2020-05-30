import sys
import unittest
import subprocess


PROGRAM_NAME = []
states       = ['Alaska', 'California', 'North Dakota']


class PrelabTest(unittest.TestCase):

  def test_noinput(self):
    """
    Running the program without an input should produce an empty output file.
    """
    
    # Run program with no input arguments
    subprocess.run(PROGRAM_NAME, check=True)

    with open("result.txt") as resultfile:
      self.assertEqual(resultfile.read(), "")


  def test_wrongstate(self):
    """
    Running the program with a wrong state name should produce an empty output file.
    """

    # Run program with wrong state
    subprocess.run(PROGRAM_NAME + ["Wrong State"], check=True)
    
    with open("result.txt") as resultfile:
      self.assertEqual(resultfile.read(), "")


  def test_allstates(self):
    """
    Test that the program returns correct results for all states.
    """

    for state in states:
      with self.subTest(state=state):
        # Run program with each state name
        subprocess.run(PROGRAM_NAME + [state], check=True)

        with open("result.txt") as resultfile:
          resultlines = resultfile.readlines()

        with open("covid-confirmed-us-subset.txt") as datafile:
          datalines = datafile.readlines()

        # Check that each result line was present in the data file
        for line in resultlines:
          self.assertIn(line, datalines, msg="Line not present in the data file")

        # Check program did not miss any lines
        # Remove result from data and if state still present then lines where missed
        filteredlines = filter(lambda x: x not in resultlines, datalines)
        for line in filteredlines:
          self.assertNotIn(state, line, msg="Following lines were missed")

    
if __name__ == '__main__':

  # Run echo command if PROGRAM_NAME argument is missing
  PROGRAM_NAME += sys.argv[1:] if len(sys.argv) >= 2 else "echo" 

  suite  = unittest.defaultTestLoader.loadTestsFromTestCase(PrelabTest)
  result = unittest.TextTestRunner().run(suite)

  # Set the exit code based on the test result
  sys.exit(not result.wasSuccessful())