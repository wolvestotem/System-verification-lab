import sys
import numpy as np

from sklearn.neural_network import MLPClassifier

if __name__ == "__main__":

  X = np.loadtxt(sys.argv[1])
  y = np.loadtxt(sys.argv[2], dtype=np.int)

  X_grading = np.loadtxt(sys.argv[3])
  clf = MLPClassifier(random_state=1, max_iter=300).fit(X, y)
  y_grading = clf.predict(X_grading)
  # Use the model to predict the labels of the grading input
  # y_grading = np.zeros_like(y)  
  np.savetxt("result.txt", y_grading, fmt="%d")
