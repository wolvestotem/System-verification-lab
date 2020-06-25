import os
import sys
import math
import random
import unittest
import subprocess

import networkx as nx

from itertools import cycle, product

check_output = lambda x: subprocess.check_output(x, universal_newlines=True)


def sort_ends(edge_list):
    return [(u, v) if u < v else (v, u) for u, v in edge_list]


def save(G, filename, data=None):
  """
  Save graph G to file using the specified format
  """
  if data:
    lines = ["{} {} {}".format(u, v, G[u][v][data]) for u, v in G.edges]
  else:
    lines = ["{} {}".format(u, v) for u, v in G.edges]

  with open(filename, "w") as f:
    f.write("{} {}\n".format(G.number_of_nodes(), G.number_of_edges()))
    f.write("\n".join(lines))


def random_cycle_graph(num_nodes):
  
  weights = [k for k in range(num_nodes)]
  random.shuffle(weights)

  edge_list  = [(k-1, k, {'weight': w}) for k, w in zip(range(1, num_nodes), weights)]
  edge_list += [(0, num_nodes-1, {'weight': weights[-1]})]

  G = nx.Graph()
  G.add_edges_from(edge_list)

  return G


def random_graph(num_nodes, ratio=0.7, bipartite=True):

  # Create 2 partitions
  nodes = [k for k in range(num_nodes * 2)]
  random.shuffle(nodes)
  set1 = nodes[:num_nodes]
  set2 = nodes[num_nodes:]

  # MST
  edges = {}
  for i in range(num_nodes):

    edges[(set1[i], set2[i])]   = i * 2

    if i != 0:
      edges[(set1[i], set2[i-1])] = i * 2 - 1
      # add cycle not part of mst
      edges[(set1[i-1], set2[i])] = i * 2 + 1

  # Add edges not part of MST
  num_edges = math.ceil((num_nodes ** 2) * ratio)
  new_edges = [(u, v) for u in set1 for v in set2 if (u, v) not in edges]
  random.shuffle(new_edges)

  for i in range(num_edges - len(edges)):
    w = random.randint(num_nodes * 2, num_nodes + 5)
    edges[(new_edges[i][0], new_edges[i][1])] = w


  G = nx.Graph()
  G.add_edges_from([(e[0], e[1], {'weight': w}) for e, w in edges.items()])

  if bipartite == False:
    G.add_edge(set1[0], set1[1], weight=random.randint(num_nodes * 2, num_nodes + 5))

  return G


def random_tl_graph(nodes_distribution):
  N = sum(nodes_distribution)

  # Setup nodes partitions
  nodes = [k for k in range(N)]
  random.shuffle(nodes)
  groups = []
  last_idx = 0

  for delta in nodes_distribution:
    groups.append(nodes[last_idx:last_idx+delta])
    last_idx += delta

  edges = []
  # Setup edges
  for g1, g2 in zip(groups, groups[1:]):
    random.shuffle(g2)

    it1, it2 = (cycle(g1), g2) if len(g2) > len(g1) else (g1, cycle(g2))
    for u, v in zip(it1, it2):
      edges.append((u, v))

    # Add random edges
    edges += [(u, v) for u, v in product(g1, g2) if random.random() < 0.7 and (u, v) not in edges]

  G = nx.DiGraph()
  G.add_edges_from(edges)

  return G


class Lab4BipartiteTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "lab4a"])


  def load_result(self, filename):
    """
    Load result from file. Return first number on each line
    """

    with open(filename) as f:
      lines = f.readlines()

    return lines[0].strip().upper()


  def test_cycle_graph1(self):
    """
    Check program output for an even cycle graph
    """
    N = random.randint(2, 5) * 2
    G = random_cycle_graph(N)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])

    reference = "YES" if nx.is_bipartite(G) else "NO"
    result    = self.load_result("result.txt")

    self.assertEqual(reference, result)


  def test_cycle_graph2(self):
    """
    Check program output for an odd cycle graph
    """
    N = random.randint(2, 5) * 2 - 1
    G = random_cycle_graph(N)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])

    reference = "YES" if nx.is_bipartite(G) else "NO"
    result    = self.load_result("result.txt")

    self.assertEqual(reference, result)


  def test_random_graph1(self):
    """
    Check program output for a random bipartite graph
    """
    N = random.randint(3, 5)
    G = random_graph(N, bipartite=True)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])

    reference = "YES" if nx.is_bipartite(G) else "NO"
    result    = self.load_result("result.txt")

    self.assertEqual(reference, result)


  def test_random_graph2(self):
    """
    Check program output for a random not bipartite graph
    """
    N = random.randint(3, 5)
    G = random_graph(N, bipartite=False)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])
    
    reference = "YES" if nx.is_bipartite(G) else "NO"
    result    = self.load_result("result.txt")

    self.assertEqual(reference, result)



class Lab4MinimumSpanningTreeTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "lab4a"])


  def load_result(self, filename):
    """
    Load result from file. Return first number on each line
    """

    with open(filename) as f:
      lines = f.readlines()

    result = []
    for l in lines[1:]:
      u, v = map(int, l.split())

      result.append((u, v))

    return result


  def test_cycle_graph1(self):
    """
    Check program output for an even cycle graph
    """
    N = random.randint(2, 5) * 2
    G = random_cycle_graph(N)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])
    

    reference = sort_ends(nx.minimum_spanning_edges(G, data=False))
    result    = sort_ends(self.load_result("result.txt"))

    self.assertEqual(reference, result)


  def test_cycle_graph2(self):
    """
    Check program output for an odd cycle graph
    """
    N = random.randint(2, 5) * 2 - 1
    G = random_cycle_graph(N)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])

    reference = sort_ends(nx.minimum_spanning_edges(G, data=False))
    result    = sort_ends(self.load_result("result.txt"))

    self.assertEqual(reference, result)


  def test_random_graph1(self):
    """
    Check program output for a random bipartite graph
    """
    N = random.randint(3, 5)
    G = random_graph(N, bipartite=True)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])
    
    reference = sort_ends(nx.minimum_spanning_edges(G, data=False))
    result    = sort_ends(self.load_result("result.txt"))

    self.assertEqual(reference, result)


  def test_random_graph2(self):
    """
    Check program output for a random not bipartite graph
    """
    N = random.randint(3, 5)
    G = random_graph(N, bipartite=False)

    save(G, "input-network.txt", "weight")

    subprocess.check_call(["./lab4a.out", "input-network.txt"])
    
    reference = sort_ends(nx.minimum_spanning_edges(G, data=False))
    result    = sort_ends(self.load_result("result.txt"))

    self.assertEqual(reference, result)
  

class Lab4TLSortTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "lab4b"])


  def load_result(self, filename):
    """
    Load result from file. Return first number on each line
    """

    with open(filename) as f:
      lines = f.readlines()

    return list(map(int, lines[0].split()))


  def test_chain_graph(self):
    """
    Check program output for node chain
    """
    G = random_tl_graph([1, 1, 1, 1, 1])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.all_topological_sorts(G))
    result    = self.load_result("result.txt")

    self.assertIn(result, reference)


  def test_simple_graph1(self):

    G = random_tl_graph([1, 2, 1])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.all_topological_sorts(G))
    result    = self.load_result("result.txt")

    self.assertIn(result, reference)


  def test_simple_graph2(self):

    G = random_tl_graph([2, 1, 2])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.all_topological_sorts(G))
    result    = self.load_result("result.txt")

    self.assertIn(result, reference)


  def test_graph(self):

    G = random_tl_graph([2, 4, 3, 1])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.all_topological_sorts(G))
    result    = self.load_result("result.txt")

    self.assertIn(result, reference)


class Lab4TLOrderedTest(unittest.TestCase):

  def setUp(self):
    """
    Compile the program before testing
    """
    subprocess.check_call(["make", "lab4b"])


  def load_result(self, filename):
    """
    Load result from file. Return first number on each line
    """

    with open(filename) as f:
      lines = f.readlines()

    return list(map(int, lines[0].split()))


  def test_chain_graph(self):
    """
    Check program output for node chain
    """
    G = random_tl_graph([1, 1, 1, 1, 1])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.lexicographical_topological_sort(G))
    result    = self.load_result("result.txt")

    self.assertEqual(result, reference)


  def test_simple_graph1(self):

    G = random_tl_graph([1, 2, 1])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.lexicographical_topological_sort(G))
    result    = self.load_result("result.txt")

    self.assertEqual(result, reference)


  def test_simple_graph2(self):

    G = random_tl_graph([2, 1, 2])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])

    reference = list(nx.lexicographical_topological_sort(G))
    result    = self.load_result("result.txt")

    self.assertEqual(result, reference)


  def test_graph(self):

    G = random_tl_graph([2, 4, 3, 1])

    save(G, "input-network.txt")

    subprocess.check_call(["./lab4b.out", "input-network.txt"])
    
    reference = list(nx.lexicographical_topological_sort(G))
    result    = self.load_result("result.txt")

    self.assertEqual(result, reference)

    
if __name__ == '__main__':

  suite = unittest.TestSuite()

  if len(sys.argv) == 2 and sys.argv[1] == "test-bipartite":

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab4BipartiteTest))
  

  elif len(sys.argv) == 2 and sys.argv[1] == "test-mst":

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab4MinimumSpanningTreeTest))


  elif len(sys.argv) == 2 and sys.argv[1] == "test-tlsort":

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab4TLSortTest))


  elif len(sys.argv) == 2 and sys.argv[1] == "test-tlordered":

    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Lab4TLOrderedTest))

  else:
    print("No tests provided")
    sys.exit(1)


  result = unittest.TextTestRunner().run(suite)

  # Set the exit code based on the test result
  sys.exit(not result.wasSuccessful())
