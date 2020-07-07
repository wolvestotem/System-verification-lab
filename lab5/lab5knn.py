import sys
import numpy as np

from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":

  X = np.loadtxt(sys.argv[1])
  y = np.loadtxt(sys.argv[2], dtype=np.int)

  X_grading = np.loadtxt(sys.argv[3])
  knn = KNeighborsClassifier(n_neighbors=20,weights="uniform",algorithm="auto")
  knn.fit(X,y)
  y_grading = knn.predict(X_grading)

  # Use the model to predict the labels of the grading input
  # y_grading = np.zeros_like(y)
  np.savetxt("result.txt", y_grading, fmt="%d")
