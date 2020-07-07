import sys
import numpy as np

from sklearn.tree import DecisionTreeClassifier

if __name__ == "__main__":

  X = np.loadtxt(sys.argv[1])
  y = np.loadtxt(sys.argv[2], dtype=np.int)

  X_grading = np.loadtxt(sys.argv[3])

  dt  = DecisionTreeClassifier(max_depth=100)
  dt.fit(X,y)
  # pre_tr = dt.predict(X)
  y_grading = dt.predict(X_grading)

  # Use the model to predict the labels of the grading input
  # y_grading = np.zeros_like(y)  
  np.savetxt("result.txt", y_grading, fmt="%d")
