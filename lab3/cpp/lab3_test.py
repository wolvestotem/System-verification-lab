import os
import sys
import random
import unittest
import subprocess

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


check_output = lambda x: subprocess.check_output(x, universal_newlines=True)


GRAPHS = []
GRAPHS_TO_TEST = []


def generate_tests(graphs, filename):
  
  for i, G in enumerate(graphs):
    # Use only the first 10 graphs 
    if i == 5:
      break

    title = filename.format(i)

    # Select the source and target nodes base on their centrality
    nodes   = []
    labels  = {}
    weights = []
    for node, centrality in nx.betweenness_centrality(G).items():
      nodes.append(node)
      labels[node] = str(node)
      weights.append(1.0 - centrality)

    S, T = random.choices(nodes, weights, k=2)
    
    # Source and target nodes should be different
    while S == T:
      S, T = random.choices(nodes, weights, k=2)

    lines = list(nx.generate_edgelist(G, data=False))
    lines = ["{} {} {}".format(len(lines), S, T)] + lines
    with open(title+".txt", "w") as f:
      f.write("\n".join(lines))

    lines = []
    with open(title+"-result.txt".format(i), "w") as f:
      for path in nx.all_simple_paths(G, S, T):
        length = len(path) - 1
        links  = " => ".join(map(str, path))
        lines += ["{} # {}".format(length, links)]
      f.write("\n".join(lines)) 

    fig = plt.figure(figsize=[6, 6])
    ax = plt.gca()
    nx.draw(G, with_label=True, labels=labels)
    fig.suptitle(title+".png")
    plt.tight_layout(0.9)
    fig.savefig(title+".png")


class Lab3ShortestPathTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "lab3b"])


  def save(self, G, S, T, filename):
    """
    Save graph G to file using the specified format
    """
    lines = list(nx.generate_edgelist(G, data=False))
    lines = ["{} {} {}".format(len(lines), S, T)] + lines
    with open(filename, "w") as f:
      f.write("\n".join(lines))


  def load_result(self, filename):
    """
    Load result from file. Return first number on each line
    """

    with open(filename) as f:
      datalines = f.readlines()

    return [int(line.split()[0]) for line in datalines]


  def test_graph(self):
    """
    Check the program output
    """

    for graph_index in GRAPHS_TO_TEST:
      with self.subTest(test=graph_index):
        G = GRAPHS[graph_index]

        # Select the source and target nodes base on their centrality
        nodes   = []
        weights = []
        for node, centrality in nx.betweenness_centrality(G).items():
          nodes.append(node)
          weights.append(1.0 - centrality)

        S, T = random.choices(nodes, weights, k=2)
        
        # Source and target nodes should be different
        while S == T:
          S, T = random.choices(nodes, weights, k=2)

        self.save(G, S, T, "input-network.txt")

        subprocess.check_call(["./lab3b.out", "input-network.txt"])

        reference = sorted([len(path) - 1 for path in nx.all_simple_paths(G, S, T)])
        result    = self.load_result("result.txt")

        self.assertEqual(reference[0], result[0])



class Lab3CppTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "lab3a"])

  
  def randmatrix(self, m, n):
    """
    Generate a matrix with random elements
    """
    A = np.random.rand(m, n) * 10
    return A


  def save(self, M, filename):
    """
    Save matrix M to file using the specified format
    """
    m, n = M.shape

    np.savetxt(filename, M, fmt='%.5f', header="{} {}".format(m, n), comments='')


  def read(self, filename):
    """
    Returns first line
    """

    with open(filename) as f:
      lines = f.readlines()

    return lines[0] if len(lines) else ""



  def test_zerovector(self):
    """
    Check with a zero vector
    """
    m = random.randint(5, 10)
    p = m
    n = 1

    M = self.randmatrix(m, p)
    V = self.randmatrix(p, n)
    V[:, 0] = 0

    self.save(M, "M.txt")
    self.save(V, "V.txt")

    subprocess.check_call(["./lab3a.out", "M.txt", "V.txt"])

    R = self.read("result.txt")
    self.assertEqual("No", R, msg="Zero vector cannot be an eigenvector")


  def test_random_matrix_eig(self):
    """
    Eigenvector of a random matrix
    """

    m = random.randint(5, 9)
    p = m
    n = 1

    M = self.randmatrix(m, p)
    M = M.T @ M
      
    eigval, Q = np.linalg.eig(M)

    # Randomly select an eigenvector and value
    idx = random.randint(0, m - 1)
    V   = Q[:, idx].reshape(m, 1)

    self.save(M, "M.txt")
    self.save(V, "V.txt")

    subprocess.check_call(["./lab3a.out", "M.txt", "V.txt"])

    R = self.read("result.txt")
    self.assertAlmostEqual(eigval[idx], float(R), delta=0.1, msg="Different value expected")


  def test_random_matrix_noeig(self):
    """
    Not an eigenvector of a random matrix
    """

    m = random.randint(5, 9)
    p = m
    n = 1

    M = self.randmatrix(m, p)
    M = M.T @ M
      
    eigval, Q = np.linalg.eig(M)

    # Randomly select an eigenvector and value
    idx1 = 0
    idx2 = random.randint(1, m - 1)

    V   = (Q[:, idx1] + Q[:, idx2]).reshape(m, 1)

    self.save(M, "M.txt")
    self.save(V, "V.txt")

    subprocess.check_call(["./lab3a.out", "M.txt", "V.txt"])

    R = self.read("result.txt")
    self.assertEqual("No", R, msg="No expected")


  def test_wrong_dim(self):
    """
    Not an eigenvector of a random matrix
    """

    m = random.randint(5, 10)
    p = 4
    n = 1

    M = self.randmatrix(m, p)
    V = self.randmatrix(p, n)

    self.save(M, "M.txt")
    self.save(V, "V.txt")

    subprocess.check_call(["./lab3a.out", "M.txt", "V.txt"])

    R = self.read("result.txt")
    self.assertEqual("Error", R)
  
    
if __name__ == '__main__':

  suite = unittest.TestSuite()

  if len(sys.argv) == 2 and sys.argv[1] == "test-nocycle":
    
    # Create a list of graphs containing 7 nodes and without cycles
    GRAPHS = nx.generators.atlas.graph_atlas_g()
    GRAPHS = list(filter(lambda g: nx.is_tree(g) and g.number_of_nodes() == 7, GRAPHS[1:]))
    
    GRAPHS_TO_TEST = [i for i in range(5)]

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab3ShortestPathTest))
  

  elif len(sys.argv) == 2 and sys.argv[1] == "test-cycle":
    
    # Create a list of graphs containing 7 nodes and without cycles
    GRAPHS = nx.generators.atlas.graph_atlas_g()
    GRAPHS = list(filter(lambda g: nx.is_connected(g) and g.number_of_nodes() == 6 and nx.cycle_basis(g), GRAPHS[1:]))
    
    GRAPHS_TO_TEST = [i for i in range(5)]

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab3ShortestPathTest))
  

  elif len(sys.argv) == 2 and sys.argv[1] == "generate-tests":

    # Create a list of graphs containing 7 nodes and without cycles
    graphs = nx.generators.atlas.graph_atlas_g()

    trees = filter(lambda g: nx.is_tree(g) and g.number_of_nodes() == 7, graphs[1:])
    generate_tests(trees, "tests/nocycle-test-{}")

    cycles = filter(lambda g: nx.is_connected(g) and g.number_of_nodes() == 6 and nx.cycle_basis(g), graphs[1:])
    
    generate_tests(cycles, "tests/cycle-test-{}")


  elif len(sys.argv) == 2 and sys.argv[1] == "test-lab3a":

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab3CppTest))

  else:
    print("No tests provided")
    sys.exit(1)


  result = unittest.TextTestRunner().run(suite)

  # Set the exit code based on the test result
  sys.exit(not result.wasSuccessful())
