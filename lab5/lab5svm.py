import sys
import numpy as np

from sklearn.svm import SVC

if __name__ == "__main__":

  X = np.loadtxt(sys.argv[1])
  y = np.loadtxt(sys.argv[2], dtype=np.int)

  X_grading = np.loadtxt(sys.argv[3])
  rbf = SVC(kernel='rbf',C=0.2,random_state=1)
  rbf.fit(X,y)
  y_grading = rbf.predict(X_grading)

  # Use the model to predict the labels of the grading input
  # y_grading = np.zeros_like(y) 
  np.savetxt("result.txt", y_grading, fmt="%d")
