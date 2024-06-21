import sklearn
import matplotlib.pyplot as plt
from pathlib import Path
import time

start_time = time.time()

import numpy as np
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Poly Kernel SVM:

np.random.seed(42)
X = 2 * np.random.rand(50, 1) - 1
y = 0.2 + 0.1 * X[:, 0] + 0.5 * X[:, 0] ** 2 + np.random.randn(50) / 10
svm_poly_reg = make_pipeline(StandardScaler(),
                             SVR(kernel="poly", degree=2, C=0.01, epsilon=0.1))
svm_poly_reg.fit(X, y)

# Predict:

X_new = [[5.5], [5.0]]
print("Sample prediction: ", svm_poly_reg.predict(X_new))

end_time = time.time()

execution_time= end_time - start_time
print("Funciton execution time: ", execution_time, " seconds")
